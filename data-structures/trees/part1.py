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

        ptr = Tree.get_key_node(self.root, key)
        return ptr if ptr is not None else False

    def find_node(self, key):

        return key in self.in_order()

    @staticmethod
    def get_key_node(node, key):

        if node is None:
            return

        if node.value == key:
            return node

        if key > node.value:
            return Tree.get_key_node(node.right, key)

        if key < node.value:
            return Tree.get_key_node(node.left, key)

    def get_children(self, key):  # TODO error handling,

        desired_node = Tree.get_key_node(self.root, key)
        return [desired_node.left, desired_node.right]

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

        def wrapper(node, cur_path=[]):

            if node.value == key:
                cur_path += [node.value]
                return cur_path

            if node.value < key:

                return wrapper(node.right, cur_path + [node.value])

            else:
                return wrapper(node.left, cur_path + [node.value])

        res = wrapper(self.root, [])
        print(res)
        return res

    def avg_diff(self):

        left_subtree_values = self.in_order(self.root.left)
        right_subtree_values = self.in_order(self.root.right)

        return sum(right_subtree_values) / len(right_subtree_values) - sum(
            left_subtree_values
        ) / len(left_subtree_values)

    def delete(self, key):
        return None

    def delete_leaf(self, key):
        # Find the node and its parent
        parent = None
        current = self.root

        while current and current.value != key:
            parent = current
            if key < current.value:
                current = current.left
            else:
                current = current.right

        # If node not found
        if not current:
            return

        # If node is not a leaf, can't delete
        if current.left or current.right:
            return

        # If parent exists, remove reference to the leaf
        if parent:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        else:
            # If deleting root and it's a leaf
            self.root = None

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
    test_BST.get_path(4)
    test_BST.print_tree()


# Comment out the line below before running your test files.
main()
