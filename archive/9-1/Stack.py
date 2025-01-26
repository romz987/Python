class Node:
    """ 
    Узел в структуре данных. 
    Хранит данные и ссылку на следующий узел, 
    если он существует.
    """

    def __init__(self, data, next_node=None):
        """
        :param data: данные для хранения в узле
        :param next: cсылка на следующий узел
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """ 
    Стэк - структура данных
    Работает по принципу FILO:
    first in last out, что значит:
    первый зашел, последний вышел.
    """


    def __init__(self, stack_size=5, top=None):
        """ 
        :param stack_size: максимальный размер стека
        :param top: текущая вершина стека
        """
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды


    def push(self, data):
        """
        Добавляет новый узел на вершину стека,
        если данное действие не переполняет стек

        :param data: данные для хранения в узле
        """
        if self.size_stack() < self.stack_size: # сверяет текущий размер стека с максимальным
            new_node = Node(data) # создает новый узел
            new_node.next_node = self.top  # создает ссылку в новом узле на предыдущий узел
            self.top = new_node  # записывает новую ноду в пемеренную для хранения вершины стека 
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"


    def pop(self):
        """  
        Удаляет узел из стека и создает
        новую вершину стека из следующего узла 
        
        :return: данные из узла, который был вершиной
        """
        if self.top: # если есть узел-вершина
            remove_last = self.top # записываем его в переменную
            self.top = self.top.next_node # записываем узел, на который ссылается текущий узел вершина как вершину
            return remove_last.data # возвращаем данные 
        else:
            return "Стэк пуст"


    def is_empty(self):
        """ 
        Проверяет стек пуст или нет.
        Если вершина стека != None 
        возвращает False
        """
        if self.top:
            return False
        else:
            return True


    def is_full(self):
        """ 
        Проверяет стек на заполненность.
        Если добавление еще одного элемента
        приведет к переполнению стека
        возвращает True
        """
        if self.stack_size == self.size_stack():
            return True
        else:
            return False


    def clear_stack(self):
        """
        Удаляет все узлы из стека
        """
        while self.top:
            self.pop()


    def get_data(self, index):
        """
        Возвращает атрибут data из узла
        по его индексу

        :param index: индекс узла
        :return: атрибут data
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"


    def size_stack(self):
        """ 
        Проверяет текущий размер стека
        Начиная с узла, который записан как вершина стека
        Перемещается по ссылкам на другие узлы, до тех пор,
        пока существуют ссылки, увеличивая счетчик на 1 для
        каждого существующего узла.
        """
        counter = 0
        stack_item = self.top # Записать stack_item узел, который является вершиной стека
        while stack_item: # Пока stack_item не None
            counter += 1 # Прибавить единицу к счетчику
            stack_item = stack_item.next_node # Записать Записать stack_item узел, на который ссылается текущий узел
        return counter


    def counter_int(self):
        """ 
        Возращает количество узлов в стеке
        атрибут data которых является типом int
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
stack.pop()
print(stack.counter_int())
