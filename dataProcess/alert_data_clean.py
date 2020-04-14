import os
import pandas as pd
from datetime import date, datetime

from sqlalchemy import text

file_date = date.today().strftime("%Y%m%d")


def alert_data_processing(df, model, session, station_alert_table, line_alert_table, trip_alert_table, logger):
    session = session
    logger = logger
    StationAlert = station_alert_table
    LineAlert = line_alert_table
    TripAlert = trip_alert_table

    today = date.today().strftime("%Y%m%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    data = df
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/alert/'

    print('alter data processing.')

    entities = data['entity']
    line_service_alerts = []
    station_facilities_alerts = []
    trip_based_alerts = []

    for line_service_alert in entities:
        alerts = line_service_alert['alert']['informedEntity']
        keep_running = True
        for alert in alerts:
            if 'routeId' in alert and keep_running is True:
                line_service_alerts.append(line_service_alert)
                keep_running = False
            else:
                break

    for station_facilities_alert in entities:
        alerts = station_facilities_alert['alert']['informedEntity']
        keep_running = True
        for alert in alerts:
            if 'stopId' in alert and keep_running is True:
                station_facilities_alerts.append(station_facilities_alert)
                keep_running = False

    for trip_based_alert in entities:
        alerts = trip_based_alert['alert']['informedEntity']
        keep_running = True
        for alert in alerts:
            if 'trip' in alert and keep_running is True:
                trip_based_alerts.append(trip_based_alert)
                keep_running = False

    df_station = pd.DataFrame(
        columns=['date', 'time', 'agencyId', 'stopId', 'cause', 'effect', 'headerText', 'descriptionText'])
    df_line = pd.DataFrame(columns=['date', 'time', 'agencyId', 'routeId',
                                    'headerText', 'descriptionText'])
    df_trip = pd.DataFrame(columns=['date', 'time', 'agencyId', 'tripId', 'headerText', 'descriptionText'])

    if len(station_facilities_alerts) > 0:
        station_facilities_alerts_date = []
        station_facilities_alerts_time = []
        station_facilities_alerts_agencyId = []
        station_facilities_alerts_stopId = []
        station_facilities_alerts_cause = []
        station_facilities_alerts_effect = []
        station_facilities_alerts_headerText = []
        station_facilities_alerts_descriptionText = []

        for entity in station_facilities_alerts:
            station_facilities_alerts_date.append(today)
            station_facilities_alerts_time.append(current_time)
            station_facilities_alerts_agencyId.append(entity['alert']['informedEntity'][0]['agencyId'])
            station_facilities_alerts_stopId.append(entity['alert']['informedEntity'][0]['stopId'])
            station_facilities_alerts_cause.append(entity['alert']['cause'])
            station_facilities_alerts_effect.append(entity['alert']['effect'])
            station_facilities_alerts_headerText.append(entity['alert']['headerText']['translation'][0]['text'])
            station_facilities_alerts_descriptionText.append(
                entity['alert']['descriptionText']['translation'][0]['text'])

        df_station['date'] = pd.Series(station_facilities_alerts_date)
        df_station['time'] = pd.Series(station_facilities_alerts_time)
        df_station['agencyId'] = pd.Series(station_facilities_alerts_agencyId)
        df_station['stopId'] = pd.Series(station_facilities_alerts_stopId)
        df_station['cause'] = pd.Series(station_facilities_alerts_cause)
        df_station['effect'] = pd.Series(station_facilities_alerts_effect)
        df_station['headerText'] = pd.Series(station_facilities_alerts_headerText)
        df_station['descriptionText'] = pd.Series(station_facilities_alerts_descriptionText)

        df_station.drop_duplicates(
            subset=['time', 'agencyId', 'stopId', 'cause', 'effect', 'headerText', 'descriptionText'], inplace=True)

        try:
            for entity in df_station.itertuples():
                data = StationAlert(
                    date=entity.date,
                    time=entity.time,
                    agency_id=entity.agencyId,
                    stop_id=entity.stopId,
                    cause=entity.cause,
                    effect=entity.effect,
                    header_text=entity.headerText,
                    description_text=entity.descriptionText
                )
                session.add(data)
        except Exception as err:
            print(err)
        session.commit()

        # Remove all duplication rows and reset the id start with 1
        query_delete = '''
                DELETE FROM public.station_alert s1
                        WHERE EXISTS (
                            SELECT *
                            FROM public.station_alert s2
                            WHERE s1.date = s2.date
                                AND s1.stop_id = s2.stop_id
                                AND s1.cause = s2.cause
                                AND s1.effect = s2.effect
                                AND s1.header_text = s2.header_text
                                AND s1.description_text = s2.description_text
                                AND s1.time < s2.time);
        '''
        session.execute(text(query_delete))
        query_reset = '''
                  UPDATE public.station_alert SET id= (SELECT MAX(id) FROM public.station_alert) + nextval('public.station_alert_id_seq');
                  ALTER SEQUENCE public.station_alert_id_seq RESTART;
                  UPDATE public.station_alert SET id= nextval('public.station_alert_id_seq');
        '''
        session.execute(text(query_reset))

        count = session.query(StationAlert.id).count()
        logger.info('%s - station_alert - Adding %s rows', model, len(df_station))
        logger.info('%s - station_alert - Total %s rows in database', model, count)

        # hdr = False if os.path.isfile(dir_name + 'station_facilities_alerts_' + file_date + '.csv') else True
        # df_station.to_csv(dir_name + 'station_facilities_alerts_' + file_date + '.csv', mode='a', header=hdr,
        #                   index=False)

    if len(line_service_alerts) > 0:
        line_service_alerts_date = []
        line_service_alerts_time = []
        line_service_alerts_agencyId = []
        line_service_alerts_routeId = []
        line_service_alerts_headerText = []
        line_service_alerts_descriptionText = []
        for entity in line_service_alerts:
            for sub_entity in entity['alert']['informedEntity']:
                line_service_alerts_date.append(today)
                line_service_alerts_time.append(current_time)
                line_service_alerts_agencyId.append(sub_entity['agencyId'])
                line_service_alerts_routeId.append(sub_entity['routeId'])
                line_service_alerts_headerText.append(entity['alert']['headerText']['translation'][0]['text'])
                line_service_alerts_descriptionText.append(entity['alert']['descriptionText']['translation'][0]['text'])

        df_line['date'] = pd.Series(line_service_alerts_date)
        df_line['time'] = pd.Series(line_service_alerts_time)
        df_line['agencyId'] = pd.Series(line_service_alerts_agencyId)
        df_line['routeId'] = pd.Series(line_service_alerts_routeId)
        df_line['headerText'] = pd.Series(line_service_alerts_headerText)
        df_line['descriptionText'] = pd.Series(line_service_alerts_descriptionText)

        df_line.drop_duplicates(subset=['time', 'agencyId', 'routeId', 'headerText', 'descriptionText'], inplace=True)

        try:
            for entity in df_line.itertuples():
                data = LineAlert(
                    date=entity.date,
                    time=entity.time,
                    agency_id=entity.agencyId,
                    route_id=entity.routeId,
                    header_text=entity.headerText,
                    description_text=entity.descriptionText
                )
                session.add(data)
        except Exception as err:
            print(err)
        session.commit()

        # Remove all duplication rows and reset the id start with 1
        query_delete = '''
                DELETE FROM public.line_alert l1
                        WHERE EXISTS (
                            SELECT *
                            FROM public.line_alert l2
                            WHERE l1.date = l2.date
                                AND l1.route_id = l2.route_id
                                AND l1.header_text = l2.header_text
                                AND l1.description_text = l2.description_text
                                AND l1.time < l2.time);
        '''
        session.execute(text(query_delete))
        query_reset = '''
                  UPDATE public.line_alert SET id= (SELECT MAX(id) FROM public.line_alert) + nextval('public.line_alert_id_seq');
                  ALTER SEQUENCE public.line_alert_id_seq RESTART;
                  UPDATE public.line_alert SET id= nextval('public.line_alert_id_seq');
        '''
        session.execute(text(query_reset))

        count = session.query(LineAlert.id).count()
        logger.info('%s - line_alert - Adding %s rows', model, len(df_line))
        logger.info('%s - line_alert - Total %s rows in database', model, count)

        # hdr = False if os.path.isfile(dir_name + 'line_service_alerts_' + file_date + '.csv') else True
        # df_line.to_csv(dir_name + 'line_service_alerts_' + file_date + '.csv', mode='a', header=hdr, index=False)

    if len(trip_based_alerts) > 0:
        trip_based_alerts_date = []
        trip_based_alerts_time = []
        trip_based_alerts_agencyId = []
        trip_based_alerts_tripId = []
        trip_based_alerts_headerText = []
        trip_based_alerts_descriptionText = []

        for entity in trip_based_alerts:
            for sub_entity in entity['alert']['informedEntity']:
                trip_based_alerts_agencyId.append(sub_entity['agencyId'])
                trip_based_alerts_date.append(today)
                trip_based_alerts_time.append(current_time)
                trip_based_alerts_tripId.append(sub_entity['trip']['tripId'])
                trip_based_alerts_headerText.append(entity['alert']['headerText']['translation'][0]['text'])
                trip_based_alerts_descriptionText.append(entity['alert']['descriptionText']['translation'][0]['text'])

        df_trip['agencyId'] = pd.Series(trip_based_alerts_agencyId)
        df_trip['date'] = pd.Series(trip_based_alerts_date)
        df_trip['time'] = pd.Series(trip_based_alerts_time)
        df_trip['tripId'] = pd.Series(trip_based_alerts_tripId)
        df_trip['headerText'] = pd.Series(trip_based_alerts_headerText)
        df_trip['descriptionText'] = pd.Series(trip_based_alerts_descriptionText)

        df_trip.drop_duplicates(subset=['time', 'agencyId', 'tripId', 'headerText', 'descriptionText'], inplace=True)

        count = session.query(TripAlert.id).count()
        logger.info('%s - trip_alert - Adding %s rows', model, len(df_trip))
        logger.info('%s - trip_alert - Total %s rows in database', model, count)

        try:
            for entity in df_trip.itertuples():
                data = TripAlert(
                    date=entity.date,
                    time=entity.time,
                    agency_id=entity.agencyId,
                    trip_id=entity.tripId,
                    header_text=entity.headerText,
                    description_text=entity.descriptionText
                )
                session.add(data)
        except Exception as err:
            print(err)
        session.commit()

        # Remove all duplication rows and reset the id start with 1
        query_delete = '''
                DELETE FROM public.trip_alert t1
                        WHERE EXISTS (
                            SELECT *
                            FROM public.trip_alert t2
                            WHERE t1.date = t2.date
                                AND t1.trip_id = t2.trip_id
                                AND t1.header_text = t2.header_text
                                AND t1.description_text = t2.description_text
                                AND t1.time < t2.time);
        '''
        session.execute(text(query_delete))
        query_reset = '''
                  UPDATE public.trip_alert SET id= (SELECT MAX(id) FROM public.trip_alert) + nextval('public.trip_alert_id_seq');
                  ALTER SEQUENCE public.trip_alert_id_seq RESTART;
                  UPDATE public.trip_alert SET id= nextval('public.trip_alert_id_seq');
        '''
        session.execute(text(query_reset))

        # hdr = False if os.path.isfile(dir_name + 'trip_based_alerts_' + file_date + '.csv') else True
        # df_trip.to_csv(dir_name + 'trip_based_alerts_' + file_date + '.csv', mode='a', header=hdr, index=False)

    session.commit()

    print('finish alter data processing.')
