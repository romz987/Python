class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node



class StringQueQue:
    

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def enqueque(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node

        self.tail = new_node


    def dequeque(self):
        pass
