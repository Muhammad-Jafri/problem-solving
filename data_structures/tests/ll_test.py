from data_structures.linked_list.linked_list import LinkedList
import unittest
from data_structures.linked_list.node import Node


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up a fresh LinkedList before each test."""
        self.linked_list = LinkedList()

    def test_empty_list(self):
        """Test that a new list is empty."""
        self.assertIsNone(self.linked_list.head)
        self.assertEqual(self.linked_list.count_elements(), 0)

    def test_insert_at_head(self):
        """Test inserting elements at the head of the list."""
        # Insert first element
        self.linked_list.insert_at_head(5)
        self.assertEqual(self.linked_list.head.value, 5)
        self.assertEqual(self.linked_list.count_elements(), 1)

        # Insert second element at head
        self.linked_list.insert_at_head(10)
        self.assertEqual(self.linked_list.head.value, 10)
        self.assertEqual(self.linked_list.head.next.value, 5)
        self.assertEqual(self.linked_list.count_elements(), 2)

    def test_insert_at_tail(self):
        """Test inserting elements at the tail of the list."""
        # Insert into empty list
        self.linked_list.insert_at_tail(5)
        self.assertEqual(self.linked_list.head.value, 5)
        self.assertEqual(self.linked_list.count_elements(), 1)

        # Insert at tail of non-empty list
        self.linked_list.insert_at_tail(10)
        self.assertEqual(self.linked_list.head.value, 5)
        self.assertEqual(self.linked_list.head.next.value, 10)
        self.assertEqual(self.linked_list.count_elements(), 2)

    def test_delete_at_head(self):
        """Test deleting elements from the head of the list."""
        # Try deleting from empty list
        with self.assertRaises(IndexError):
            self.linked_list.delete_at_head()

        # Add elements and delete
        self.linked_list.insert_at_head(5)
        self.linked_list.insert_at_head(10)

        deleted_node = self.linked_list.delete_at_head()
        self.assertEqual(
            deleted_node.value if deleted_node else None, 10
        )  # Assuming delete returns deleted node
        self.assertEqual(self.linked_list.head.value, 5)
        self.assertEqual(self.linked_list.count_elements(), 1)

        # Delete last element
        deleted_node = self.linked_list.delete_at_head()

        self.assertIsNone(self.linked_list.head)
        self.assertEqual(self.linked_list.count_elements(), 0)

    def test_delete_at_tail(self):
        """Test deleting elements from the tail of the list."""
        # Try deleting from empty list
        with self.assertRaises(IndexError):
            self.linked_list.delete_at_tail()

        # Delete from single element list
        self.linked_list.insert_at_head(5)
        deleted_node = self.linked_list.delete_at_tail()
        self.assertIsNone(self.linked_list.head)

        # Delete from multi-element list
        self.linked_list.insert_at_head(5)
        self.linked_list.insert_at_head(10)
        self.linked_list.insert_at_head(15)

        deleted_node = self.linked_list.delete_at_tail()
        self.assertEqual(deleted_node.value if deleted_node else None, 5)
        self.assertEqual(self.linked_list.count_elements(), 2)
        self.assertEqual(self.linked_list.head.value, 15)
        self.assertEqual(self.linked_list.head.next.value, 10)
        self.assertIsNone(self.linked_list.head.next.next)

    def test_count_elements(self):
        """Test counting elements in the list."""
        self.assertEqual(self.linked_list.count_elements(), 0)

        self.linked_list.insert_at_head(5)
        self.assertEqual(self.linked_list.count_elements(), 1)

        self.linked_list.insert_at_head(10)
        self.assertEqual(self.linked_list.count_elements(), 2)

        self.linked_list.delete_at_head()
        self.assertEqual(self.linked_list.count_elements(), 1)

        self.linked_list.delete_at_tail()
        self.assertEqual(self.linked_list.count_elements(), 0)


if __name__ == "__main__":
    unittest.main()
