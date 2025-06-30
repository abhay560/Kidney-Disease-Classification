from kidneyDiseaseClassifier import logger
from kidneyDiseaseClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Pipeline"
if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed successfully")

    except Exception as e:
        logger.error(f"Error occurred in {STAGE_NAME}: {str(e)}")
