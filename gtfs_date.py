from os import path
import os
import argparse
import logging.config
from database import tables
from sqlalchemy import create_engine
from dataProcess import static_timetable, trip_update, alert, vehicle_position
from sqlalchemy.orm import sessionmaker


def set_parser():
    parser = argparse.ArgumentParser(description='Search some files')

    parser.add_argument('-a', '--apiKey', default=api_key, help='the apiKey', action='store_true')

    parser.add_argument('-A', '--alert', default=alert.alert(api_key, model),
                        help='running the alert model to grab realtime timetable', action='store_true')

    args = parser.parse_args()

    if args.apiKey is None:
        print('Warning: the apiKey is missing.')
        exit(1)


def create_log():
    # create logger
    log_path = "log/logging.conf"
    log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
    logging.config.fileConfig(log_file_path)
    logs = logging.getLogger('gtfs_events')
    return logs


if __name__ == '__main__':

    api_key = open("apikey.txt", "r").read().split('.')[0]
    model = 'sydneytrains'

    logger = create_log()
    os.chdir(os.path.dirname(__file__))

    # Database config
    database_type = "postgresql"
    user = "frankie"
    password = "0203"
    hostname = "localhost:5432"
    database_name = "trains"

    engine = create_engine(f'{database_type}://{user}:{password}@{hostname}/{database_name}',
                           echo=True)

    # sessionmaker returns a class
    session = sessionmaker(bind=engine)

    s = session()

    # Check if it has the tables
    for table in tables.Base.metadata.tables.keys():
        try:
            if not engine.has_table(table):
                logger.info('Creating table %s', table)
                tables.Base.metadata.tables[table].create(engine)
            else:
                logger.info('The tables has been created --- %s', table)
        except Exception as err:
            logger.error('Database Error: %s', str(err))
            exit(1)

    if api_key is None:
        api_key = input("Please input your api_key: ")
        exit(0)

    logger.info("Start running project ---- model %s", model)

    try:
        keep_running = True
        while keep_running:
            option = input("Please select: \n1.tripUpdate \n2.timetable \n"
                           "3.alert \n4.vehicle position \n5.delete table \n6.exit \n:")

            if option == "1":
                logger.info(model + ": grab trip update info")
                trip_update.trip_update(api_key, model)

            if option == "2":
                logger.info("%s - grab static timetable info", model)
                static_timetable.timetable(api_key, model, s, tables.Timetable, logger)

            if option == "3":
                logger.info(model + ": grab alert info")
                alert.alert(api_key, model)

            if option == "4":
                logger.info(model + ": grab vehicle position info")
                vehicle_position.vehicle_position(api_key, model, s, tables.VehiclePosition, logger)

            if option == "5":
                for theClass in tables.AllClasses:
                    theClass.__table__.drop(engine)
                logger.info("Delete all the tables --- %s", tables.Base.metadata.tables.keys())

            if option == "6":
                print('Closing. . .')
                keep_running = False
                logger.info("Stop running project")
    finally:
        print('Closing session . . .')
        session.close_all()
        exit(0)
