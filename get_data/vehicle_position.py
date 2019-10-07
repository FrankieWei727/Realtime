from google.protobuf import json_format
import requests
import json
from protobuf import tfnsw_gtfs_realtime_pb2


def vehcile_position(api, model):

    dir_name = "/Users/frankie/Realtime/Data/vehiclePosition/"

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/' + model,
                            headers={'Authorization': api})
    feed.ParseFromString(response.content)

    message = json_format.MessageToJson(feed)

    df = json.loads(message)
    with open(dir_name + 'vehicle_position.json', 'w') as json_file:
        json.dump(df, json_file)

    # for entity in message:
    #     if entity.HasField('trip_update'):
    #         print(entity)
