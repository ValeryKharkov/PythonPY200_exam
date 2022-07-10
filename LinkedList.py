from typing import Any, Iterable, Optional
from Node_and_DoubleLinkedNode import Node


class LinkedList:

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """ Удаление элемента из последовательности."""
        if not 0 < index <= self.len:  # проверка индекса
            raise IndexError

        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)  # алгоритм удаления
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self.len -= 1

    def __len__(self) -> int:
        """ Метод возвращает длину последовательности. """
        return self.len

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    # def nodes_iterator(self) -> Iterator[Node]:
    #     current_node = self.head
    #     for _ in range(self.len):
    #         yield current_node
    #         current_node = current_node.next

    # def clear(self):
    #     self.head = None
    #     self.tail = None
    #
    #     self.len = 0

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def insert(self, index: int, value: Any) -> None:
        """ Вставка значения по указанному индексу. """

        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.len += 1
        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self.len += 1


if __name__ == '__main__':
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)

    print("Проверка вхождения числа 2 в связный список")
    print(2 in linked_list)
    print("Проверка вхождения числа 5 в связный список")
    print(5 in linked_list)

    print(repr(linked_list))
    # print(linked_list)
    # del linked_list[1]
    # print(linked_list)
    # del linked_list[1]
    # print(linked_list)
    # del linked_list[0]
    # print(linked_list)
    #
    # ll = LinkedList(list_)
    # print(ll)
    # ll.append(100)
    # print(ll)
