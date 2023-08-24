"""
Contains everything related to logging in pge
"""
import logging


def setupLogging(LoggerName: str, level: int = 10, FileHandler: logging.FileHandler = None, ConsoleHandler: logging.StreamHandler = None) -> logging.Logger:
    """
    A simple function to setup a logger based on the name given
    :param LoggerName: A string which has the name of the logger to give to logging.getLogger()
    :param level: The lowest level to output from the logger (optional defaults to logging.DEBUG)
    :param FileHandler: If you want a custom FileHandler for your logger (optional defaults to the one defined in function)
    :param ConsoleHandler: If you want a custom StreamHandler for your logger (optional defaults to the one defined in the function)
    :return: logging.Logger
    """
    logger: logging.Logger = logging.getLogger(LoggerName)
    logFormatter = logging.Formatter(
        "%(levelname)s (%(asctime)s) - %(name)s: %(message)s (Line: %(lineno)d [%(filename)s])",
        "%m/%d %H:%M:%S"
    )

    if FileHandler is None:
        fileHandler = logging.FileHandler(
            "{0}/{1}.log".format("./logs", "console")
        )
    else:
        fileHandler = FileHandler
    fileHandler.setFormatter(logFormatter)
    
    if ConsoleHandler is None:
        consoleHandler = logging.StreamHandler()
    else:
        consoleHandler = ConsoleHandler
    consoleHandler.setFormatter(logFormatter)

    logger.level = level
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger


