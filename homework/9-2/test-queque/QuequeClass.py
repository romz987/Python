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
        print("Элементы очереди:", " - ".join(self.queue))
