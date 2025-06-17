import os
import sys
import numpy as np
import pandas as pd

"""
Defining common constants variable for training pipeline
"""

TARGET_COLUMN:str = "Result"
PIPELINE_NAME: str = "network_security"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "phisingData.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
    DATA ingestion releted constant
"""
DATA_INGESTION_COLLECTION_NAME:str = "Network_Data"
DATA_INGESTION_DATABASE_NAME: str = "JATINAI"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2