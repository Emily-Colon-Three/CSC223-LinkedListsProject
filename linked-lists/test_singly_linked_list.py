import unittest
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