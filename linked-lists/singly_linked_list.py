"""SinglyLinkedList is a class which acts as an implementation of a Singly Linked List
ADT, composed of nodes which point to the subsequent node within the list. It has three
key members holding it together, self._head and self._tail, which are references to the
first and last nodes respectively, and count, which is an integer tracking exactly how
many nodes are currently in the SinglyLinkedList."""
from node import Node

class SinglyLinkedList:
    def __init__(self): # On initialization, an empty linked list is created.
        self._head = None
        self._tail = None
        self._count = 0

