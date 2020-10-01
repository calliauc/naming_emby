import logging

def generate_logger():
    logger = logging.getLogger('Journal_exemple')
    logger.setLevel(logging.INFO)

    fl = logging.FileHandler('debug.log')
    fl.setLevel(logging.DEBUG)
    logger.addHandler(fl)

    cl = logging.StreamHandler()
    cl.setLevel(logging.DEBUG)
    logger.addHandler(cl)

    return logger