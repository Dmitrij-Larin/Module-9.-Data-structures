import unittest

from Module_9_1.Stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.next_node, node_1)
        self.assertEqual(node_2.next_node.data, 5)


class TestStack(unittest.TestCase):
    stack = Stack(2)

    def test_01_init(self):
        self.assertEqual(self.stack.stack_size, 2)
        self.assertEqual(self.stack.top, None)

    def test_02_push(self):
        self.stack.push('bottom_data')
        self.stack.push('top_data')
        self.assertEqual(self.stack.top.data, 'top_data')
        self.assertEqual(self.stack.top.next_node.data, 'bottom_data')
        self.assertEqual(self.stack.push('overflow_data'), "Стэк переполнен")
        self.assertEqual(self.stack.size_stack(), 2)

    def test_03_pop(self):
        self.assertEqual(self.stack.pop(), 'top_data')
        self.assertEqual(self.stack.pop(), 'bottom_data')
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.pop(), 'Стэк пуст')

    def test_04_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push('bottom_data')
        self.assertEqual(self.stack.is_empty(), False)

    def test_05_is_full(self):
        self.assertEqual(self.stack.is_full(), False)
        self.stack.push('top_data')
        self.assertEqual(self.stack.is_full(), True)

    def test_06_clear_stack(self):
        self.stack.pop()
        self.assertEqual(self.stack.clear_stack(), None)

    def test_07_get_data(self):
        self.stack.push(2)
        self.stack.push('top_data')
        self.assertEqual(self.stack.get_data(0), 'top_data')
        self.assertEqual(self.stack.get_data(1), 2)
        self.assertEqual(self.stack.get_data(2), 'Out of range')

    def test_08_size_stack(self):
        self.assertEqual(self.stack.size_stack(), 2)

    def test_09_counter_int(self):
        self.assertEqual(self.stack.counter_int(), 1)
