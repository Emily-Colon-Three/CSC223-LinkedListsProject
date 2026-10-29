import unittest
from unittest import TestCase

from singly_linked_list import SinglyLinkedList
from node import Node

# Creates a default, empty SinglyLinkedList object, then checks that properties are correct.
class EmptyList(unittest.TestCase):
    def test_empty_list(self):
        self.list = SinglyLinkedList()

        self.assertIsNone(self.list._head)
        self.assertIsNone(self.list._tail)
        self.assertEqual(self.list._count, 0)

# Creates two lists, one empty, and one containing two nodes already. Uses append() and
# prepend() upon both lists, then tests that correct instructions were executed.
class AddingNodes(unittest.TestCase):
    def setUp(self):
        self.empty = SinglyLinkedList()

        self.twonode = SinglyLinkedList()
        self.twonode.append(1)
        self.twonode.append(5)

    def test_append(self):
        self.empty.append(1) # 1 becomes the only node, and thus the tail as well as head.

        self.assertEqual(self.empty._head.data, 1)
        self.assertEqual(self.empty._tail, self.empty._head)
        self.assertEqual(self.empty._count, 1)

        self.twonode.append(11) # twonode should become 1, 5, 11

        self.assertEqual(self.twonode._head.data, 1)
        self.assertEqual(self.twonode._tail.data, 11)
        self.assertEqual(self.twonode._count, 3)

    def test_prepend(self):
        self.empty.prepend(1) # Puts 1 as the only node.

        self.assertEqual(self.empty._head.data, 1)
        self.assertEqual(self.empty._tail, self.empty._head)
        self.assertEqual(self.empty._count, 1)

        self.twonode.prepend(0) # twonode should become 0, 1, 5

        self.assertEqual(self.twonode._head.data, 0)
        self.assertEqual(self.twonode._tail.data, 5)
        self.assertEqual(self.twonode._count, 3)

# A series of tests which ensure full functionality of insert_after() method. Tests both
# successful and unsuccessful insertions, in cases where list is empty or does not contain
# existing value. Also tests tail logic, for when the first node of existing value is last.
class Insertion(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.append(1)
        self.list1.append(2)
        self.list1.append(4)

        self.list2 = SinglyLinkedList()

    def test_successful_insertion(self):
        self.list1.insert_after(2, 3) # Inserts a node of 3 after 2, new order: 1, 2, 3, 4

        self.assertEqual(self.list1._head.data, 1)
        self.assertEqual(self.list1._tail.data, 4)
        self.assertEqual(self.list1._count, 4)
        # Tests that new node added in proper order, after the intended existing node.
        self.assertEqual(self.list1._head.next.next.data, 3)

    def test_insertion_after_tail(self):
        self.list1.insert_after(4, 8) # Inserts 8 after 4, new order is 1, 2, 4, 8

        self.assertEqual(self.list1._head.data, 1)
        self.assertEqual(self.list1._tail.data, 8)
        self.assertEqual(self.list1._count, 4)

    def test_failed_insertion(self):
        with self.assertRaises(ValueError):
            self.list2.insert_after(0, 1) # Tries to insert node into empty list; no specified value exists in it.

        with self.assertRaises(ValueError):
            # List made not to be empty before testing again, to test error handling outside empty lists.
            self.list2.append(5)
            self.list2.append(10)
            self.list2.insert_after(1, 2)