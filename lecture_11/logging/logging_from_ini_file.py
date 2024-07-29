import logging
import logging.config


logging.config.fileConfig('lecture_11/logging/logging_config.ini')

logger = logging.getLogger('sampleLogger')
logg = logging.getLogger('root')


logger.debug("Message from DEBUG")
logg.debug("Message from DEBUG")
logger.info("Message from INFO")
logg.info("Message from INFO")
