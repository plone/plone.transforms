import logging

logger = logging.getLogger('plone.transforms')

# generic log method
def log(severity, message):
    logger.log(severity, message)
