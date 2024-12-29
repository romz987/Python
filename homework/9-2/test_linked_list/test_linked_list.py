import unittest
from LinkedListClass import *
from unittest.mock import patch
import io


class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        """Тестирование инициализации узла."""
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next_node)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Создание экземпляра LinkedList для тестов."""
        self.linked_list = LinkedList()


    def test_insert_at_head(self):
        """Тестирование вставки узла в начало списка."""
        result = self.linked_list.insert_at_head(10)
        self.assertEqual(result, "Узел с данными 10 добавлен в начало списка")
        self.assertEqual(self.linked_list.head.data, 10)


    def test_insert_at_end(self):
        """Тестирование вставки узла в конец списка."""
        self.linked_list.insert_at_head(10)
        result = self.linked_list.insert_at_end(20)
        self.assertEqual(result, "Узел с данными 20 добавлен в конец списка")
        self.assertEqual(self.linked_list.head.next_node.data, 20)


    def test_remove_node_position(self):
        """Тестирование удаления узла по позиции."""
        self.linked_list.insert_at_head(10)
        self.linked_list.insert_at_head(20)
        result = self.linked_list.remove_node_position(1)
        self.assertEqual(result, "Удален узел с данными 20 позиции 1")
        self.assertEqual(self.linked_list.head.data, 10)


    def test_insert_at_position(self):
        """Тестирование вставки узла на заданную позицию."""
        self.linked_list.insert_at_head(10)
        result = self.linked_list.insert_at_position(20, 2)
        self.assertEqual(result, "Узел с данными 20 добавлен на позицию 2")
        self.assertEqual(self.linked_list.head.next_node.data, 20)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_ll(self, mock_stdout):
        """Тестирование вывода данных списка."""
        self.linked_list.insert_at_head(10)
        self.linked_list.insert_at_head(20)
        self.linked_list.insert_at_head(30)
        self.linked_list.print_ll()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output, ['30', '20', '10'])


    def test_get(self):
        """Тестирование поиска существующих данных."""
        self.linked_list.insert_at_head(10)
        found, node = self.linked_list.get(10)
        self.assertTrue(found)
        self.assertEqual(node.data, 10)


    def test_change_data(self):
        """Тестирование изменения данных существующего узла."""
        self.linked_list.insert_at_head(10)
        result = self.linked_list.change_data(10, 20)
        self.assertEqual(result, "Заменены данные в узле № 1")
        self.assertEqual(self.linked_list.head.data, 20)


if __name__ == '__main__':
    unittest.main()

