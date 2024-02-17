
from box import ConfigBox
from logger_file.logging import logger
from Exception_file.exception import CustomException
from pathlib import Path
import yaml
import sys
import os
import json
from typing import Any
import joblib








def read_yaml(path_to_yaml : Path) ->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} has been loaded successfully...!')
            return ConfigBox(content)
        
    except Exception as e:
        raise CustomException(e , sys)
    

def create_directories(path_to_directories : list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)


        if verbose:
            logger.info(f'created directory at : {path}...!')



def save_json(path : Path, data : dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'json file saved at {path}...!')


def load_json(path : Path) ->ConfigBox:
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f'json file loaded successfully at {path}...!')

    return ConfigBox(content)


def save_bin(data : Any, path : Path):
    joblib.dump(value = data, filename=path)
    logger.info(f'binary file saved at : {path}')



def load_bin(path : Path) -> Any:
    data = joblib.load(path)
    logger.info(f'binary file loaded from {path}...!')
    return data


def get_size(path : Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'---{size_in_kb} KB-----!'