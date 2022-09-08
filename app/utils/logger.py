import logging


def create_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create our handlers
    c_handler = logging.StreamHandler()

    c_handler.setLevel(logging.DEBUG)

    # Formatter
    c_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s'  # noqa E501
    )

    # Pass the formatter to the handlers
    c_handler.setFormatter(c_format)

    logger.addHandler(c_handler)

    return logger
