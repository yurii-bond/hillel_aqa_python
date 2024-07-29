import logging
import datetime


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d - %(name)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler(f'lecture_11/logging/example_code_{datetime.datetime.now()}.log')
                    ])

logger = logging.getLogger(__name__)

logger.info("INFO message")
logger.debug("DEBUG message")

logging.shutdown()
