import logging


logger = None

def logger_config():
    global logger

    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Удаляем все существующие обработчики
        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler('library.log')
        file_handler.setLevel(logging.DEBUG)

        # console_handler = logging.StreamHandler()
        # console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        # console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)

    return logger
