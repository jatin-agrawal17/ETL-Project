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

SCHEMA_FILE_PATH:str = os.path.join("data_schema" , "schema.yaml")


"""
    DATA ingestion releted constant
"""
DATA_INGESTION_COLLECTION_NAME:str = "Network_Data"
DATA_INGESTION_DATABASE_NAME: str = "JATINAI"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2

"""
    Data validation constant
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"

"""
    Data transormation constant
    
"""
## knn imputer
DATA_TRANSORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSORMATION_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANSFORMATION_TRANSORMED_OBJECT_DIR:str = "transformed object"
DATA_TRANSFORMATION_IMPUTER_PARAMS:dict = {
    "missing_values":np.nan,
    "n_neighbors":  3,
    "weights": "uniform"
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"
