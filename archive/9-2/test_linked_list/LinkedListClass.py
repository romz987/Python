class Node:
    """Класс, представляющий узел связного списка."""

    def __init__(self, data, next_node=None):
        """
        Инициализация узла.

        :param data: Данные, которые будет хранить узел.
        :param next_node: Ссылка на следующий узел (по умолчанию None).
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс, представляющий связный список."""

    def __init__(self):
        """Инициализация пустого связного списка."""
        self.head = None

    def insert_at_head(self, data):
        """
        Вставка узла с данными в начало списка.

        :param data: Данные, которые будет хранить новый узел.
        :return: Сообщение о добавлении узла.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        """
        Вставка узла с данными в конец списка.

        :param data: Данные, которые будет хранить новый узел.
        :return: Сообщение о добавлении узла.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        """
        Удаление узла по заданной позиции.

        :param rm_position: Позиция узла, который нужно удалить.
        :return: Сообщение о результате удаления.
        """
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        """
        Вставка узла с данными на заданную позицию.

        :param data: Данные, которые будет хранить новый узел.
        :param node_position: Позиция, на которую нужно вставить узел.
        :return: Сообщение о добавлении узла.
        """
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        """
        Вывод данных связного списка.

        :return: Сообщение о выводе данных.
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        """
        Поиск узла по данным.

        :param data: Данные, которые нужно найти.
        :return: Кортеж (найдено ли, узел).
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        """
        Изменение данных узла.

        :param node_data: Данные узла, который нужно изменить.
        :param change_data: Новые данные для узла.
        :return: Сообщение о результате изменения данных.
        """
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"
