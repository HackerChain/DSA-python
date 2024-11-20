class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursively(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursively(current_node.right, key)

    def dfs_in_order(self, node):
        if node:
            self.dfs_in_order(node.left)
            print(node.val, end=' ')
            self.dfs_in_order(node.right)

    def dfs_pre_order(self, node):
        if node:
            print(node.val, end=' ')
            self.dfs_pre_order(node.left)
            self.dfs_pre_order(node.right)

    def dfs_post_order(self, node):
        if node:
            self.dfs_post_order(node.left)
            self.dfs_post_order(node.right)
            print(node.val, end=' ')

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    print("In-order DFS:")
    tree.dfs_in_order(tree.root)
    print("\nPre-order DFS:")
    tree.dfs_pre_order(tree.root)
    print("\nPost-order DFS:")
    tree.dfs_post_order(tree.root)
