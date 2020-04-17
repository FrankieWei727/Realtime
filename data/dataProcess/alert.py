import os
import json
import requests
from sqlalchemy import text
from data.protobuf import tfnsw_gtfs_realtime_pb2
from google.protobuf import json_format
from datetime import datetime
import pytz
from ..database import tables


def alert(api_key, model, session, logger):
    logger.info("%s - grab alert info", model)

    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/alert/'
    feed = tfnsw_gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/alerts/' + model,
                            headers={'Authorization': api_key})

    feed.ParseFromString(response.content)

    logger.info("%s - alert date processing..", model)

    # Convert this a Python object, and save it to be placed into each alert
    timestamp = datetime.fromtimestamp(feed.header.timestamp,
                                       tz=pytz.timezone('Australia/Sydney'))

    for entity in feed.entity:
        entity = entity.alert
        for data in entity.informed_entity:
            if data.HasField('route_id'):
                print(entity)
            if data.HasField('route_id'):
                route = tables.LineAlert(
                    datetime=timestamp,
                    agency_id=data.agency_id,
                    route_id=data.route_id,
                    header_text=entity.header_text.translation[0].text,
                    description_text=entity.description_text.translation[0].text
                )
                session.add(route)
            if data.HasField('stop_id'):
                stop = tables.StationAlert(
                    datetime=timestamp,
                    agency_id=data.agency_id,
                    stop_id=data.stop_id,
                    cause=entity.DESCRIPTOR.enum_types_by_name['Cause'].values_by_number[entity.cause].name,
                    effect=entity.DESCRIPTOR.enum_types_by_name['Effect'].values_by_number[entity.effect].name,
                    header_text=entity.header_text.translation[0].text,
                    description_text=entity.description_text.translation[0].text
                )
                session.add(stop)
            if data.HasField('trip'):
                trip = tables.TripAlert(
                    datetime=timestamp,
                    agency_id=data.agency_id,
                    trip_id=data.trip.trip_id,
                    header_text=entity.header_text.translation[0].text,
                    description_text=entity.description_text.translation[0].text
                )
                session.add(trip)

    session.commit()

    """
        station_alert
    """
    # Remove all duplication rows and reset the id start with 1
    query_delete_older_record = '''
            DELETE FROM public.station_alert s1
                    WHERE EXISTS (
                        SELECT *
                        FROM public.station_alert s2
                        WHERE s1.stop_id = s2.stop_id
                            AND s1.cause = s2.cause
                            AND s1.effect = s2.effect
                            AND s1.header_text = s2.header_text
                            AND s1.description_text = s2.description_text
                            AND s1.datetime < s2.datetime);
    '''
    session.execute(text(query_delete_older_record))
    query_delete_duplicate = '''
            DELETE FROM public.station_alert s1
                    WHERE EXISTS (
                        SELECT *
                        FROM public.station_alert s2
                        WHERE s1.datetime = s2.datetime
                            AND s1.stop_id = s2.stop_id
                            AND s1.cause = s2.cause
                            AND s1.effect = s2.effect
                            AND s1.header_text = s2.header_text
                            AND s1.description_text = s2.description_text
                            AND s1.id < s2.id);
    '''
    session.execute(text(query_delete_duplicate))
    query_reset = '''
              UPDATE public.station_alert SET id= (SELECT MAX(id) FROM public.station_alert) + nextval('public.station_alert_id_seq');
              ALTER SEQUENCE public.station_alert_id_seq RESTART;
              UPDATE public.station_alert SET id= nextval('public.station_alert_id_seq');
    '''
    session.execute(text(query_reset))

    session.commit()

    count = session.query(tables.StationAlert.id).count()
    logger.info('%s - station_alert - Total %s rows in database', model, count)

    """
        line_alert  
    """
    # Remove all duplication rows and reset the id start with 1
    query_delete_older_record = '''
                  DELETE FROM public.line_alert l1
                          WHERE EXISTS (
                              SELECT *
                              FROM public.line_alert l2
                              WHERE l1.route_id = l2.route_id
                                  AND l1.header_text = l2.header_text
                                  AND l1.description_text = l2.description_text
                                  AND l1.datetime < l2.datetime);
          '''
    session.execute(text(query_delete_older_record))
    query_delete_duplicate = '''
                  DELETE FROM public.line_alert l1
                          WHERE EXISTS (
                              SELECT *
                              FROM public.line_alert l2
                              WHERE l1.route_id = l2.route_id
                                  AND l1.header_text = l2.header_text
                                  AND l1.description_text = l2.description_text
                                  AND l1.datetime = l2.datetime
                                  AND l1.id < l2.id);
          '''
    session.execute(text(query_delete_duplicate))
    query_reset = '''
                    UPDATE public.line_alert SET id= (SELECT MAX(id) FROM public.line_alert) + nextval('public.line_alert_id_seq');
                    ALTER SEQUENCE public.line_alert_id_seq RESTART;
                    UPDATE public.line_alert SET id= nextval('public.line_alert_id_seq');
          '''
    session.execute(text(query_reset))

    session.commit()

    count = session.query(tables.LineAlert.id).count()
    logger.info('%s - line_alert - Total %s rows in database', model, count)

    """
        trip_alert
    """

    # Remove all duplication rows and reset the id start with 1
    query_delete_older_record = '''
            DELETE FROM public.trip_alert t1
                    WHERE EXISTS (
                        SELECT *
                        FROM public.trip_alert t2
                        WHERE t1.trip_id = t2.trip_id
                            AND t1.header_text = t2.header_text
                            AND t1.description_text = t2.description_text
                            AND t1.datetime < t2.datetime);
    '''
    session.execute(text(query_delete_older_record))
    query_delete_duplicate = '''
            DELETE FROM public.trip_alert t1
                    WHERE EXISTS (
                        SELECT *
                        FROM public.trip_alert t2
                        WHERE t1.trip_id = t2.trip_id
                            AND t1.header_text = t2.header_text
                            AND t1.description_text = t2.description_text
                            AND t1.datetime = t2.datetime
                            AND t1.id < t2.id);
    '''
    session.execute(text(query_delete_duplicate))
    query_reset = '''
              UPDATE public.trip_alert SET id= (SELECT MAX(id) FROM public.trip_alert) + nextval('public.trip_alert_id_seq');
              ALTER SEQUENCE public.trip_alert_id_seq RESTART;
              UPDATE public.trip_alert SET id= nextval('public.trip_alert_id_seq');
    '''
    session.execute(text(query_reset))

    session.commit()

    count = session.query(tables.TripAlert.id).count()
    logger.info('%s - trip_alert - Total %s rows in database', model, count)

    df = json_format.MessageToJson(feed)
    df = json.loads(df)

    with open(dir_name + 'alert.json', 'w') as json_file:
        json.dump(df, json_file)
