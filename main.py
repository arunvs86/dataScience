from src.DataScience import logger
from src.DataScience.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} coompleted <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e