from QuequeClass import Queue
import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)


    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('A')
        self.assertFalse(self.queue.is_empty())


    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')
        self.assertTrue(self.queue.is_full())


if __name__ == '__main__':
    unittest.main()

