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

# Tests remove() method across different cases, both valid and invalid. Test removal of
# head node, tail node, and interior nodes, as well as error handling when removing from
# an empty list or a value not present in a list.
class RemovingNodes(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.append(1)
        self.list1.append(2)
        self.list1.append(4)
        self.list1.append(3)
        self.list1.append(4)
        self.list1.append(5)

        self.list2 = SinglyLinkedList() # Empty list

    def test_head_removal(self):
        self.list1.remove(1) # Removes head, making new head 2 (2, 4, 3, 4, 5)

        self.assertEqual(self.list1._head.data, 2)
        self.assertEqual(self.list1._tail.data, 5)
        self.assertEqual(self.list1._count, 5)

    def test_tail_removal(self):
        self.list1.remove(5) # Removes last node, new tail should be 4 (1, 2, 4, 3, 4)

        self.assertEqual(self.list1._head.data, 1)
        self.assertEqual(self.list1._tail.data, 4)
        self.assertEqual(self.list1._count, 5)

        self.assertIsNone(self.list1._tail.next) # Checks that tail has no next reference

    def test_interior_removal(self):
        self.list1.remove(4) # Should remove the first node of value 4 (1, 2, 3, 4, 5)

        self.assertEqual(self.list1._head.data, 1)
        self.assertEqual(self.list1._head.next.next.data, 3)
        self.assertEqual(self.list1._tail.data, 5)
        self.assertEqual(self.list1._count, 5)

    def test_invalid_removal(self):
        with self.assertRaises(ValueError): # Removing from empty list
            self.list2.remove(0)

        with self.assertRaises(ValueError): # Removing non-present value
            self.list1.remove(6)

# Tests contains() method, both in cases where value is present and ones where it is
# absent from a list. Checks that True or False is returned accordingly.
class ContainsInList(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.append(1)
        self.list1.append(2)
        self.list1.append(4)
        self.list1.append(8)

        self.list2 = SinglyLinkedList() # empty list

    def test_present(self):
        self.assertTrue(self.list1.contains(1))
        self.assertTrue(self.list1.contains(2))
        self.assertTrue(self.list1.contains(4))
        self.assertTrue(self.list1.contains(8))

    def test_absent(self):
        self.assertFalse(self.list1.contains(0))
        self.assertFalse(self.list2.contains(1)) # List 2 is empty, can't contain 1.

# Tests that is_empty() method returns True for empty lists, and False for non-empty.
class ListEmptiness(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList() # List with 1 node, head is also tail.
        self.list1.append(1)

        self.list2 = SinglyLinkedList() # List with 3 nodes, head and tail different.
        self.list2.append(2)
        self.list2.append(4)
        self.list2.append(6)

        self.list3 = SinglyLinkedList() # Empty list

    def test_false(self):
        self.assertFalse(self.list1.is_empty())
        self.assertFalse(self.list2.is_empty())

    def test_true(self):
        self.assertTrue(self.list3.is_empty())

# Tests that len() compatible with SinglyLinkedList, returning count of nodes.
class LengthOfList(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList() # Count: 1
        self.list1.append(1)

        self.list2 = SinglyLinkedList() # Count: 3
        self.list2.append(2)
        self.list2.append(4)
        self.list2.append(6)

        self.list3 = SinglyLinkedList() # Count: 0

    def test_length(self):
        self.assertEqual(len(self.list1), 1)
        self.assertEqual(len(self.list2), 3)
        self.assertEqual(len(self.list3), 0)

# Tests str() compatibility for SinglyLinkedList, which relies upon iter() and next().
# Passing test means both should be functioning properly.
class StringOutput(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.append(1)
        self.list1.append(2)
        self.list1.append(4)
        self.list1.append(8)

        self.list2 = SinglyLinkedList()

    def test_string(self):
        self.assertEqual(str(self.list1), "Head -> 1 -> 2 -> 4 -> 8 -> None")
        self.assertEqual(str(self.list2), "Head -> None")

# First, uses the list with build_list_forward() method, then build_list_backward().
# Tests that string output matches order of input list.
class BuildingList(unittest.TestCase):
    def setUp(self):
        self.input_list = [1, 2, 3, 4, 5]
        self.list = SinglyLinkedList()

    def test_forward_building(self):
        self.list.build_list_forward(self.input_list)
        self.assertEqual(str(self.list), "Head -> 1 -> 2 -> 3 -> 4 -> 5 -> None")

    def test_reverse_building(self):
        self.list.build_list_backward(self.input_list)
        self.assertEqual(str(self.list), "Head -> 5 -> 4 -> 3 -> 2 -> 1 -> None")