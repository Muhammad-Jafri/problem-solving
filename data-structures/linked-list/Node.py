class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
