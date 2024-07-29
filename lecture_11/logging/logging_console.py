import logging


logging.basicConfig(level=logging.NOTSET, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


logging.debug('This is message from DEBUG level')
logging.info('This is message from INFO level')
logging.warning('This is message from WARNING level')
logging.error('This is message from ERROR level')
logging.critical('This is message from CRITICAL level')
