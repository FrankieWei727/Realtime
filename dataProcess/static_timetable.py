import glob
import requests
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import os
from dataProcess import timetable_data_clean


def timetable(api, model):
    print('start getting timetable data.')
    os.chdir(os.path.dirname(__file__))
    path = os.getcwd() + '/timetable/'

    response_time = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/schedule/' + model,
                                 headers={'Authorization': api})

    f = ZipFile(BytesIO(response_time.content))
    f.extractall(path=path)

    all_files = glob.glob(path + "/*.txt")

    # convert txt files to csv files and delete all of them
    for file in all_files:
        df = pd.read_csv(file, low_memory=False)
        filename = file.split(".")[0]
        df.to_csv(filename + '.csv', index=False)

        if file.endswith(".txt"):
            os.remove(os.path.join(path, file))

    print('finish getting timetable data.')

    timetable_data_clean.timetable_data_processing()
