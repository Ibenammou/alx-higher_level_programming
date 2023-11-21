#!/usr/bin/python3
"""Class Node defines a singly linked list"""


class Node:
    """Class Node that defines a node of a singly linked list by:
    """
    def __init__(self, data, next_node=None):
        """Defines the private attribute
        Attribute:
            Data: private instance attribute
            next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Defines the property data"""
        return self._data

    @data.setter
    def data(self, value):
        """Defines the property setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Defines the property next node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """setter to set the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Class defines a singly linked list"""

    def __init__(self):
        """Defines self"""
        self.head = None

    def sorted_insert(self, value):
        """Defines the sorted list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                current.next_node is not None
                and current.next_node.data < value
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Define str self"""
        res = []
        Current = self.head
        while Current is not None:
            res.append(str(Current.data))
            Current = Current.next_node
        return "\n".join(res)
