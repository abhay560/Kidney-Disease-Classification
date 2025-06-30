from kidneyDiseaseClassifier.entity.config_entity import DataINgestionConfig
from kidneyDiseaseClassifier.utils.common import create_directories, read_yaml
from kidneyDiseaseClassifier.constants import *


class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataINgestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataINgestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_source_file = config.local_source_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    
