
from kidneyDiseaseClassifier import logger
from kidneyDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from kidneyDiseaseClassifier.config.configuration import ConfigurationManager


STAGE_NAME = "Prepare base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

                                             
        
if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME} pipeline...")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} pipeline completed successfully.")
    
    except Exception as e:
        logger.error(f"Error occurred in {STAGE_NAME} pipeline: {str(e)}")
