from datetime import date

import numpy as np
import requests
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import os
from sqlalchemy import text
from ..database import tables


def timetable(api, model, session, logger):
    logger.info("%s - grab static timetable info", model)
    os.chdir(os.path.dirname(__file__))

    # Get the timetable current date
    today = date.today().strftime("%Y%m%d")

    path = os.getcwd() + '/timetable/'

    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/schedule/' + model,
                            headers={'Authorization': api})

    files = ZipFile(BytesIO(response.content))
    files.extractall(path=path)

    logger.info("%s - timetable date processing..", model)

    df_routes = pd.read_csv(files.open('routes.txt'))
    df_agency = pd.read_csv(files.open('agency.txt'))
    df_calendar = pd.read_csv(files.open('calendar.txt'))
    df_shapes = pd.read_csv(files.open('shapes.txt'))
    df_stop_times = pd.read_csv(files.open('stop_times.txt'), dtype={"stop_id": str, "stop_headsign": str})
    df_stops = pd.read_csv(files.open('stops.txt'))
    df_trips = pd.read_csv(files.open('trips.txt'))

    # add parent station name to stops
    parent_station_name = []
    for row in df_stops.itertuples():
        if pd.notnull(row.parent_station):
            parent_station_name.append(df_stops[df_stops['stop_code'] == row.parent_station].stop_name.values[0])
        else:
            parent_station_name.append(np.nan)
    df_stops['parent_station_name'] = pd.Series(parent_station_name)

    # Merge agency.csv and routes.csv
    df_update = pd.merge(df_routes, df_agency, on='agency_id')
    # Merge trips.csv
    df_update = pd.merge(df_trips, df_update, on='route_id')
    # Merge calendar.csv
    df_update = pd.merge(df_update, df_calendar, on='service_id')
    # Merge stop_times.csv and stops.csv
    df_update_stop = pd.merge(df_stops, df_stop_times, on='stop_id')
    # Merge df_update and df_update_stop
    df = pd.merge(df_update, df_update_stop, on='trip_id')

    # Drop columns
    df = df.drop(['stop_desc', 'zone_id', 'stop_url', 'stop_timezone', 'shape_dist_traveled',
                  'trip_short_name', 'route_url', 'agency_phone', 'agency_lang',
                  'agency_url', 'route_desc', 'agency_id', 'stop_headsign', 'stop_code'], axis=1)

    df = df.astype({"route_id": str, "parent_station": str, "end_date": str, "start_date": str, "block_id": str})
    df = df[df.start_date == today]

    # Services with route_id as RTTA_DEF or RTTA_REV are non-revenue services and should be excluded
    df = df[~(df["route_id"].isin(['RTTA_DEF', 'RTTA_REV']))]

    # Drop the rows of NSW Trains
    df = df[df['agency_name'] != 'NSW Trains']

    df.sort_values(['start_date', 'trip_id', 'arrival_time'], ascending=[True, True, True], inplace=True)

    # Set the time to None and drop them when the time is > 24:00:00, example 24:33:00
    df['arrival_time'] = pd.to_datetime(df['arrival_time'], errors='coerce')
    df['departure_time'] = pd.to_datetime(df['departure_time'], errors='coerce')
    df = df[pd.notnull(df['arrival_time'])]
    df = df[pd.notnull(df['departure_time'])]

    # Store date to database
    try:
        for entity in df.itertuples():
            data = tables.Timetable(
                start_date=entity.start_date,
                end_date=entity.end_date,
                arrival_time=entity.arrival_time,
                departure_time=entity.departure_time,
                route_id=entity.route_id,
                route_short_name=entity.route_short_name,
                route_long_name=entity.route_long_name,
                route_type=entity.route_type,
                route_color=entity.route_color,
                route_text_color=entity.route_text_color,
                service_id=entity.service_id,
                trip_id=entity.trip_id,
                trip_headsign=entity.trip_headsign,
                direction_id=entity.direction_id,
                stop_id=entity.stop_id,
                stop_name=entity.stop_name,
                stop_sequence=entity.stop_sequence,
                pickup_type=entity.pickup_type,
                drop_off_type=entity.drop_off_type,
                block_id=entity.block_id,
                shape_id=entity.shape_id,
                stop_lat=entity.stop_lat,
                stop_lon=entity.stop_lon,
                location_type=entity.location_type,
                parent_station=entity.parent_station,
                parent_station_name=entity.parent_station_name,
                wheelchair_accessible=entity.wheelchair_accessible,
                monday=entity.monday,
                tuesday=entity.tuesday,
                wednesday=entity.wednesday,
                thursday=entity.thursday,
                friday=entity.friday,
                saturday=entity.saturday,
                sunday=entity.sunday,
                agency_name=entity.agency_name,
                agency_timezone=entity.agency_timezone
            )
            session.add(data)
    except Exception as err:
        print(err)

    session.commit()

    # Remove all duplication rows and reset the id start with 1
    query_delete = '''
                      DELETE FROM public.timetable t1
                        WHERE EXISTS (
                            SELECT *
                            FROM public.timetable t2
                            WHERE t1.start_date = t2.start_date
                                AND t1.end_date = t2.end_date
                                AND t1.trip_id = t2.trip_id
                                AND t1.arrival_time = t2.arrival_time
                                AND t1.departure_time = t2.departure_time
                                AND t1.id < t2.id);
            '''
    session.execute(text(query_delete))
    query_reset = '''
                      UPDATE public.timetable SET id= (SELECT MAX(id) FROM public.timetable) + nextval('public.timetable_id_seq');
                      ALTER SEQUENCE public.timetable_id_seq RESTART;
                      UPDATE public.timetable SET id= nextval('public.timetable_id_seq');
            '''
    session.execute(text(query_reset))

    session.commit()

    count = session.query(tables.Timetable.id).count()
    logger.info('%s - timetable - Total %s rows in database', model, count)

    # Rearrange the order of columns
    # df = df[
    #     ['start_date', 'end_date', 'arrival_time', 'departure_time', 'route_id', 'route_short_name', 'route_long_name',
    #      'route_type', 'route_color', 'route_text_color', 'service_id', 'trip_id', 'trip_headsign', 'direction_id',
    #      'stop_id', 'stop_name', 'stop_sequence', 'pickup_type', 'drop_off_type', 'block_id', 'shape_id', 'stop_lat',
    #      'stop_lon', 'location_type', 'parent_station', 'parent_station_name', 'wheelchair_accessible',
    #      'wheelchair_boarding', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
    #      'agency_name', 'agency_timezone']]

    # Output all the data to csv file
    # df.to_csv(path + 'timetable_' + today + '.csv', index=False)
