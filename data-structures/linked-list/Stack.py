from Linkedlist import Linkedlist


class Stack(Linkedlist):
    def push(self, value: int):
        self.insert_at_head(value)

    def pop(self):
        return self.delete_head()


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.print_ll()

    popped = s.pop()
    print(popped)
    s.print_ll()
