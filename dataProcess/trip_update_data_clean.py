import os
import pandas as pd
from datetime import date

from sqlalchemy import text


def trip_update_date_processing(df, model, session, trip_update_table, logger):
    session = session
    TripUpdate = trip_update_table
    logger = logger

    data = df
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/tripUpdate/'

    print('trip update data processing.')

    try:
        entities = data['entity']
        entity_timestamp = []
        entity_trip_id = []
        entity_route_id = []
        entity_stop_id = []
        entity_scheduleRelationship = []
        entity_arrival_time = []
        entity_arrival_delay = []
        entity_departure_time = []
        entity_departure_delay = []
        entity_stop_time_update_scheduleRelationship = []

        # pd.Timestamp(None, tz=pytz.timezone('Australia/Sydney'))

        for entity in entities:

            entityTimestamp = entity['tripUpdate']['timestamp']
            entityTripId = entity['tripUpdate']['trip']['tripId']
            entityRouteId = entity['tripUpdate']['trip']['routeId']

            # if the entity has the 'scheduleRelationship' key
            if 'scheduleRelationship' in entity['tripUpdate']['trip']:
                entityScheduleRelationship = entity['tripUpdate']['trip']['scheduleRelationship']
            else:
                entityScheduleRelationship = ''

            # if the entity has the 'stopTimeUpdate' key
            if 'stopTimeUpdate' in entity['tripUpdate']:
                entity_stop_time_update = entity['tripUpdate']['stopTimeUpdate']

                for stop_time_update in entity_stop_time_update:
                    entity_timestamp.append(entityTimestamp)
                    entity_trip_id.append(entityTripId)
                    entity_scheduleRelationship.append(entityScheduleRelationship)
                    entity_route_id.append(entityRouteId)
                    entity_stop_id.append(stop_time_update['stopId'])

                    # if the entity has the 'arrival' key
                    if 'arrival' in stop_time_update:
                        if ('time' in stop_time_update['arrival']) & ('delay' not in stop_time_update['arrival']):
                            entity_arrival_time.append(stop_time_update['arrival']['time'])
                            entity_arrival_delay.append(0)

                        elif ('delay' in stop_time_update['arrival']) & ('time' not in stop_time_update['arrival']):
                            entity_arrival_delay.append(stop_time_update['arrival']['delay'])
                            entity_arrival_time.append(None)
                        else:
                            entity_arrival_time.append(stop_time_update['arrival']['time'])
                            entity_arrival_delay.append(stop_time_update['arrival']['delay'])
                    else:
                        entity_arrival_delay.append(0)
                        entity_arrival_time.append(None)

                    # if the entity has the 'departure' key
                    if 'departure' in stop_time_update:
                        if ('time' in stop_time_update['departure']) & ('delay' not in stop_time_update['departure']):
                            entity_departure_time.append(stop_time_update['departure']['time'])
                            entity_departure_delay.append(0)

                        elif ('delay' in stop_time_update['departure']) & ('time' not in stop_time_update['departure']):
                            entity_departure_delay.append(stop_time_update['departure']['delay'])
                            entity_departure_time.append(None)

                        else:
                            entity_departure_time.append(stop_time_update['departure']['time'])
                            entity_departure_delay.append(stop_time_update['departure']['delay'])

                    else:
                        entity_departure_delay.append(0)
                        entity_departure_time.append(None)

                    # if the entity has the 'scheduleRelationship' key
                    if 'scheduleRelationship' in stop_time_update:
                        entity_stop_time_update_scheduleRelationship.append(stop_time_update['scheduleRelationship'])
                    else:
                        entity_stop_time_update_scheduleRelationship.append('')
            else:
                entity_arrival_delay.append(0)
                entity_arrival_time.append(None)
                entity_departure_delay.append(0)
                entity_departure_time.append(None)
                entity_stop_id.append('')
                entity_stop_time_update_scheduleRelationship.append('')
                entity_timestamp.append(entityTimestamp)
                entity_trip_id.append(entityTripId)
                entity_scheduleRelationship.append(entityScheduleRelationship)
                entity_route_id.append(entityRouteId)

        df = pd.DataFrame(
            columns=['timestamp', 'date', 'time', 'trip_id', 'route_id', 'schedule_relationship', 'stop_id',
                     'arrival_time', 'arrival_delay', 'departure_time', 'departure_delay',
                     'update_scheduleRelationship'])

        df['timestamp'] = pd.Series(entity_timestamp)
        df['trip_id'] = pd.Series(entity_trip_id)
        df['route_id'] = pd.Series(entity_route_id)
        df['schedule_relationship'] = pd.Series(entity_scheduleRelationship)
        df['stop_id'] = pd.Series(entity_stop_id)
        df['departure_delay'] = pd.Series(entity_departure_delay)
        df['departure_time'] = pd.Series(entity_departure_time)
        df['arrival_delay'] = pd.Series(entity_arrival_delay)
        df['arrival_time'] = pd.Series(entity_arrival_time)
        df['update_scheduleRelationship'] = pd.Series(entity_stop_time_update_scheduleRelationship)

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df.timestamp = df.timestamp + pd.Timedelta('10:00:00')
        df.timestamp = df.timestamp.dt.strftime('%Y%m%d %H:%M:%S')

        df.departure_time = pd.to_datetime(df['departure_time'], unit='s')
        df.arrival_time = pd.to_datetime(df['arrival_time'], unit='s')
        df.departure_time = df.departure_time + pd.Timedelta('10:00:00')
        df.arrival_time = df.arrival_time + pd.Timedelta('10:00:00')
        df.departure_time = df.departure_time.dt.strftime('%Y%m%d %H:%M:%S')
        df.arrival_time = df.arrival_time.dt.strftime('%Y%m%d %H:%M:%S')

        df = df.replace({'NaT': None})

        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        df['time'] = pd.to_datetime(df['timestamp']).dt.time
        df.drop('timestamp', axis=1, inplace=True)

        # Drop the rows of Nsw Trains
        df = df[~(df["route_id"].isin(['BMT_1', 'BMT_2', 'CCN_1a', 'CCN_1b', 'CCN_1c',
                                       'CCN_2a', 'CCN_2b', 'CTY_NC1', 'CTY_NC1a',
                                       'CTY_NC2', 'CTY_NW1a', 'CTY_NW1b', 'CTY_NW1c',
                                       'CTY_NW1d', 'CTY_NW2a', 'CTY_NW2b', 'CTY_S1a',
                                       'CTY_S1b', 'CTY_S1c', 'CTY_S1d', 'CTY_S1e',
                                       'CTY_S1f', 'CTY_S1g', 'CTY_S1h', 'CTY_S1i',
                                       'CTY_S2a', 'CTY_S2b', 'CTY_S2c', 'CTY_S2d',
                                       'CTY_S2e', 'CTY_S2f', 'CTY_S2g', 'CTY_S2h',
                                       'CTY_S2i', 'CTY_W1a', 'CTY_W1b', 'CTY_W2a',
                                       'CTY_W2b', 'HUN_1a', 'HUN_1b', 'HUN_2a',
                                       'HUN_2b', 'SCO_1a', 'SCO_1b', 'SCO_2a',
                                       'SCO_2b', 'SHL_1a', 'SHL_1b', 'SHL_1c',
                                       'SHL_1d', 'SHL_1e', 'SHL_2a', 'SHL_2b', 'SHL_2c',
                                       'SHL_2d', 'SHL_2e', 'RTTA_DEF', 'RTTA_REV']))]

        # Store date to the database
        try:
            for entity in df.itertuples():
                data = TripUpdate(
                    date=entity.date,
                    time=entity.time,
                    trip_id=entity.trip_id,
                    route_id=entity.route_id,
                    stop_id=entity.stop_id,
                    schedule_relationship=entity.schedule_relationship,
                    arrival_time=entity.arrival_time,
                    arrival_delay=entity.arrival_delay,
                    departure_time=entity.departure_time,
                    departure_delay=entity.departure_delay,
                    update_scheduleRelationship=entity.update_scheduleRelationship
                )
                session.add(data)
        except Exception as err:
            raise err

        session.commit()

        # Remove all duplication rows and reset the id start with 1
        query_delete = '''
                  DELETE FROM public.trip_update t1
                    WHERE EXISTS (
                        SELECT *
                        FROM public.trip_update t2
                        WHERE t1.date = t2.date
                            AND t1.trip_id = t2.trip_id
                            AND t1.stop_id = t2.stop_id
                            AND t1.time < t2.time);
        '''
        session.execute(text(query_delete))
        query_reset = '''
                  UPDATE public.trip_update SET id= (SELECT MAX(id) FROM public.trip_update) + nextval('public.trip_update_id_seq');
                  ALTER SEQUENCE public.trip_update_id_seq RESTART;
                  UPDATE public.trip_update SET id= nextval('public.trip_update_id_seq');
        '''
        session.execute(text(query_reset))

        session.commit()

        count = session.query(TripUpdate.id).count()
        logger.info('%s - trip_update - Adding %s rows', model, len(df))
        logger.info('%s - trip_update - Total %s rows in database', model, count)

        # Get the timetable current date
        # file_date = date.today().strftime("%Y%m%d")

        # Output the data to csv file
        # if os.path.isfile(dir_name + 'trip_update_' + file_date + '.csv'):
        #     df2 = pd.read_csv(dir_name + 'trip_update_' + file_date + '.csv', dtype={'stop_id': 'str'})
        #     df2 = pd.concat([df, df2]).drop_duplicates(subset=['trip_id', 'stop_id']).reset_index(drop=True)
        #     df2 = df2.sort_values(by=['time'])
        #     print(len(df), len(df2))
        #     df2.to_csv(dir_name + 'trip_update_' + file_date + '.csv', index=False)
        # else:
        #     df = df.drop_duplicates()
        #     df = df.sort_values(by=['time'])
        #     df['stop_id'] = df['stop_id'].astype('str')
        #     df.to_csv(dir_name + 'trip_update_' + file_date + '.csv', index=False)

    except Exception as err:
        raise err

    print('finish trip update data processing.')
