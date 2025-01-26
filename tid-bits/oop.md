```
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

class Stack(LinkedList):
    def __init__(self):
        # Initialize the LinkedList attributes
        super().__init__()
        
        # Add Stack-specific attributes
        self.stack_top = None

# Example usage
stack = Stack()
print(stack.head)       # Output: None (inherited from LinkedList)
print(stack.size)       # Output: 0 (inherited from LinkedList)
print(stack.stack_top)  # Output: None (Stack-specific attribute)

```

```
class LinkedList:
    def __init__(self, default_value=None):
        self.head = default_value
        self.size = 0

class Stack(LinkedList):
    def __init__(self, default_value=None):
        super().__init__(default_value)  # Pass to LinkedList's __init__
        self.stack_top = None

```