import os 
import yaml
from src.DataScience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path : Path) -> ConfigBox:
    """
    read yaml file and returns

    Args:
        path to yaml file -- str like input
    
    Raises:
        ValueError : if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type helps to access dictionary elements like 
        objects. For example, file= {"Key1": "Value1", "Key2": "Value2"}
        to access it, we use file["Key1"],
        with configBox we can use it as file.Key1
    """

    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    for path in path_to_directories:
        os.makedirs(path,exist_ok = True)
        if verbose:
            logger.info(f"Created directory at: {path} ")


@ensure_annotations
def save_json(path: Path, data: dict):

    with open(path,'w') as file:
        json.dump(data,file,indent=4)
    
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    
    with open(path) as file:
        content = json.load(file)

    logger.info(f"Json file loaded successfully from path: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_binary(data:Any , path:Path):

    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_binary(path:Path) -> Any:

    data = joblib.load(path)
    logger.info(f"Binary file saved at: {path}")
    return data