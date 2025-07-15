class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"



class MyLinkedList(LinkedList):


    def __init__(self):
        super().__init__()


    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"


    def insert_at_index(self, index: int, data: str):
        """ Вставляем ноду по индексу"""
        if index < 0 or index > self.len_ll():
            return "введенный индекс не соответствует количеству нод"

        new_node = Node(data)

        # Вставка в голову
        if index == 0:
            return self.insert_at_head(data)

        # Вставка в хвост
        if index == self.len_ll():
            return self.insert_at_tail(data)

        # Вставка в середину
        current_node = self.head
        index_counter = 0

        while index_counter < index - 1:
            current_node = current_node.next_node
            index_counter += 1

        new_node.next_node = current_node.next_node
        new_node.prev_node = current_node

        if current_node.next_node:
            current_node.next_node.prev_node = new_node

        current_node.next_node = new_node

        return f"Вставлена нода по индексу {index}"


    def remove_node_index(self, index: int):
        list_length = self.len_ll() - 1
        if index > list_length or index < 0:
            return "введенный индекс не соответствует количеству нод"
        
        index_counter = 0
        current_node = self.head

        # Если удаляем голову списка
        if index == 0:
            removed_node = current_node.data
            self.head = current_node.next_node
            if self.head:
                self.head.prev_node = None
            return f"Удаленная нода: {removed_node}"

        if index == self.len_ll() - 1:
            current_node = self.tail
            removed_node = current_node.data
            self.tail = current_node.prev_node 
            self.tail.next_node = None
            return f"Удаленная нода: {removed_node}"

        # Перемещаемся к нужному узлу
        while index_counter != index:
            current_node = current_node.next_node
            index_counter += 1

        removed_node = current_node.data

        # Обновляем ссылки
        if current_node.prev_node:
            current_node.prev_node.next_node = current_node.next_node
        if current_node.next_node:
            current_node.next_node.prev_node = current_node.prev_node

        return f"Удаленная нода: {removed_node}"


    def remove_node_data(self, data: str):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                # Если удаляем голову
                if current_node == self.head:
                    self.head = current_node.next_node
                    if self.head:
                        self.head.prev_node = None
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    if current_node.next_node:
                        current_node.next_node.prev_node = current_node.prev_node

                if current_node == self.tail:
                    self.tail = current_node.prev_node

                return f"Удаленная нода: {current_node.data}"

            current_node = current_node.next_node

        return f"{data} - ноды с такими данными не существует"


    def len_ll(self):
        current_node = self.head
        if current_node.next_node is None:
            return 1

        length_counter = 1
        while True:
            current_node = current_node.next_node
            length_counter += 1
            if current_node.next_node is None:
                return 4


    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False


    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False


    def contains_from(self, data, from_head=True):
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)




    

if __name__ == "__main__":
    mll = MyLinkedList() 

    mll.insert_at_head("hello!")
    mll.insert_at_head("how are you?")
    mll.insert_at_head("my name is MyName")
    mll.insert_at_head("goodbuy")

    # print('Читаем с начала:')
    # mll.print_ll_from_head()
    # print('Читаем с конца:')
    # mll.print_ll_from_tail()

    print()
    print(mll.remove_node_index(3))

    print('Читаем с начала:')
    mll.print_ll_from_head()
    print()
    print('Читаем с конца:')
    mll.print_ll_from_tail()

    print()
    print('Вставляем ноду по индексу:')
    mll.insert_at_index(2, "new data!!!")

    print('Читаем с начала:')
    mll.print_ll_from_head()
    print()
    print('Читаем с конца:')
    mll.print_ll_from_tail()


    print()
    print('Удаляем ноду с данными')
    mll.remove_node_data("how are you?")
    print('Читаем с начала:')
    mll.print_ll_from_head()
    print()
    print('Читаем с конца:')
    mll.print_ll_from_tail()

    print()
    print("Содержимое:")
    print(mll.contains_from("new data!!!", False))
    
    print('buy')


