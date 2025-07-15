import socket
import threading

HOST = '127.0.0.1'  # Использовать все адреса: виден и снаружи, и изнутри
PORT = 50435  # Порт для прослушивания (непривилегированные порты > 1023)

running = True  # Флаг работы сервера
clients = []  # Список активных соединений


def handle_connection(sock, addr):
    """ Обрабатывает подключение клиента в отдельном потоке """
    global running
    with sock:
        print(f"Подключение: {addr}")
        clients.append(sock)

        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    break
            except ConnectionError:
                print(f"Клиент {addr} отключился с ошибкой!")
                break

            message = data.decode("utf-8").strip()
            print(f"Получено от {addr}: {message}")

            if message == "shutdown":
                print("Сервер выключается...")
                running = False
                sock.sendall("Server shutting down".encode())
                sock.shutdown(socket.SHUT_WR)
                break

            elif message == "disconnect":
                sock.sendall("disconnected".encode())
                sock.shutdown(socket.SHUT_WR)
                print(f"Клиент {addr} отключен!")
                break

            # Отправляем клиенту обработанный ответ
            response = message.upper().encode()
            try:
                sock.sendall(response)
            except ConnectionError:
                print(f"Ошибка отправки данных клиенту {addr}")
                break

        print(f"Отключение клиента {addr}")
        clients.remove(sock)


def server_loop():
    """ Запускает серверный цикл и принимает подключения """
    global running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen()
        print("Сервер запущен. Ожидание подключений...")

        while running:
            try:
                sock, addr = serv_sock.accept()
                print("Новое подключение:", addr)
                client_thread = threading.Thread(target=handle_connection, args=(sock, addr), daemon=True)
                client_thread.start()
            except OSError:
                break  # Сервер закрыт

    print("Сервер корректно завершил работу.")


if __name__ == '__main__':
    server_thread = threading.Thread(target=server_loop, daemon=True)
    server_thread.start()

    # Ожидаем завершения работы сервера
    while running:
        try:
            command = input()
            if command == "shutdown":
                print("Завершаем сервер...")
                running = False
                break
        except KeyboardInterrupt:
            print("\nПринудительное завершение сервера...")
            running = False
            break
