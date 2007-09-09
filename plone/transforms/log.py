import logging

logger = logging.getLogger('plone.transforms')

# generic log method
def log(severity, message):
    logger.log(severity, message)

# debog log method
def log_debug(message):
    logger.log(logging.DEBUG, message)
