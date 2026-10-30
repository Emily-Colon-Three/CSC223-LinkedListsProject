"""SinglyLinkedList is a class which acts as an implementation of a Singly Linked List
ADT, composed of nodes which point to the subsequent node within the list. It has three
key members holding it together, self._head and self._tail, which are references to the
first and last nodes respectively, and count, which is an integer tracking exactly how
many nodes are currently in the SinglyLinkedList. It contains a series of methods which
manipulate or observe attributes of the list:
Firstly, append() and prepend() take data as the argument, then create a new node and add
it either to the back (append) or front (prepend) of the list, becoming the new tail or
head, respectively. They have logic for being used on an empty list, making the added node
become both head and tail. 1 is added to the count after either case.
Then, insert_after() takes a value to look for and a value to add as a new node, finding
the former value and inserting a node of the new value between it and the previous
subsequent node. It will raise ValueError if the list is empty or lacks the target. Count
is increased by one with successful insertion.
Then, remove() finds and removes a node from the list. It changes references so that the
node is no longer referenced in the SinglyLinkedList, whether it be head, tail, or interior.
It raises an error for empty lists and lists without the specified value.
Then, contains() returns True or False depending on whether a SinglyLinkedList object has
a node of the specified value. is_empty() method works similarly, simply returning True for
an empty list and False if there is any node at all present. len() is also made compatible
with SinglyLinkedList, returning _count as list length."""
from xml.etree.ElementInclude import include

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
        if self.is_empty(): # In the case of an empty list
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
        if self.is_empty():
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

    # Finds node with data given in parameters, then removed it from SinglyLinkedList.
    # Contains case handling for if the node is the head, the tail, or an interior node.
    # Additionally, can handle an error of the list being either empty or lacking target.
    def remove(self, data):
        if self.is_empty():
            raise ValueError("SinglyLinkedList is empty.")

        # Checks first if head has target data; removes head if so.
        if self._head.data == data:
            if self._head == self._tail: # Case in which node to be removed is only one.
                self._head = None
                self._tail = None
                self._count = 0

                return # method must terminate now that removal is complete
            else: # For when there is at least one node after head
                self._head = self._head.next
                self._count -= 1

                return # Head has been removed, no need for the rest of the instructions

        current = self._head

        # Checks for node after current; head already checked, and removal needs previous node.
        while current.next.data != data:
            if current.next == self._tail:
                raise ValueError("Node with that value does not exist in list.")

            current = current.next

        if current.next == self._tail: # If the node to be removed is tail
            current.next = None
            self._tail = current
            self._count -= 1
        else: # Node to be removed is an interior node
            current.next = current.next.next
            self._count -= 1

    # Method which returns True or False, telling whether SinglyLinkedList contains
    # a specified value in any of its nodes. No errors should be raised; the value is either
    # in the list, or it isn't.
    def contains(self, data) -> bool:
        if self.is_empty():
            return False # Empty lists do not contain any value at all

        # Quickly checks if the head contains target value. If yes, the value is found.
        if self._head.data == data:
            return True

        current = self._head

        while current.data != data:
            if current == self._tail: # If current isn't the target, and is tail, target isn't present.
                return False

            current = current.next

        if current.data == data: # Loop has ended, and current is validated as target.
            return True

    # Simple function, True if list is empty, False if it contains any nodes at all.
    def is_empty(self) -> bool:
        if self._head is None:
            return True
        else:
            return False

    # Dunder method that allows len() to return the length of SinglyLinkedList, count.
    def __len__(self):
        return self._count

    def __iter__(self):
        if self._head is None:
            raise StopIteration

        self.index = 0
        return self

    def __next__(self):
        if (self.index) < len(self):
            current = self._head
            for i in range(self.index):
                current = current.next

            self.index += 1
            return current
        else:
            raise StopIteration

    # Function to let SinglyLinkedList be convertible into string output.
    def __str__(self):
        if self._head is None:
            return "Head -> None"

        string = "Head -> "

        for node in self:
            string += f"{node.data} -> "
        string += "None"

        return string

    # Function which fills empty SinglyLinkedList with elements from a Python list.
    def build_list_forward(self, list):
        for i in list:
            self.append(list[i - 1])

    # Function which fills empty SinglyLinkedList with Python List in reverse order.
    def build_list_backward(self, list):
        for i in list:
            self.append(list[-i])

    def remove_all(self, data) -> int:
        if self.is_empty():
            return 0

        current = self._head

        for i in range(self._count):
            if current.next.data == data:
                current.next = current.next.next

            current = current.next

        if self._head.data == data:
            self._head = self._head.next
        