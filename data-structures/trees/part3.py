# Assignment 2-Part 3
# Implemetation

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None


def visiting_floors(root):
    pass


def changing_room_numbers(root):
    # Step one -> Think of a way to know that you are on the odd level
    # Step two -> Think what you have to store inorder to make the mirror image of odd levels of the tree
    # Hint For Step two -> Odd level Nodes are the Children of the Even level nodes
    pass


if __name__ == "__main__":
    """ Construct the following tree
				  1
			   /     \
			 /         \
		   2             3
		 /   \         /   \
		4     5       6     7
	  /  \    / \    / \    / \
	 8    9  10 11 12  13  14 15
	"""

    root = Node(1)
    root.l = Node(2)
    root.r = Node(3)
    root.l.l = Node(4)
    root.l.r = Node(5)
    root.r.l = Node(6)
    root.r.r = Node(7)
    root.l.l.l = Node(8)
    root.l.l.r = Node(9)
    root.l.r.l = Node(10)
    root.l.r.r = Node(11)
    root.r.l.l = Node(12)
    root.r.l.r = Node(13)
    root.r.r.l = Node(14)
    root.r.r.r = Node(15)
# Call your functions below this line of code
