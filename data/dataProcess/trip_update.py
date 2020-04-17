from datetime import datetime
import pytz
from google.protobuf import json_format
import requests
import json
import os
from sqlalchemy import text
from data.protobuf import tfnsw_gtfs_realtime_pb2
from ..database import tables


def trip_update(api, model, session, logger):
    logger.info("%s - grab trip update info", model)
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/tripUpdate/'

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/realtime/' + model,
                            headers={'Authorization': api})

    feed.ParseFromString(response.content)
    feed = json_format.MessageToJson(feed)
    feed = json.loads(feed)

    logger.info("%s - trip update date processing..", model)

    not_sydney_train_list = ['BMT_1', 'BMT_2', 'CCN_1a', 'CCN_1b', 'CCN_1c',
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
                             'SHL_2d', 'SHL_2e', 'RTTA_DEF', 'RTTA_REV']

    for entity in feed['entity']:
        if entity['tripUpdate']['trip']['routeId'] not in not_sydney_train_list:
            entity_datetime = datetime.fromtimestamp(int(entity['tripUpdate']['timestamp']),
                                                     tz=pytz.timezone('Australia/Sydney'))
            if 'scheduleRelationship' in entity['tripUpdate']['trip']:
                schedule_relationship = entity['tripUpdate']['trip']['scheduleRelationship']
            else:
                schedule_relationship = None
            if 'stopTimeUpdate' in entity['tripUpdate']:
                stop_time_update = entity['tripUpdate']['stopTimeUpdate']
                for stop in stop_time_update:
                    arrival_time = None
                    arrival_delay = None
                    departure_time = None
                    departure_delay = None
                    if 'scheduleRelationship' in stop:
                        update_schedule_relationship = stop['scheduleRelationship']
                    else:
                        update_schedule_relationship = None
                    if 'arrival' in stop:
                        if 'delay' not in stop['arrival'] and 'time' in stop['arrival']:
                            arrival_delay = None
                            arrival_time = datetime.fromtimestamp(int(stop['arrival']['time']),
                                                                  tz=pytz.timezone('Australia/Sydney'))
                        elif 'delay' in stop['arrival'] and 'time' not in stop['arrival']:
                            arrival_delay = stop['arrival']['delay']
                            arrival_time = None
                        else:
                            arrival_time = datetime.fromtimestamp(int(stop['arrival']['time']),
                                                                  tz=pytz.timezone('Australia/Sydney'))
                            arrival_delay = stop['arrival']['delay']
                    if 'departure' in stop:
                        if 'delay' not in stop['departure'] and 'time' in stop['departure']:
                            departure_delay = None
                            departure_time = datetime.fromtimestamp(int(stop['departure']['time']),
                                                                    tz=pytz.timezone('Australia/Sydney'))
                        elif 'delay' in stop['departure'] and 'time' not in stop['departure']:
                            departure_delay = stop['departure']['delay']
                            departure_time = None
                        else:
                            departure_delay = stop['departure']['delay']
                            departure_time = datetime.fromtimestamp(int(stop['departure']['time']),
                                                                    tz=pytz.timezone('Australia/Sydney'))
                    data = tables.TripUpdate(
                        datetime=entity_datetime,
                        trip_id=entity['tripUpdate']['trip']['tripId'],
                        route_id=entity['tripUpdate']['trip']['routeId'],
                        schedule_relationship=schedule_relationship,
                        stop_id=stop['stopId'],
                        update_schedule_relationship=update_schedule_relationship,
                        arrival_delay=arrival_delay,
                        arrival_time=arrival_time,
                        departure_delay=departure_delay,
                        departure_time=departure_time
                    )
                    session.add(data)
            else:
                data = tables.TripUpdate(
                    datetime=entity_datetime,
                    trip_id=entity['tripUpdate']['trip']['tripId'],
                    route_id=entity['tripUpdate']['trip']['routeId'],
                    schedule_relationship=schedule_relationship,
                )
                session.add(data)

    session.commit()

    # Remove all duplication rows and reset the id start with 1
    query_delete_older_record = '''
              DELETE FROM public.trip_update t1
                WHERE EXISTS (
                    SELECT *
                    FROM public.trip_update t2
                    WHERE t1.trip_id = t2.trip_id
                        AND t1.stop_id = t2.stop_id
                        AND t1.datetime < t2.datetime);
    '''
    session.execute(text(query_delete_older_record))
    query_delete_duplicate = '''
              DELETE FROM public.trip_update t1
                WHERE EXISTS (
                    SELECT *
                    FROM public.trip_update t2
                    WHERE t1.trip_id = t2.trip_id
                        AND t1.stop_id = t2.stop_id
                        AND t1.datetime = t2.datetime
                        AND t1.id < t2.id);
    '''
    session.execute(text(query_delete_duplicate))
    query_reset = '''
              UPDATE public.trip_update SET id= (SELECT MAX(id) FROM public.trip_update) + nextval('public.trip_update_id_seq');
              ALTER SEQUENCE public.trip_update_id_seq RESTART;
              UPDATE public.trip_update SET id= nextval('public.trip_update_id_seq');
    '''
    session.execute(text(query_reset))

    session.commit()

    count = session.query(tables.TripUpdate.id).count()
    logger.info('%s - trip_update - Total %s rows in database', model, count)

    with open(dir_name + 'trip_update.json', 'w') as json_file:
        json.dump(feed, json_file)

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
