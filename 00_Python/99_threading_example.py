import threading
import time
import random

def send_notification(user, delay):
    print(f"Начинало отправки уведомления: {user}")
    time.sleep(delay)
    print(f"Уведомление пользователю {user} отправлено! Задержка: {delay} секун")

def main():
    # Список пользователей и задержек отправки
    users_with_delays = [
        ("Alice", 2),
        ("Bob", 3),
        ("Charlie", 1),
        ("Diana", 5),
    ]

    threads = []

    # Создание и запуск потоков
    for user, delay in users_with_delays:
        thread = threading.Thread(target=send_notification, args=(user, delay))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

