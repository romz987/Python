# Реализация паттерна комманда
class Client:
    

    def __init__(self):
        pass


class Command:
    

    def __init__(self):
        pass


class Executer:
    

    def __init__(self):
        pass

        
    def show_text(self, sender_name: str, message_text: str):
        """ 
        Вывести текст с именем 
        отправителя на экран 
        """
        print(
            f"sender: {sender_name}\n"
            f"message: {message_text}"
        )




if __name__ == "__main__":
    pass
