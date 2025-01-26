# Assignment 2-Part 1
# BST


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self):  # Initializing the BST. Root points to None.
        self.root = None

    def in_order(self, cur_node=None):

        res = []

        if cur_node is None:
            cur_node = self.root

        def wrapper(cur_node):

            if cur_node is None:
                return

            wrapper(cur_node.left)
            res.append(cur_node.value)
            wrapper(cur_node.right)

        wrapper(cur_node)
        return res

    def pre_order(self):
        res = []

        def wrapper(cur_node):

            if cur_node is None:
                return

            res.append(cur_node.value)
            wrapper(cur_node.left)
            wrapper(cur_node.right)

        wrapper(self.root)
        return res

    def post_order(self):

        res = []

        def wrapper(cur_node):

            if cur_node is None:
                return

            wrapper(cur_node.left)
            wrapper(cur_node.right)
            res.append(cur_node.value)

        wrapper(self.root)
        return res

    def insert(
        self, val
    ):  # TODO complete that shit on your own, its not that difficult
        def recursive_insert(node, val):
            # If tree is empty, create new node
            if node is None:
                return Node(val)

            # If value is less than current node's value, go left
            if val < node.value:
                node.left = recursive_insert(node.left, val)
            # If value is greater or equal, go right
            else:
                node.right = recursive_insert(node.right, val)

            # Return the (possibly modified) node
            return node

        # Update the root with the result of recursive insertion
        self.root = recursive_insert(self.root, val)

    def get_node(self, key):
        return None

    def find_node(self, key):

        return key in self.in_order()

    def get_children(self, key):  # TODO error handling,

        def get_key_node(node):

            if node.value == key:
                return node

            if key > node.value:
                get_key_node(node.right)

            if key < node.value:
                get_key_node(node.left)

        desired_node = get_key_node(self.root)
        return [
            desired_node.left.value if desired_node.left is not None else None,
            desired_node.right.value if desired_node.right is not None else None,
        ]

    def update_node(self, key, val):
        return None

    def get_height(
        self,
    ):  # Height of tree with just root node is 1, figure out why tf are we doing height - 1 TODO

        # Do a level order traversal and increment height by 1
        cur_node = self.root
        height = 0
        queue = []
        queue.append(cur_node)

        while queue:

            n = len(queue)
            for i in range(n):
                popped_node = queue.pop()
                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)
            height += 1

        return height - 1

    def get_path(self, key):
        return None

    def avg_diff(self):

        left_subtree_values = self.in_order(self.root.left)
        right_subtree_values = self.in_order(self.root.right)

        return sum(right_subtree_values) / len(right_subtree_values) - sum(
            left_subtree_values
        ) / len(left_subtree_values)

    def delete(self, key):
        return None

    def delete_leaf(self, key):
        return None

    def delete_leaves(self):
        return False

    def print_tree(self):
        """
        Print the binary search tree with visual representation of node connections.
        """

        def print_node(node, prefix="", is_left=True):
            if not node:
                return

            # Print right subtree first (top of the tree)
            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                print_node(node.right, new_prefix, False)

            # Print current node
            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

            # Print left subtree
            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                print_node(node.left, new_prefix, True)

        # Start printing from the root
        print_node(self.root, "", True)


# Testing Area ---


# You can create a class tree object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
def main():
    test_BST = Tree()
    test_BST.root = Node(6)
    test_BST.root.left = Node(5)
    test_BST.root.right = Node(7)
    test_BST.root.left.left = Node(4)
    test_BST.root.left.right = Node(5.5)
    test_BST.root.right.left = Node(6.5)
    test_BST.root.right.right = Node(8)
    test_BST.print_tree()
    print(test_BST.get_children(6))


# Comment out the line below before running your test files.
main()
