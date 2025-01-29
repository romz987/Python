# Реализация паттерна комманда
# Многопоточность! :)
# Это импровизированный менеджер уведомлений
# Создаете уведомления - для этого запускаете программу
# Указываете заголок уведомления, текст и время в секундах
# через которое необходимо вывести уведомление
# Объект Executer не реализован так как это избыточно в контексте задания
# Для Invoker реализован метод удаления уведомления из очереди 
import threading
import time


class NotificationClient:

    def __init__(self, invoker):
        self.query = None
        self.invoker = invoker
    
    def create_notification(self) -> None:
        """ Создаем уведомление """
        try:
            header = str(input("Введите заголовок уведомления: "))
            message = str(input("Введите текст уведомления: "))
            timing = int(input("Через сколько секунд вывести уведомление?: "))
        except Exception as e:
            print(f"error: {str(e)}")
            self.create_notification()
        else:
            self.query = NotificationCommand(header, message, timing)
            self.send_to_invoker()
            one_more = str(input("Создать еще одно уведомление? (y/n): "))
            if one_more == "y":
                self.create_notification()

    def send_to_invoker(self) -> None:
        """ Отправить запрос в очередь исполнения """
        self.invoker.add_to_queue(self.query)


class NotificationCommand:
    
    def __init__(self, header: str, message: str, timing: int):
        """ 
        Конструктор запроса 

        :param header: заголовок уведомления 
        :param message: текст уведомления
        :param timing: время задержки в секундах
        """
        self.__header = header
        self.__message = message 
        self.__timing = timing

    def get_data(self) -> dict:
        """ Получить данные запроса """
        return {
            "header": self.__header,
            "message": self.__message,
            "timing": self.__timing
        }

    def get_timing(self) -> int:
        """ Получить время задержки """
        return self.__timing

    def get_header(self) -> int:
        """ Получить время задержки """
        return str(self.__header)


class Invoker:

    def __init__(self):
        self.__queue = []

    def add_to_queue(self, command: NotificationCommand) -> None:
        """
        Добавить запрос в очередь выполнения

        :command: объект запроса
        """
        self.__queue.append(command)

    def show_queue(self):
        print(self.__queue)

    def execute_notifications(self):
        """ Выполнить уведомления из очереди """
        for command in sorted(self.__queue, key=lambda cmd: cmd.get_timing()):
            timing = command.get_timing()
            threading.Timer(timing, self.display_notification, args=(command,)).start()

    def display_notification(self, command: NotificationCommand):
        """ 
        Вывести уведомление на экран 

        :param command: объект уведомления
        """
        data = command.get_data()
        print(f"Уведомление: {data['header']} - {data['message']}")

    def delete_notification_from_queue(self, header: str) -> None:
        """ 
        Удалить уведомление из очереди

        :param header: заголовок уведомления которое нужно уведомить
        """
        for command in sorted(self.__queue):
                command_header = command.get_header()
                if header == command_header:
                    self.__queue.remove(command)
                    print(f"Уведомление с заголовком {header} было удалено!")




if __name__ == "__main__":
    invoker = Invoker()
    client = NotificationClient(invoker)

    client.create_notification()
    invoker.execute_notifications()
    invoker.delete_notification_from_queue("hello")
