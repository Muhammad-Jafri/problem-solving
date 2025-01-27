from Task1_A import get_hashcode, div_compression


class TableItem:
    def __init__(self, k, v, hw):
        '''
        Arguments:
        k: Integer (Hash key)
        v: String
        hw: Bool (for Task2 = None, for Task3 = True/False)
        '''

        self.key = k
        self.value = v
        self.honeyword = hw


class LinearProbing(TableItem):
    def __init__(self, table_size):
        '''
        Arguments:
        table_size: Integer
        
        Class members:
        self.count = Integer (Counts the number of items in the Hashtable)
        self.table_size = Integer (The size of the hashtable)
        self.hash_table = List (Hashtable)
        '''
        self.count = 0
        self.table_size = table_size
        self.hash_table = [None for i in range(self.table_size)]

    def get_hash(self, value):
        '''
        Arguments:
        value: String

        Returns: 
        Compressed Hash Code: Integer

        Use functions from Task1_A.py here
        Essentially the same funciton you implemented in Task1_B.py
        '''
        pass

    def resize_table(self):
        '''
        Function called in insert_word() function.

        Choose resize factor of your choice. 
        This will determine the time you take to pass the tests so try different values.

        Returns: Nothing
        '''
        pass

    def insert_word(self, value, honeyword_flag):
        '''
        Arguments:
        value: String
        honeyword_flag: Bool (for Task2 = None, for Task3 = True/False)

        Call resize() function here when loadfactor is high.
        Choose loadfactor of your choice. 
        This will determine the time you take to pass the tests so try different values.

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
        if value found: TableItem()
        if value not found: None
        '''
        pass
