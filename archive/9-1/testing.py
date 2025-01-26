import unittest
from Stack import Node, Stack


class TestStack(unittest.TestCase):


    def test_pop(self):
        stk = Stack()
        stk.push('hello!')
        stk.push('goodbuy!')
        stk.push(11)

        self.assertEqual(stk.pop(), 11)


    def test_is_full(self):
        stk = Stack()
        stk.push('hello!')
        stk.push('goodbuy!')
        stk.push(11)
        stk.push('value_one')
        stk.push('value_two')

        self.assertEqual(stk.is_full(), True)


    def test_get_data(self):
        stk = Stack()
        stk.push('hello!')
        stk.push('goodbuy!')
        stk.push(11)
        stk.push('value_one')
        stk.push('value_two')

        self.assertEqual(stk.get_data(4), 'hello!')


    def test_size_stack(self):
        stk = Stack()
        stk.push('hello!')
        stk.push('goodbuy!')
        stk.push(11)
        stk.push('value_one')
        stk.push('value_two')
    
        self.assertEqual(stk.size_stack(), 5)


    def test_counter_int(self):
        stk = Stack()
        stk.push('hello!')
        stk.push('goodbuy!')
        stk.push(11)
        stk.push('value_one')
        stk.push('value_two')
    
        self.assertEqual(stk.counter_int(), 1)



if __name__ == "__main__":
    unittest.main()
