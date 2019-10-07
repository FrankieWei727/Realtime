from os import path

import trip_update
import static_timetable
import alert
import vehicle_position
import logging
import logging.config
import argparse


def set_parser():
    parser = argparse.ArgumentParser(description='Search some files')

    parser.add_argument('-a', '--apiKey', default=api_key, help='the apiKey', action='store_true')

    parser.add_argument('-A', '--alert', default=alert.alert(api_key, model),
                        help='running the alert model to grab realtime timetable', action='store_true')

    args = parser.parse_args()

    if args.apiKey is None:
        print('Warning: the apiKey is missing.')
        exit(1)


if __name__ == '__main__':

    # create a log object
    # logging.basicConfig(filename='gtfs_events.log',
    #                     level=logging.DEBUG,
    #                     format='%(asctime)s - %(levelname)s - %(message)s',
    #                     datefmt='%m/%d/%Y %I:%M:%S %p')

    log_path = "log/logging.conf"
    log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
    logging.config.fileConfig(log_file_path)

    # create logger
    logger = logging.getLogger('gtfs_events')

    api_key = 'apikey EXmt0Pl6OWxy2OZUo19fus2PYKsMd4F6G7W8'
    model = 'sydneytrains'

    # set_parser()

    logger.info("Start running project")
    option = input("Please select: 1.tripUpdate 2.timetable 3.alert 4. vehicle position 5.exit : \n")

    if option == "1":
        logger.info(model + ": grab trip update info")
        trip_update.trip_update(api_key, model)

    if option == "2":
        logger.info(model + ": grab static timetable info")
        static_timetable.timetable(api_key, model)

    if option == "3":
        logger.info(model + ": grab alert info")
        alert.alert(api_key, model)

    if option == "4":
        logger.info(model + ": grab vehicle position info")
        vehicle_position.vehcile_position(api_key, model)

    if option == "5":
        print('Closing. . .')
        logger.info("Stop running project")
        exit(0)
