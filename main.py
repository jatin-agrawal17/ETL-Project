from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.exception.exception import CustomException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from network_security.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("data initiation completed")
        print(dataingestionartifact)
        
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
    except Exception as e:
        raise CustomException(e,sys)