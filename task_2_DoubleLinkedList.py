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
    dll = DoubleLinkedList([1, 2, 3, 4, 5])

    dll.append(6)
    print(dll)

    dll.insert(3, 20)
    print(dll)

    dll_1 = DoubleLinkedNode([10, 100, 1000])
    dll_2 = DoubleLinkedNode([20, 200, 2000])
    dll_3 = DoubleLinkedNode([30, 300, 3000])

    dll_1.next = dll_2
    dll_2.next = dll_3
    dll_2.prev = dll_1
    dll_3.prev = dll_2

    print(repr(dll_1))
    print(repr(dll_2))
    print(repr(dll_3))
