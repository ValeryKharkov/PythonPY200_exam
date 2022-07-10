import unittest

from task_1_DoubleLinkedNode import DoubleLinkedNode


class TestCase(unittest.TestCase):  #  наследуюсь от unittest.TestCase
    def test_repr_double_linked_Node_without_next(self):
        node_value = 50
        node = DoubleLinkedNode(node_value)  # проверить метод __repr__ без следующего узла
        expected_value = f'DoubleLinkedNode({node_value}, None, None)'
        actual_value = repr(node)
        self.assertEqual(expected_value, actual_value, msg='Неверный repr')


#     def __repr__(self) -> str:
#         return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"
# # DoubleLinkedNode(1, DoubleLinkedNode(2, None, None), None)