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

    # This function adds an additional node to the SinglyLinkedList at the back, which
    # becomes the new tail. Also adds 1 to count, regardless of whether it handles a case
    # of an empty or non-empty list.
    def append(self, data):
        new = Node(data)
        if self._head is None: # In the case of an empty list
            self._head = new
            self._tail = new
        else:
            self._tail.next = new
            self._tail = new

        self._count += 1 # Updates count; the variable must remain accurate to node count.

    # This function adds a node to the beginning of the list, which becomes the new head.
    # It updates the count accordingly, and makes the new node point to the previous head.
    def prepend(self, data):
        new = Node(data)
        if self._head is None: # Empty list logic
            self._head = new
            self._tail = new
        else: # Sets the next node of the new node to the current head, then replaces head
            new.next = self._head
            self._head = new

        self._count += 1 # Similar to append, a new node is being added; count is 1 more.