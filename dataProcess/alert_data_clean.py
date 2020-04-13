import os
import pandas as pd
from datetime import date, datetime

file_date = date.today().strftime("%Y%m%d")


def alert_data_processing(df):
    print('alter data processing.')

    today = date.today().strftime("%Y%m%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    data = df
    os.chdir(os.path.dirname(__file__))
    dir_name = os.getcwd() + '/alert/'

    entities = data['entity']
    line_service_alerts = []
    station_facilities_alerts = []
    trip_based_alerts = []

    for line_service_alert in entities:
        alerts = line_service_alert['alert']['informedEntity']
        keep_running = True
        for alert in alerts:
            if 'routeId' in alert and keep_running == True:
                line_service_alerts.append(line_service_alert)
                keep_running = False
            else:
                break

    for station_facilities_alert in entities:
        alerts = station_facilities_alert['alert']['informedEntity']
        keep_running = True
        for alert in alerts:
            if 'stopId' in alert and keep_running == True:
                station_facilities_alerts.append(station_facilities_alert)
                keep_running = False

    for trip_based_alert in entities:
        alerts = trip_based_alert['alert']['informedEntity']
        keep_running = True
        for alert in alerts:
            if 'trip' in alert and keep_running == True:
                trip_based_alerts.append(trip_based_alert)
                keep_running = False

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

        df_station = pd.DataFrame(
            columns=['date', 'time', 'agencyId', 'stopId', 'cause', 'effect', 'headerText', 'descriptionText'])

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

        hdr = False if os.path.isfile(dir_name + 'station_facilities_alerts_' + file_date + '.csv') else True
        df_station.to_csv(dir_name + 'station_facilities_alerts_' + file_date + '.csv', mode='a', header=hdr,
                          index=False)

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

        df_line = pd.DataFrame(columns=['date', 'time', 'agencyId', 'routeId',
                                        'headerText', 'descriptionText'])

        df_line['date'] = pd.Series(line_service_alerts_date)
        df_line['time'] = pd.Series(line_service_alerts_time)
        df_line['agencyId'] = pd.Series(line_service_alerts_agencyId)
        df_line['routeId'] = pd.Series(line_service_alerts_routeId)
        df_line['headerText'] = pd.Series(line_service_alerts_headerText)
        df_line['descriptionText'] = pd.Series(line_service_alerts_descriptionText)

        df_line.drop_duplicates(subset=['time', 'agencyId', 'routeId', 'headerText', 'descriptionText'], inplace=True)

        hdr = False if os.path.isfile(dir_name + 'line_service_alerts_' + file_date + '.csv') else True
        df_line.to_csv(dir_name + 'line_service_alerts_' + file_date + '.csv', mode='a', header=hdr, index=False)

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

        df_trip = pd.DataFrame(columns=['date', 'time', 'agencyId', 'tripId', 'headerText', 'descriptionText'])

        df_trip['agencyId'] = pd.Series(trip_based_alerts_agencyId)
        df_trip['date'] = pd.Series(trip_based_alerts_date)
        df_trip['time'] = pd.Series(trip_based_alerts_time)
        df_trip['tripId'] = pd.Series(trip_based_alerts_tripId)
        df_trip['headerText'] = pd.Series(trip_based_alerts_headerText)
        df_trip['descriptionText'] = pd.Series(trip_based_alerts_descriptionText)

        df_trip.drop_duplicates(subset=['time', 'agencyId', 'tripId', 'headerText', 'descriptionText'], inplace=True)

        hdr = False if os.path.isfile(dir_name + 'trip_based_alerts_' + file_date + '.csv') else True
        df_trip.to_csv(dir_name + 'trip_based_alerts_' + file_date + '.csv', mode='a', header=hdr, index=False)

    print('finish alter data processing.')
