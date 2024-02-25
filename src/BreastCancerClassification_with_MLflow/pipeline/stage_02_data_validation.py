from src.BreastCancerClassification_with_MLflow.config.configuration import ConfigurationManager
from src.BreastCancerClassification_with_MLflow.components.data_validation import DataValidation
from Exception_file.exception import CustomException
import sys





STAGE_NAME = 'Data_Validation_Stage'


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_columns()
        except Exception as e:
            raise CustomException(e, sys)