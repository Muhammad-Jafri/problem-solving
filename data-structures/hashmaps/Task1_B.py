from Task1_A import get_hashcode, div_compression
from LinkedList import LinkedList


class Chaining:
    def __init__(self, table_size):
        """
        Arguments:
        table_size: Integer
        """

        self.table_size = table_size
        self.hash_table = [LinkedList() for i in range(self.table_size)]

    def get_hash(self, value):
        """
        Arguments:
        value: String

        Returns:
        Compressed Hash Code: Integer

        Use functions from Task1_A.py here
        """
        return div_compression(get_hashcode(value), self.table_size)

    def insert_word(self, value):
        """
        Arguments:
        value: String

        Returns: Nothing
        """

        idx = self.get_hash(value)
        self.hash_table[idx].insert_at_tail(value)
        return

    def delete_word(self, value):
        """
        Arguments:
        value: String

        Returns: Nothing
        """
        idx = self.get_hash(value)
        self.hash_table[idx].delete_any(value)
        return

    def lookup_word(self, value):
        """
        Arguments:
        value: String

        Returns:
        if value is found: the value (String)
        if value is not found: False
        """
        idx = self.get_hash(value)
        return self.hash_table[idx].get_element(value)
