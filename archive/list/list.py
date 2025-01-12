class Node:


    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node 



class LinkedList:


    def __init__(self):
        self.head = None 


    def insert_at_begging(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else: 
            new_node.next_node = self.head
            self.head = new_node


    def remove_node(self, index):
        if index == 0:
            result = self.head 
            self.head = self.head.next_node
            return result.data 

        counter = 0
        current_node = self.head
        while current_node and counter < (index - 1):
            current_node = current_node.next_node
            counter += 1 

        node_for_remove = current_node.next_node 
        current_node.next_node = node_for_remove.next_node
        data, node_for_remove.data = node_for_remove.data, None 

        return data


    def print_ll(self):
        current_node = self.head 
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

        return "Список показан!"


    def contains(self, value):
        current_node = self.head
        while current_node and current_node.data != value:
            current_node = current_node.next_node 
           
        if current_node is None:
            return "Данные не найдены"

        return current_node.data


    def replace_data(self, old_value, new_value):
        current_node = self.head 

        while current_node and current_node.data != old_value:
            current_node = current_node.next_node 

        if current_node is None:
            return "Данные не найдены"

        current_node.data = new_value 
        return "ok!"



lls = LinkedList()

lls.insert_at_begging('data_one')
lls.insert_at_begging('data_two')
lls.insert_at_begging('data_three')
lls.insert_at_begging('data_four')

# print(lls.contains('data_three'))

lls.print_ll()
lls.replace_data('data_two', 'hello!')
print()
lls.print_ll()



        



