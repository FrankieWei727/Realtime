import requests
import csv
from io import BytesIO
from zipfile import ZipFile
from pathlib import Path


def timetable():

    response_time = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/schedule/sydneytrains',
                            headers={'Authorization': 'apikey EXmt0Pl6OWxy2OZUo19fus2PYKsMd4F6G7W8'})


    f = ZipFile(BytesIO(response_time.content))
    f.extractall(path='Data/Timetable/')

    for in_path in Path('Data/Timetable/').glob('*.txt'):
        out_path = in_path.with_suffix('.csv')
        with in_path.open('r') as fin, out_path.open('w') as fout:
            reader = csv.DictReader(fin)
            writer = csv.DictWriter(fout, reader.fieldnames)
            writer.writeheader()
            writer.writerows(reader)


if __name__ == '__main__':
    timetable()
