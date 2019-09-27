# from google.transit import gtfs_realtime_pb2
import requests
from protobuf_to_dict import protobuf_to_dict
import pandas as pd
from nested_lookup import nested_lookup
from nested_lookup import get_all_keys
from nested_lookup import get_occurrence_of_key, get_occurrence_of_value
import json
from protobuf import tfnsw_gtfs_realtime_pb2

api_key = 'apikey EXmt0Pl6OWxy2OZUo19fus2PYKsMd4F6G7W8'

def trip_update():
    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/realtime/sydneytrains',
                            headers={'Authorization': api_key})
    feed.ParseFromString(response.content)
    print(type(feed))

    message = protobuf_to_dict(feed)

    keys = get_all_keys(message)
    print(message.keys())
    no_of_key_occurrence = get_occurrence_of_key(message, key='trip_update')
    print(no_of_key_occurrence)

    message_dict = message['entity']
    for info in message_dict[10:20]:
        print(info)
        print('\n')

    time = []
    trip = []
    stop_time_update = []
    for mag in message_dict:
        key = get_all_keys(mag)
        time.append(mag['trip_update']['timestamp'])
        trip.append(mag['trip_update']['trip'])
        if 'stop_time_update' in key:
            print('True')
            stop_time_update.append(mag['trip_update']['stop_time_update'])
        else:
            stop_time_update.append('None')

    time = pd.Series(time)
    trip = pd.Series(trip)
    stop_time_update = pd.Series(stop_time_update)
    df = pd.DataFrame(columns = ['time', 'trip', 'stop_time_update'])
    df['time'] = time
    df['trip'] = trip
    df['stop_time_update'] = stop_time_update
    print(df.head())

    df.to_csv('trip_update.csv')



    # for entity in message:
    #     if entity.HasField('trip_update'):
    #         print(entity)


if __name__ == '__main__':
    trip_update()
