import requests
from protobuf import tfnsw_gtfs_realtime_pb2
from google.protobuf import json_format
import json
import os
from dataProcess import alert_data_clean


def alert(api_key, model):
    print('start getting alter data.')
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/alert/'

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/alerts/' + model,
                            headers={'Authorization': api_key})
    feed.ParseFromString(response.content)

    message = json_format.MessageToJson(feed)

    df = json.loads(message)
    with open(dir_name + 'alert.json', 'w') as json_file:
        json.dump(df, json_file)

    print('finish getting alter data.')
    alert_data_clean.alert_data_processing()
