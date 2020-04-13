import json
import os
import pandas as pd
import numpy as np
from datetime import date


def trip_update_date_processing(df):
    print('trip update data processing.')

    data = df
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/tripUpdate/'

    entities = data['entity']
    entity_id = []
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

    for entity in entities:
        # id
        entityId = entity['id']

        # id/tripipdate/timestamp
        entityTimestamp = entity['tripUpdate']['timestamp']

        # id/tripipdate/trip/tripid
        entityTripId = entity['tripUpdate']['trip']['tripId']

        # id/tripipdate/trip/scheduleRelationship
        if 'scheduleRelationship' in entity['tripUpdate']['trip']:
            entityScheduleRelationship = entity['tripUpdate']['trip']['scheduleRelationship']
        else:
            entityScheduleRelationship = ""

        # id/tripipdate/trip/routeid
        entityRouteId = entity['tripUpdate']['trip']['routeId']

        # id/tripipdate/stopTimeUpdate
        if 'stopTimeUpdate' in entity['tripUpdate']:
            entity_stop_time_update = entity['tripUpdate']['stopTimeUpdate']

            for stoptimeupdate in entity_stop_time_update:
                entity_id.append(entityId)
                entity_timestamp.append(entityTimestamp)
                entity_trip_id.append(entityTripId)
                entity_scheduleRelationship.append(entityScheduleRelationship)
                entity_route_id.append(entityRouteId)

                entityArrivalDelay = ""
                entityArrivalTime = ""
                # id/tripipdate/stopTimeUpdate/arrival
                if 'arrival' in stoptimeupdate:
                    if ('time' in stoptimeupdate['arrival']) & ('delay' not in stoptimeupdate['arrival']):
                        entityArrivalTime = stoptimeupdate['arrival']['time']
                        entity_arrival_time.append(entityArrivalTime)

                        entity_arrival_delay.append(entityArrivalDelay)

                    elif ('delay' in stoptimeupdate['arrival']) & ('time' not in stoptimeupdate['arrival']):
                        entityArrivalDelay = stoptimeupdate['arrival']['delay']
                        entity_arrival_delay.append(entityArrivalDelay)

                        entity_arrival_time.append(entityArrivalTime)
                    else:
                        entityArrivalTime = stoptimeupdate['arrival']['time']
                        entity_arrival_time.append(entityArrivalTime)
                        entityArrivalDelay = stoptimeupdate['arrival']['delay']
                        entity_arrival_delay.append(entityArrivalDelay)

                else:
                    entity_arrival_delay.append(entityArrivalDelay)
                    entity_arrival_time.append(entityArrivalTime)

                entityDepartureDelay = ""
                entityDepartureTime = ""
                # id/tripipdate/stopTimeUpdate/arrival/departure
                if 'departure' in stoptimeupdate:
                    if ('time' in stoptimeupdate['departure']) & ('delay' not in stoptimeupdate['departure']):
                        entityDepartureTime = stoptimeupdate['departure']['time']
                        entity_departure_time.append(entityDepartureTime)

                        entity_departure_delay.append(entityDepartureDelay)
                    elif ('delay' in stoptimeupdate['departure']) & ('time' not in stoptimeupdate['departure']):
                        entityDepartureDelay = stoptimeupdate['departure']['delay']
                        entity_departure_delay.append(stoptimeupdate['departure']['delay'])

                        entity_departure_time.append(entityDepartureTime)
                    else:
                        entityDepartureTime = stoptimeupdate['departure']['time']
                        entity_departure_time.append(entityDepartureTime)
                        entityDepartureDelay = stoptimeupdate['departure']['delay']
                        entity_departure_delay.append(stoptimeupdate['departure']['delay'])

                else:
                    entityDepartureDelay = ""
                    entity_departure_delay.append(entityDepartureDelay)
                    entityDepartureTime = ""
                    entity_departure_time.append(entityDepartureTime)

                #           id/tripipdate/stopTimeUpdate/arrival/scheduleRelationship
                if 'scheduleRelationship' in stoptimeupdate:
                    entityStopTimeScheduleRelationship = stoptimeupdate['scheduleRelationship']
                    entity_stop_time_update_scheduleRelationship.append(stoptimeupdate['scheduleRelationship'])
                else:
                    entityStopTimeScheduleRelationship = ""
                    entity_stop_time_update_scheduleRelationship.append(entityStopTimeScheduleRelationship)

                #           id/tripipdate/stopTimeUpdate/stopid
                entityStopId = stoptimeupdate['stopId']
                entity_stop_id.append(entityStopId)
        else:
            entityArrivalDelay = ""
            entity_arrival_delay.append(entityArrivalDelay)
            entityArrivalTime = ""
            entity_arrival_time.append(entityArrivalTime)

            entityDepartureDelay = ""
            entity_departure_delay.append(entityDepartureDelay)
            entityDepartureTime = ""
            entity_departure_time.append(entityDepartureTime)

            entityStopId = ""
            entity_stop_id.append(entityStopId)

            entityStopTimeScheduleRelationship = ""
            entity_stop_time_update_scheduleRelationship.append(entityStopTimeScheduleRelationship)

            entity_id.append(entityId)
            entity_timestamp.append(entityTimestamp)
            entity_trip_id.append(entityTripId)
            entity_scheduleRelationship.append(entityScheduleRelationship)
            entity_route_id.append(entityRouteId)

    df = pd.DataFrame(columns=['id', 'timestamp', 'trip_id', 'route_id', 'schedule_relationship',
                               'stop_id', 'departure_delay', 'departure_time', 'arrival_delay',
                               'arrival_time', 'update_scheduleRelationship'])

    entities_id = pd.Series(entity_id)
    df['id'] = entities_id

    entity_timestamp = pd.Series(entity_timestamp)
    df['timestamp'] = entity_timestamp

    entity_trip_id = pd.Series(entity_trip_id)
    df['trip_id'] = entity_trip_id

    entity_route_id = pd.Series(entity_route_id)
    df['route_id'] = entity_route_id

    entity_scheduleRelationship = pd.Series(entity_scheduleRelationship)
    df['schedule_relationship'] = entity_scheduleRelationship

    entity_stop_id = pd.Series(entity_stop_id)
    df['stop_id'] = entity_stop_id

    entity_departure_delay = pd.Series(entity_departure_delay)
    df['departure_delay'] = entity_departure_delay

    entity_departure_time = pd.Series(entity_departure_time)
    df['departure_time'] = entity_departure_time

    entity_arrival_delay = pd.Series(entity_arrival_delay)
    df['arrival_delay'] = entity_arrival_delay

    entity_arrival_time = pd.Series(entity_arrival_time)
    df['arrival_time'] = entity_arrival_time

    entity_stop_time_update_scheduleRelationship = pd.Series(entity_stop_time_update_scheduleRelationship)
    df['update_scheduleRelationship'] = entity_stop_time_update_scheduleRelationship

    df.drop('id', axis=1, inplace=True)

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.timestamp = df.timestamp + pd.Timedelta('10:00:00')
    df.timestamp = df.timestamp.dt.strftime('%Y%m%d %H:%M:%S')

    try:
        df['departure_time'] = pd.to_datetime(df['departure_time'], unit='s')
        df.departure_time = df.departure_time + pd.Timedelta('10:00:00')
        df.departure_time = df.departure_time.dt.strftime('%Y%m%d %H:%M:%S')
        df.departure_time = df.departure_time.str.split(' ', 1).str[1]
    except:
        df.departure_time = ""

    try:
        df['arrival_time'] = pd.to_datetime(df['arrival_time'], unit='s')
        df.arrival_time = df.arrival_time + pd.Timedelta('10:00:00')
        df.arrival_time = df.arrival_time.dt.strftime('%Y%m%d %H:%M:%S')
        df.arrival_time = df.arrival_time.str.split(' ', 1).str[1]
    except:
        df.arrival_time = ""

    df['date'], df['time'] = df.timestamp.str.split(' ', 1).str
    df.drop('timestamp', axis=1, inplace=True)

    # re-arrange the order of columns
    df = df[['date', 'time', 'trip_id', 'route_id', 'schedule_relationship', 'stop_id', 'arrival_time',
             'arrival_delay', 'departure_time', 'departure_delay', 'update_scheduleRelationship']]
    df.reset_index(drop=True, inplace=True)

    file_date = df.date[0]

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

    # df.to_csv(dir_name + 'test_ trip_update_' + file_date + '.csv', index=False)

    if os.path.isfile(dir_name + 'trip_update_' + file_date + '.csv'):
        df2 = pd.read_csv(dir_name + 'trip_update_' + file_date + '.csv', dtype={'stop_id': 'str'})
        df2 = pd.concat([df, df2]).drop_duplicates(subset=['trip_id', 'stop_id']).reset_index(drop=True)
        df2 = df2.sort_values(by=['time'])
        print(len(df), len(df2))
        df2.to_csv(dir_name + 'trip_update_' + file_date + '.csv', index=False)
    else:
        df = df.drop_duplicates()
        df = df.sort_values(by=['time'])
        df['stop_id'] = df['stop_id'].astype('str')
        df.to_csv(dir_name + 'trip_update_' + file_date + '.csv', index=False)

    # hdr = False if os.path.isfile(dir_name + 'trip_update_' + file_date + '.csv') else True
    # df.to_csv(dir_name + 'trip_update_' + file_date + '.csv', mode='a', header=hdr, index=False)

    print('finish trip update data processing.')
