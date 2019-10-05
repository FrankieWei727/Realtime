import trip_update
import static_timetable
import alert

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

    api_key = 'apikey EXmt0Pl6OWxy2OZUo19fus2PYKsMd4F6G7W8'
    model = 'sydneytrains'

    # set_parser()

    option = input("Please select: 1.tripUpdate 2.timetable 3.alert 4.exit : \n")

    if option == "1":
        trip_update.trip_update(api_key, model)

    if option == "2":
        static_timetable.timetable(api_key, model)

    if option == "3":
        print('alert info update')
        alert.alert(api_key, model)

    if option == "4":
        print('Closing. . .')
        exit(0)






