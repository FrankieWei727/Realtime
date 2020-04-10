import json
import os
import pandas as pd
from datetime import date

file_date = date.today().strftime("%Y%m%d")


def vehicle_position_data_processing(df):
    print('vehicle position data processing')
    # with open("vehicle_position.json", "r") as read_file:
    #     data = json.load(read_file)

    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/vehiclePosition/'

    data = df

    vehicle = []
    tripId = []
    stopId = []
    scheduleRelationship = []
    routeId = []
    latitude = []
    longitude = []
    timestamp = []
    congestionLevel = []
    label = []

    for entity in data['entity']:
        vehicle.append(entity['vehicle']['vehicle']['id'])
        tripId.append(entity['vehicle']['trip']['tripId'])
        stopId.append(entity['vehicle']['stopId'])
        if 'routeId' in entity['vehicle']['trip']:
            routeId.append(entity['vehicle']['trip']['routeId'])
        else:
            routeId.append("")
        scheduleRelationship.append(entity['vehicle']['trip']['scheduleRelationship'])
        latitude.append(entity['vehicle']['position']['latitude'])
        longitude.append(entity['vehicle']['position']['longitude'])
        timestamp.append(entity['vehicle']['timestamp'])
        congestionLevel.append(entity['vehicle']['congestionLevel'])
        if 'label' in entity['vehicle']['vehicle']:
            label.append(entity['vehicle']['vehicle']['label'])
        else:
            label.append("")

    df = pd.DataFrame(columns=['timestamp', 'vehicle', 'tripId', 'stopId', 'scheduleRelationship', 'routeId',
                               'latitude', 'longitude', 'congestionLevel', 'label'])

    vehicle = pd.Series(vehicle)
    df['vehicle'] = vehicle

    tripId = pd.Series(tripId)
    df['tripId'] = tripId

    stopId = pd.Series(stopId)
    df['stopId'] = stopId

    scheduleRelationship = pd.Series(scheduleRelationship)
    df['scheduleRelationship'] = scheduleRelationship

    routeId = pd.Series(routeId)
    df['routeId'] = routeId

    latitude = pd.Series(latitude)
    df['latitude'] = latitude

    longitude = pd.Series(longitude)
    df['longitude'] = longitude

    timestamp = pd.Series(timestamp)
    df['timestamp'] = timestamp

    congestionLevel = pd.Series(congestionLevel)
    df['congestionLevel'] = congestionLevel

    label = pd.Series(label)
    df['label'] = label

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.timestamp = df.timestamp + pd.Timedelta('10:00:00')
    df.timestamp = df.timestamp.dt.strftime('%Y%m%d %H:%M:%S')

    hdr = False if os.path.isfile(dir_name + 'vehicle_position_' + file_date + '.csv') else True
    df.to_csv(dir_name + 'vehicle_position_' + file_date + '.csv', mode='a', header=hdr, index=False)

    print('finish vehicle position data processing')
