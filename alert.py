import requests
from protobuf_to_dict import protobuf_to_dict
import pandas as pd
from nested_lookup import nested_lookup
from nested_lookup import get_all_keys
from nested_lookup import get_occurrence_of_key, get_occurrence_of_value
import json
from protofbuf import tfnsw_gtfs_realtime_pb2

api_key = 'apikey EXmt0Pl6OWxy2OZUo19fus2PYKsMd4F6G7W8'


def alert():
    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/alerts/sydneytrains',
                            headers={'Authorization': api_key})
    feed.ParseFromString(response.content)
    print(type(feed))
    for entity in feed.entity:
        if entity.HasField('alert'):
            print(entity)


if __name__ == '__main__':
    alert()
