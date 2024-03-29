
from logger_file.logging import logger
from src.BreastCancerClassification_with_MLflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.BreastCancerClassification_with_MLflow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.BreastCancerClassification_with_MLflow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Exception_file.exception import CustomException
import sys
from logger_file.logging import logger




STAGE_NAME = 'Data_Ingestion_Stage'



try:
    logger.info(f'----------------{STAGE_NAME} started------------------')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'------------------{STAGE_NAME} completed --------------------')
except Exception as e:
    raise CustomException(e, sys)




STAGE_NAME = 'Data_Validation_Stage'

try:
    logger.info(f'--------------------{STAGE_NAME} started---------------')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = 'Data_Transformation_Stage'

try:
    logger.info(f'-------------------{STAGE_NAME} started--------------------')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
except Exception as e:
    raise CustomException(e, sys)