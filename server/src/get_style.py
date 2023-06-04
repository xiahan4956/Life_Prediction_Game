import logging

logger = logging.getLogger(__name__)

def generate_style():
    logger.info("Choosing style")
    styles =  [ 'Cyber punk',"fantasy","Real","Historical"] 
    return styles
