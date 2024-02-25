
from src.BreastCancerClassification_with_MLflow.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from logger_file.logging import logger


class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

    
    def train_test_splitting(self):

        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False, header = True)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False, header = True)

        train_X = train.drop(columns = 'y', axis = 1)

        train_Y = train[['y']]

        std = StandardScaler()

        train_X = std.fit_transform(train_X)

        train_X = pd.DataFrame(train_X)

        le = LabelEncoder()

        train_Y = le.fit_transform(train_Y)

        train_Y = pd.DataFrame(train_Y)

        transformed_train = pd.concat([train_X, train_Y], axis = 1)

        transformed_train.to_csv(os.path.join(self.config.root_dir, 'transformed_train.csv'), index= False, header = True)

        test_X = test.drop(columns = 'y', axis = 1)

        test_Y = test[['y']]

        test_X = std.transform(test_X)

        test_X = pd.DataFrame(test_X)

        test_Y = le.transform(test_Y)

        test_Y = pd.DataFrame(test_Y)

        transformed_test = pd.concat([test_X, test_Y], axis = 1)

        transformed_test.to_csv(os.path.join(self.config.root_dir, 'transformed_test.csv'), index = False, header= True)


        logger.info('completed splitting the data into training and testing...!')
        logger.info(transformed_train.shape)
        logger.info(transformed_test.shape)


        print(transformed_train.shape)
        print(transformed_test.shape)

