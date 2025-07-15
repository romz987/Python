import socket

HOST = '127.0.0.1'  
PORT = 50434

running = True

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen()
        print("Сервер запущен. Ожидаю подключения...")

        while running:
            sock, addr = serv_sock.accept()
            with sock:
                print(f"Подключение по {addr}")

                while True:
                    try:
                        data = sock.recv(1024)
                        if not data:
                            break
                    except ConnectionError:
                        print("Клиент внезапно отключился")
                        break

                    print(f"Received: {data}, from: {addr}")

                    if data.decode("utf-8") == "shutdown":
                        print("Выключение сервера...")
                        running = False  # Останавливаем сервер
                        sock.sendall("Server shutting down".encode())
                        sock.shutdown(socket.SHUT_WR)
                        break

                    elif data.decode("utf-8") == "disconnect":
                        sock.sendall("disconnected".encode())
                        sock.shutdown(socket.SHUT_WR)
                        print(f"Клиент {addr} отключен!")
                        break

                    sock.sendall(data.upper())

            if not running:
                break

