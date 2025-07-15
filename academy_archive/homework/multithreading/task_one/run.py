import threading
from functions import *

if __name__ == "__main__":
    # Определяем и запускаем первый поток
    thread1 = threading.Thread(target=list_random_gen, args=(q, 100))
    thread1.start()
    thread1.join()
    # Выводим результат выполнения первого потока
    my_list = q.get()
    print(f"Список случайных чисел: {my_list}")

    # Определяем и запускаем остальные потоки
    thread2 = threading.Thread(target=list_sum_numbers, args=(q, my_list))
    thread3 = threading.Thread(target=list_arithmetic_mean, args=(q, my_list))
    thread2.start()
    thread3.start()    
    thread2.join()
    thread3.join()
    # Выводим результат
    print(f"Сумма случайных чисел в списке: {q.get()}")
    print(f"Среднееарифметическое чисел в списке: {q.get()}")



