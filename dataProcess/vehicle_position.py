from google.protobuf import json_format
import requests
import json
import os
from protobuf import tfnsw_gtfs_realtime_pb2
from dataProcess import vehicle_position_data_clean as data_clean


def vehicle_position(api, model, session, vehicle_position_table, logger):
    print('start getting vehicle position data.')
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/vehiclePosition/'

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/' + model,
                            headers={'Authorization': api})
    feed.ParseFromString(response.content)

    message = json_format.MessageToJson(feed)

    df = json.loads(message)

    with open(dir_name + 'vehicle_position.json', 'w') as json_file:
        json.dump(df, json_file)

    print('finish getting vehicle position data.')

    data_clean.vehicle_position_data_processing(df, session, vehicle_position_table, logger, model)
