import threading
from functions import *


if __name__ == "__main__":
    # Первый поток
    file_path = str(input("Как назовем файл со случайными числами?: "))
    thread1 = threading.Thread(target=create_file_random_num, args=(file_path, 15))
    thread1.start()
    thread1.join()

    # Второй и третий потоки
    thread2 = threading.Thread(target=check_file_for_primes, args=(file_path, ))
    thread3 = threading.Thread(target=calc_factorial_in_file, args=(file_path, ))
    thread2.start()
    thread3.start()
    thread2.join()
    thread3.join()


