import os
import sys
import json

from dotenv import load_dotenv
import pymongo.mongo_client
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# python package that provides set of root certificates
# trusted certificate authority
import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from network_security.logging.logger import logging
from network_security.exception.exception import CustomException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def cv_to_json_converter(self, filepath):
        try:
            data = pd.read_csv(filepath)
            data.reset_index(drop=True , inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.collection = self.mongo_client[database][collection]
            self.collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise CustomException(e, sys)

        
        
if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "JATINAI"
    Collections ="Network_Data"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(filepath=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records , DATABASE , Collections)
    print(no_of_records)