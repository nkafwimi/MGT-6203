import argparse
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import os
import pandas as pd

YEAR_LIST = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
DATA_SOURCE_PREFIX = './Data/source/'

def __run():
    if not os.path.exists(DATA_SOURCE_PREFIX):
        print("---- Creating source directory")
        os.mkdir(DATA_SOURCE_PREFIX, 0o777)

    for year in YEAR_LIST:
        url = f"https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-{year}.zip"
        tempzip = open(f"{DATA_SOURCE_PREFIX}{year}.csv", "wb")
        with urlopen(url) as remote_file:
            with BytesIO(remote_file.read()) as byte_file, ZipFile(byte_file) as zip_file:
                survey_file_name = [s for s in zip_file.namelist() if ".csv" in s][0]
                tempzip.write(zip_file.open(survey_file_name).read())
        print(f"Successfully downloaded data for the year {year}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--all', help="Download all survey data", action="store_true")
    args = parser.parse_args()

    if args.all:
        __run()
    else:
        raise Exception("No argument passed: Run the script with --all")
