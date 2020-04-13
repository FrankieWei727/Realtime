import os
import pandas as pd
from datetime import date
from sqlalchemy import text


def vehicle_position_data_processing(df, session, vehicle_position_table, logger, model):
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/vehiclePosition/'

    data = df
    session = session
    VehiclePosition = vehicle_position_table
    file_date = date.today().strftime("%Y%m%d")

    print('vehicle position data processing')
    try:
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

        df = pd.DataFrame(
            columns=['date', 'time', 'timestamp', 'vehicle', 'tripId', 'stopId', 'scheduleRelationship', 'routeId',
                     'latitude', 'longitude', 'congestionLevel', 'label'])

        df['vehicle'] = pd.Series(vehicle)
        df['tripId'] = pd.Series(tripId)
        df['stopId'] = pd.Series(stopId)
        df['scheduleRelationship'] = pd.Series(scheduleRelationship)
        df['routeId'] = pd.Series(routeId)
        df['latitude'] = pd.Series(latitude)
        df['longitude'] = pd.Series(longitude)
        df['timestamp'] = pd.Series(timestamp)
        df['congestionLevel'] = pd.Series(congestionLevel)
        df['label'] = pd.Series(label)

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df.timestamp = df.timestamp + pd.Timedelta('10:00:00')
        df.timestamp = df.timestamp.dt.strftime('%Y%m%d %H:%M:%S')
        df['date'], df['time'] = df.timestamp.str.split(' ', 1).str

        df.drop('timestamp', axis=1, inplace=True)

        df = df[~df.tripId.str.contains("NonTimetabled")]

        # Drop the rows of Nsw Trains
        df = df[~(df["routeId"].isin(['BMT_1', 'BMT_2', 'CCN_1a', 'CCN_1b', 'CCN_1c',
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

        df = df.sort_values(by=['time'])

        # Store date to database
        try:
            for entity in df.itertuples():
                data = VehiclePosition(
                    date=entity.date,
                    time=entity.time,
                    vehicle=entity.vehicle,
                    trip_id=entity.tripId,
                    stop_id=entity.stopId,
                    schedule_relationship=entity.scheduleRelationship,
                    route_id=entity.routeId,
                    lat=entity.latitude,
                    lon=entity.longitude,
                    congestion_level=entity.congestionLevel,
                    label=entity.label
                )
                session.add(data)
        except Exception as err:
            print(err)
        session.commit()

        # Execute the sql to delete the duplicate rows of the same vehicle
        query_delete = '''
                DELETE from public.vehicle_position v1
                            WHERE EXISTS (
                                    SELECT *
                                    FROM public.vehicle_position v2
                                    WHERE v1.date = v2.date
                                        AND v1.vehicle = v2.vehicle
                                        AND v1.trip_id = v2.trip_id
                                        AND v1.stop_id = v2.stop_id
                                        AND v1.schedule_relationship = v2.schedule_relationship
                                        AND v1.route_id = v2.route_id
                                        AND v1.lat = v2.lat
                                        AND v1.lon = v2.lon
                                        AND v1.congestion_level = v2.congestion_level
                                        AND v1.label = v2.label
                                        AND v1.id < v2.id);
        '''
        session.execute(text(query_delete))
        query_reset = '''
                  UPDATE public.vehicle_position SET id= (SELECT MAX(id) FROM public.vehicle_position) + nextval('public.vehicle_position_id_seq');
                  ALTER SEQUENCE public.vehicle_position_id_seq RESTART;
                  UPDATE public.vehicle_position SET id= nextval('public.vehicle_position_id_seq');
        '''
        session.execute(text(query_reset))

        session.commit()

        count = session.query(VehiclePosition.id).count()
        logger.info('%s - vehicle_position - Adding %s rows', model, len(df))
        logger.info('%s - vehicle_position - Total %s rows in database', model, count)

    except Exception as err:
        print(err)

    # Output the date to csv
    # hdr = False if os.path.isfile(dir_name + 'vehicle_position_' + file_date + '.csv') else True
    # df.to_csv(dir_name + 'vehicle_position_' + file_date + '.csv', mode='a', header=hdr, index=False)

    print('finish vehicle position data processing')
