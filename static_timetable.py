import glob
import requests
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import os


def timetable(api, model):

    dir_name = "/Users/frankie/Realtime/Data/timetable/"

    response_time = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/schedule/' + model,
                                 headers={'Authorization': api})

    f = ZipFile(BytesIO(response_time.content))
    f.extractall(path=dir_name)

    all_files = glob.glob(dir_name + "/*.txt")

    # convert txt files to csv files and delete all of them
    for file in all_files:
        df = pd.read_csv(file)
        filename = file.split(".")[0]
        df.to_csv(filename + '.csv', index=False)

        if file.endswith(".txt"):
            os.remove(os.path.join(dir_name, file))
