from collections.abc import MutableSequence  # абстрактный класс определяет общий интерфейс для набора подклассов.
from typing import Any, Optional
from Node_and_DoubleLinkedNode import DoubleLinkedNode
from LinkedList import LinkedList


class DoubleLinkedList(LinkedList):
    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == '__main__':
    list_ = [1, 2, 3]


    ll = DoubleLinkedList([1, 2, 3, 4, 5])

    print(ll)