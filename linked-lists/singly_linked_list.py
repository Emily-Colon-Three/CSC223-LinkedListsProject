"""SinglyLinkedList is a class which acts as an implementation of a Singly Linked List
ADT, composed of nodes which point to the subsequent node within the list. It has three
key members holding it together, self._head and self._tail, which are references to the
first and last nodes respectively, and count, which is an integer tracking exactly how
many nodes are currently in the SinglyLinkedList. It contains a series of methods which
manipulate or observe attributes of the list:
Firstly, append() and prepend() take data as the argument, then create a new node and add
it either to the back (append) or front (prepend) of the list, becoming the new tail or
head, respectively. They have logic for being used on an empty list, making the added node
become both head and tail. 1 is added to the count after either case."""
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

    # This method will insert a new node with specified data after a node found in the list
    # with a matching specified existing value. If this target node is the tail, added node
    # becomes new tail. ValueError raised if target not found or if list is empty.
    def insert_after(self, existing_data, new_data):
        # List is first ensured to not be empty
        if self._head is None:
            raise ValueError("SinglyLinkedList is empty.")

        current = self._head # Creates cursor variable which starts at list head.
        new_node = Node(new_data)

        # This loop passes through the list node by node, and will terminate once current node has target data.
        while current.data != existing_data:
            if current == self._tail: # condition added to stop cursor from finding tail.next
                raise ValueError("Node with that value does not exist in list.")

            current = current.next

        if current == self._tail: # If cursor has landed on tail as only matching node
            self._tail.next = new_node
            self._tail = new_node
            self._count += 1
        else: # Default case, current is matching and not the tail.
            new_node.next = current.next
            current.next = new_node
            self._count += 1