from Node import Node


class Linkedlist:  # Doing some shitty error handling but yolo ;p

    def __init__(self):
        self.head = None
        self.n = 0

    def insert_at_head(self, value: int):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def delete_head(self):

        prev_head = self.head
        self.head = self.head.next
        self.n -= 1
        return prev_head

    def insert_at_index(self, index: int, value: int):

        if index == 1:
            self.insert_at_head(value)
        elif index == self.n:
            self.insert_at_tail(value)

        elif index < 1 or index > self.n:
            print("index is out of bounds")

        else:  # Traverse till index - 1, store it's next in temp, point current to new node and point new node next to temp

            new_node = Node(value)
            ptr = self.head
            for i in range(1, index):
                ptr = ptr.next

            existing_link = ptr.next
            ptr.next = new_node
            new_node.next = existing_link
            self.n += 1

    def insert_at_tail(self, value: int):

        ptr = self.head
        new_node = Node(value)
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
        self.n += 1

    def delete_tail(self):  # Stop traversal at second last element

        ptr = self.head

        while ptr.next.next:
            ptr = ptr.next

        ptr.next = None
        self.n -= 1

    def print_ll(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        print(f"total elements: {self.n}")


if __name__ == "__main__":

    ll = Linkedlist()
    ll.insert_at_index(1, 20)
    ll.insert_at_index(1, 30)
    ll.insert_at_index(1, 40)
    ll.insert_at_index(1, 50)
    ll.insert_at_index(2, 69)
    ll.print_ll()
