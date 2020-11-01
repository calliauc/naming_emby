import logging

def generate_logger():
    logger = logging.getLogger('Journal_exemple')
    logger.setLevel(logging.DEBUG)

    fl = logging.FileHandler('debug.log')
    fl.setLevel(logging.DEBUG)
    fileFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fl.setFormatter(fileFormatter)
    logger.addHandler(fl)

    cl = logging.StreamHandler()
    cl.setLevel(logging.INFO)
    consoleFormatter = logging.Formatter('%(levelname)s - %(message)s')
    cl.setFormatter(consoleFormatter)
    logger.addHandler(cl)

    return logger