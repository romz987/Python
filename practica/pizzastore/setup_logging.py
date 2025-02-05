import logging 


def setup_logging():
    # Настройка логирования
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler('pizzeria.log')
    file_handler.setLevel(logging.DEBUG)  # Уровень логирования для файла

    # Создаем обработчик для вывода логов на консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Уровень логирования для консоли

    # Создаем форматтер и добавляем его к обработчикам
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
