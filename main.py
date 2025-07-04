from kidneyDiseaseClassifier import logger
from kidneyDiseaseClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from kidneyDiseaseClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion Pipeline"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.error(f"Error occurred in {STAGE_NAME}: {str(e)}")


STAGE_NAME = "Base Model Pipeline"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed successfully")

except Exception as e:
    logger.error(f"Error occurred in {STAGE_NAME}: {str(e)}")