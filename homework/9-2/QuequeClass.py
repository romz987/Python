class Queue:


    def __init__(self, size):
        """
        Инициализация очереди.

        :param size: Максимальный размер очереди.
        """
        self.size = size
        self.queue = []


    def is_empty(self):
        """
        Проверка, пуста ли очередь.

        :return: True, если очередь пуста, иначе False.
        """
        return len(self.queue) == 0


    def is_full(self):
        """
        Проверка, заполнена ли очередь.

        :return: True, если очередь заполнена, иначе False.
        """
        return len(self.queue) == self.size


    def enqueue(self, item):
        """
        Добавление элемента в очередь.

        :param item: Элемент, который нужно добавить в очередь.
        :raises OverflowError: Если очередь заполнена.
        """
        if self.is_full():
            raise OverflowError("Очередь заполнена")
        self.queue.append(item)


    def dequeue(self):
        """
        Удаление элемента из очереди.

        :return: Удаленный элемент.
        :raises IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue.pop(0)


    def show(self):
        """
        Отображение всех элементов очереди на экран.
        """
        print("Элементы очереди:", ", ".join(self.queue))



def main():
    size = int(input("Введите максимальный размер очереди: "))
    queue = Queue(size)

    while True:
        print("\nМеню:")
        print("1. Добавить элемент в очередь")
        print("2. Удалить элемент из очереди")
        print("3. Показать элементы очереди")
        print("4. Проверить, пуста ли очередь")
        print("5. Проверить, заполнена ли очередь")
        print("6. Выход")

        choice = input("Выберите операцию (1-6): ")

        if choice == '1':
            item = input("Введите элемент для добавления: ")
            try:
                queue.enqueue(item)
                print(f"Элемент '{item}' добавлен в очередь.")
            except OverflowError as e:
                print(e)

        elif choice == '2':
            try:
                removed_item = queue.dequeue()
                print(f"Элемент '{removed_item}' удален из очереди.")
            except IndexError as e:
                print(e)

        elif choice == '3':
            queue.show()

        elif choice == '4':
            if queue.is_empty():
                print("Очередь пуста.")
            else:
                print("Очередь не пуста.")

        elif choice == '5':
            if queue.is_full():
                print("Очередь заполнена.")
            else:
                print("Очередь не заполнена.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()

