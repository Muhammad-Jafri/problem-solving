from data_structures.linked_list.node import Node
from data_structures.linked_list.base import LinkedListBase
from typing import Optional


class LinkedList(LinkedListBase):
    def __init__(self):
        super().__init__()

    def insert_at_head(self, value: int):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        traversal_ptr = self.head

        while traversal_ptr.next:
            traversal_ptr = traversal_ptr.next

        traversal_ptr.next = new_node

    def count_elements(self):
        count = 0
        traversal_ptr = self.head
        while traversal_ptr:
            count += 1
            traversal_ptr = traversal_ptr.next

        return count

    def delete_at_head(self):
        if not self.head:
            raise IndexError("deleting from an empty list")

        deleted_node = self.head
        self.head = self.head.next
        return deleted_node

    def delete_at_tail(self):
        if self.head is None:
            raise IndexError("deleting from an empty list")
        traversal_ptr = self.head

        if traversal_ptr.next is None:
            self.head = None
            return self.head

        while traversal_ptr.next.next is not None:
            traversal_ptr = traversal_ptr.next

        deleted_node = traversal_ptr.next
        traversal_ptr.next = None
        return deleted_node
    
    

    def __str__(self):
        """Return a human-readable string representation."""
        if not self.head:
            return "[]"
        
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        
        return "[" + " -> ".join(values) + "]"

