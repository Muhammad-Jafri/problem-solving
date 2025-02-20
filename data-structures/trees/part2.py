# Assignment 2-Part 2
# AVL Trees


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1


class AVLTree(object):
    def insert(self, root, key):
        return "Null"

    def l_rotate(self, z):
        return "Null"

    def r_rotate(self, z):
        return "Null"

    def get_height(self, root):
        return "Null"

    def get_bal(self, root):
        return "Null"

    # You are requied return the the value of the root in a list after
    # If Root is not Found then you are required to return None
    def delete_node(self, root, node_to_be_deleted):
        return "Null"

    def update_node(self, root, new_value_of_node, old_value_of_node):
        return "Null"

    def delete_all_nodes_at_given_height(self, root, level):
        return "Null"


# Testing Area ---

# You can create a class tree object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
# Create an object here to test the functions.

if __name__ == "__main__":
    pass
