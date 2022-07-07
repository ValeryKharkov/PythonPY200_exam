import unittest

from task_1_DoubleLinkedNode import Node


class TestCase(unittest.TestCase):  #  наследуюсь от unittest.TestCase
    def test_repr_node_without_next(self):
        node_value = 5
        node = Node(node_value)  #  проверить метод __repr__ без следующего узла
        expected_value = f'Node({node_value}, None)'  # ожидание
        actual_value = repr(node)  # факт
        self.assertEqual(expected_value, actual_value, msg='Неверный repr')


