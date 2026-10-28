"""The Node class is a simple unit of data, which acts as the building block of a
SinglyLinkedList. Every Node object contains data, and a reference to the next node. The
reference will be set to None upon  initialization, able to be changed later."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next