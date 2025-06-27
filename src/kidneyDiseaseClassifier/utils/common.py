import os
from box.exceptions import BoxValueError
import yaml
from kidneyDiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml(str): path like input

    Raises: 
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    create list of multiple directories

    Args: 
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"Created file directory at: {path}")

    
@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size on KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save data in json format """

    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"Data saved in json format at: {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file and returns"""
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Json file: {path} loaded successfully")
            return ConfigBox(data)
        
    except Exception as e:
        raise e
    

@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    save data in binary format """
    with open(path, 'wb') as bin_file:
        joblib.dump(data, bin_file)
        logger.info(f"Data saved in binary format at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary file and returns"""
    try:
        with open(path, 'rb') as bin_file:
            data = joblib.load(bin_file)
            logger.info(f"Binary file: {path} loaded successfully")
            return data
        
    except Exception as e:
        raise e
    

@ensure_annotations
def decode_image(imgstring, fileName):
    """
    decode image from base64 string """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close
    logger.info(f"Image saved as: {fileName}")

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    """
    encode image into base64 string """
    with open(croppedImagePath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        logger.info(f"Image encoded into base64: {encoded_string}")
        return encoded_string