import os
import zipfile
import gdown
from kidneyDiseaseClassifier import logger
from kidneyDiseaseClassifier.entity.config_entity import DataINgestionConfig
from kidneyDiseaseClassifier.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataINgestionConfig):
        self.config = config

    def download_file(self):

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_source_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading dataset from {dataset_url} to {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(f"Dataset downloaded successfully to {zip_download_dir}")

        except Exception as e:
            logger.error(f"Error occurred while downloading dataset: {str(e)}")


    def unzip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_source_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Dataset unzipped successfully to {unzip_path}")
        
        except Exception as e:
            raise e

    
