from kidneyDiseaseClassifier.components.data_ingestion import DataIngestion
from kidneyDiseaseClassifier.config.configuration import ConfigurationManager
from kidneyDiseaseClassifier import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_file()
        except Exception as e:
            raise e
        

