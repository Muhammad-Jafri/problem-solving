from Task1_A import get_hashcode, div_compression
from LinkedList import LinkedList

class Chaining:
    def __init__(self, table_size):
        '''
        Arguments:
        table_size: Integer
        '''
        
        self.table_size = table_size
        self.hash_table = [LinkedList() for i in range(self.table_size)]

    def get_hash(self, value):
        '''
        Arguments:
        value: String
        
        Returns: 
        Compressed Hash Code: Integer
        
        Use functions from Task1_A.py here
        '''
        pass

    def insert_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns: Nothing
        '''
        pass

    def delete_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns: Nothing
        '''
        pass

    def lookup_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns:
        if value is found: the value (String)
        if value is not found: False
        '''
        pass
