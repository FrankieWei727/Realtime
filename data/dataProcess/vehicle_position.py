import pytz
from google.protobuf import json_format
import requests
import json
import os
from sqlalchemy import text
from data.protobuf import tfnsw_gtfs_realtime_pb2
from ..database import tables
from datetime import datetime


def vehicle_position(api, model, session, logger):
    logger.info("%s - grab vehicle position info", model)

    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/vehiclePosition/'

    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/' + model,
                            headers={'Authorization': api})
    feed.ParseFromString(response.content)

    logger.info("%s - vehicle position date processing..", model)
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

    for entity in feed.entity:
        entity = entity.vehicle
        if entity.trip.route_id not in not_sydney_train_list and \
                "NonTimetabled" not in entity.trip.trip_id:
            entity_datetime = datetime.fromtimestamp(entity.timestamp,
                                                     tz=pytz.timezone('Australia/Sydney'))
            data = tables.VehiclePosition(
                datetime=entity_datetime,
                vehicle=entity.vehicle.id,
                trip_id=entity.trip.trip_id,
                stop_id=entity.stop_id,
                schedule_relationship=entity.trip.DESCRIPTOR.enum_types_by_name[
                    'ScheduleRelationship'].values_by_number[entity.trip.schedule_relationship].name,
                route_id=entity.trip.route_id,
                lat=entity.position.latitude,
                lon=entity.position.longitude,
                congestion_level=entity.DESCRIPTOR.enum_types_by_name['CongestionLevel'].values_by_number[
                    entity.congestion_level].name,
                label=entity.vehicle.label
            )
            session.add(data)

    session.commit()

    # Execute the sql to delete the duplicate rows of the same vehicle
    query_delete_older_record = '''
            DELETE from public.vehicle_position v1
                        WHERE EXISTS (
                                SELECT *
                                FROM public.vehicle_position v2
                                WHERE v1.vehicle = v2.vehicle
                                    AND v1.trip_id = v2.trip_id
                                    AND v1.stop_id = v2.stop_id
                                    AND v1.schedule_relationship = v2.schedule_relationship
                                    AND v1.route_id = v2.route_id
                                    AND v1.lat = v2.lat
                                    AND v1.lon = v2.lon
                                    AND v1.congestion_level = v2.congestion_level
                                    AND v1.label = v2.label
                                    AND EXTRACT(YEAR FROM v1.datetime) = EXTRACT(YEAR FROM v2.datetime)
                                    AND EXTRACT(MONTH FROM v1.datetime) = EXTRACT(MONTH FROM v2.datetime)
                                    AND EXTRACT(DAY FROM v1.datetime) = EXTRACT(DAY FROM v2.datetime)
                                    AND v1.datetime < v2.datetime);
    '''
    session.execute(text(query_delete_older_record))
    query_delete_duplicate = '''
            DELETE from public.vehicle_position v1
            WHERE EXISTS (
                    SELECT *
                    FROM public.vehicle_position v2
                    WHERE v1.vehicle = v2.vehicle
                        AND v1.trip_id = v2.trip_id
                        AND v1.stop_id = v2.stop_id
                        AND v1.schedule_relationship = v2.schedule_relationship
                        AND v1.route_id = v2.route_id
                        AND v1.lat = v2.lat
                        AND v1.lon = v2.lon
                        AND v1.congestion_level = v2.congestion_level
                        AND v1.label = v2.label
                        AND v1.datetime = v2.datetime
                        AND v1.id < v2.id);
    '''
    session.execute(text(query_delete_duplicate))
    query_reset = '''
            UPDATE public.vehicle_position SET id= (SELECT MAX(id) FROM public.vehicle_position) + nextval('public.vehicle_position_id_seq');
            ALTER SEQUENCE public.vehicle_position_id_seq RESTART;
            UPDATE public.vehicle_position SET id= nextval('public.vehicle_position_id_seq');
    '''
    session.execute(text(query_reset))

    session.commit()

    count = session.query(tables.VehiclePosition.id).count()
    logger.info('%s - vehicle_position - Total %s rows in database', model, count)

    df = json_format.MessageToJson(feed)
    df = json.loads(df)

    with open(dir_name + 'vehicle_position.json', 'w') as json_file:
        json.dump(df, json_file)
