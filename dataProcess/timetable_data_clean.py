import pandas as pd
from datetime import date
import os


def timetable_data_processing():
    print('timetable data processing')

    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/timetable/'

    df_agency = pd.read_csv(dir_name + 'agency.csv')
    df_calendar = pd.read_csv(dir_name + 'calendar.csv')
    df_routes = pd.read_csv(dir_name + 'routes.csv')
    df_shapes = pd.read_csv(dir_name + 'shapes.csv')
    df_stop_times = pd.read_csv(dir_name + 'stop_times.csv', dtype={"stop_id": object})
    df_stops = pd.read_csv(dir_name + 'stops.csv')
    df_trips = pd.read_csv(dir_name + 'trips.csv')

    df_stop_times['stop_id'] = df_stop_times['stop_id'].astype('str')

    # merge agency.csv and routes.csv
    df_update = pd.merge(df_routes, df_agency, on='agency_id')
    # merge trips.csv
    df_update = pd.merge(df_trips, df_update, on='route_id')
    # merge calendar.csv
    df_update = pd.merge(df_update, df_calendar, on='service_id')

    # merge stop_times.csv and stops.csv
    df_update_stop = pd.merge(df_stops, df_stop_times, on='stop_id')

    # merge df_update and df_update_stop
    df = pd.merge(df_update, df_update_stop, on='trip_id')

    df = df.drop(['stop_desc', 'zone_id', 'stop_url', 'stop_timezone', 'shape_dist_traveled',
                  'trip_short_name', 'route_url', 'agency_phone', 'agency_lang',
                  'agency_url', 'route_desc', 'agency_id', 'stop_headsign', 'stop_code'], axis=1)

    # Services with route_id as RTTA_DEF or RTTA_REV are non-revenue services and should be excluded
    df = df[(df['route_id'] != 'RTTA_DEF')]
    df = df[(df['route_id'] != 'RTTA_REV')]

    # replace the null value to 'No BlockID'
    df['block_id'].fillna('No BlockID', inplace=True)

    # checke the NaN value
    # plt.figure(figsize=(20,6))
    # sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    df[df.isnull()].count()

    df.sort_values(['start_date', 'route_id', 'trip_id'], ascending=[True, True, True], inplace=True)

    # rearrage the order of columns
    df = df[['start_date', 'end_date',
             'arrival_time', 'departure_time',
             'route_id', 'route_short_name', 'route_long_name', 'route_type', 'route_color', 'route_text_color',
             'service_id', 'trip_id', 'trip_headsign', 'direction_id',
             'stop_id', 'stop_name', 'stop_sequence', 'pickup_type', 'drop_off_type', 'block_id', 'shape_id',
             'stop_lat', 'stop_lon', 'location_type', 'parent_station', 'wheelchair_accessible', 'wheelchair_boarding',
             'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
             'agency_name', 'agency_timezone']]
    df.reset_index(drop=True, inplace=True)

    df = df.astype({"route_id": str,
                    "parent_station": str,
                    "end_date": str,
                    "start_date": str,
                    "block_id": str})

    today = date.today().strftime("%Y%m%d")
    print("Today's date:", today)

    df = df[df.start_date == today]

    df.to_csv(dir_name + 'timetable_' + today + '.csv', index=False)

    print('finish timetable data processing')
