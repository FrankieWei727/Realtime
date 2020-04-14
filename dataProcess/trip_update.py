from google.protobuf import json_format
import requests
import json
import os
from protobuf import tfnsw_gtfs_realtime_pb2
from dataProcess import trip_update_data_clean as data_clean


def trip_update(api, model, session, trip_update_table, logger):
    print('start getting trip update data.')
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/tripUpdate/'

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/realtime/' + model,
                            headers={'Authorization': api})
    feed.ParseFromString(response.content)

    message = json_format.MessageToJson(feed)

    df = json.loads(message)
    with open(dir_name + 'trip_update.json', 'w') as json_file:
        json.dump(df, json_file)

    print('finish getting trip update data.')

    data_clean.trip_update_date_processing(df, model, session, trip_update_table, logger)
