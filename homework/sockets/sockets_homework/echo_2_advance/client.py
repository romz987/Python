import os
import socket

HOST = '127.0.0.1'
PORT = 50434

def client_menu():
    """ Меню клиента """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # Устанавливаем таймаут
        sock.settimeout(2)

        # Запускаем менюшку
        while True:
            os.system('clear')
            print("СОКЕТЫ")
            print()
            print("1. Отправить сообщение серверу")
            print("2. Показать список доступных комманд")
            print("3. Переподключиться к серверу")
            print()
            print("0. Выход")
            print("\n")
            choice = input("Выберите опцию: ")

            match choice:
                case "1":
                    os.system('clear')
                    try:                 
                        print("ОТПРАВИТЬ СООБЩЕНИЕ")
                        print()
                        message = str(input("Введите сообщение: "))
                        message_bytes_send = message.encode()
                        sock.sendall(message_bytes_send)
                        message_bytes_recieved = sock.recv(1024)
                        message_recivied = message_bytes_recieved.decode("utf-8")
                        if message_recivied == "disconnected" or message_recivied == "":
                            print()
                            print("Вы отключены от сервера")
                            print()
                        print(f"Ответ: {message_recivied}")

                    except Exception as e:
                        print(f"Ошибка: {str(e)}")
                    finally:
                        print()
                        input("Нажмите любую клавишу для продолжения...")    

                case "2":
                    os.system('clear')
                    try:                 
                        print("СПИСОК КОММАНД")
                        print()
                        print("disconnect - отключиться от сервера (клиент завершит свою работу)")
                        print("shutdown - завершить работу сервера удаленно")

                    except Exception as e:
                        print(f"Ошибка: {str(e)}")
                    finally:
                        print()
                        input("Нажмите любую клавишу для продолжения...") 

                case "3":
                    os.system('clear')
                    try:                 
                        print("ПЕРЕПОДКЛЮЧЕНИЕ К СЕРВЕРУ")
                        print()
                        client_menu()

                    except Exception as e:
                        print(f"Ошибка: {str(e)}")

                case "0":
                    os.system('clear')
                    exit()

                case _:
                    os.system('clear')
                    print("Вы нажали что-то не то...")
                    input("Нажмите любую клавишу для продолжения...")


if __name__ == "__main__":
    client_menu()
