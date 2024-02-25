from Exception_file.exception import CustomException
from logger_file.logging import logger
from pathlib import Path
from src.BreastCancerClassification_with_MLflow.config.configuration import ConfigurationManager
from src.BreastCancerClassification_with_MLflow.components.data_transformation import DataTransformation
import sys


STAGE_NAME = 'Data_Transformation_Stage'


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path('artifacts//data_validation//status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]


            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                print('your data is not valid, please check your data...!')


        except Exception as e:
            raise CustomException(e, sys)
