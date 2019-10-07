# from google.transit import gtfs_realtime_pb2
from google.protobuf import json_format
import requests
from protobuf_to_dict import protobuf_to_dict
import pandas as pd
import json
from protobuf import tfnsw_gtfs_realtime_pb2
from data_process import Trip_update_data as data_pro


def trip_update(api, model):

    dir_name = "/Users/frankie/Realtime/Data/tripUpdate/"

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/realtime/' + model,
                            headers={'Authorization': api})
    feed.ParseFromString(response.content)

    message = json_format.MessageToJson(feed)

    df = json.loads(message)
    with open(dir_name + 'trip_update.json', 'w') as json_file:
        json.dump(df, json_file)

    data_pro.json_to_csv()


