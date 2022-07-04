from typing import Optional
from node import Node


class DoubleLinkedNode(Node):
    def __init__(self, value, next_=None, prev_=None):
        super().__init__(value, next_)
        self.prev = prev_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"]):
        self._prev = prev_
    # Переопределяем магический метод __repr__ для модификации вывода результата
    def __repr__(self) -> str:
        next_repr: str = str(None) \
            if self.next is None \
            else f"DoubleLinkedNode({self.next.value}, {None}, {None})"
        prev_repr: str = str(None) \
            if self.prev is None \
            else f"DoubleLinkedNode({self.prev.value}, {None}, {None})"
        return f"DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})"

if __name__ == "__main__":
    """
    Тестирование класса DoubleLinkedNode
    """

    node_1 = DoubleLinkedNode(1)
    node_2 = DoubleLinkedNode(2)
    node_3 = DoubleLinkedNode(3)
    node_4 = DoubleLinkedNode(4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_2.prev = node_1
    node_3.prev = node_2
    node_4.prev = node_3

    print(repr(node_1))
    print(repr(node_2))
    print(repr(node_3))
    print(repr(node_4))

    print(str(node_1))
    print(str(node_2))
    print(str(node_3))
    print(str(node_4))


