class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f'TreeNode({self.value})'


class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def traverse(self, node, level=0):
        print(' ' * level * 2 + str(node.value))
        for child in node.children:
            self.traverse(child, level + 1)

    def add(self, parent_value, child_value):
        parent_node = self.find(self.root, parent_value)
        if parent_node:
            parent_node.add_child(TreeNode(child_value))
        else:
            print(f'Parent node with value {parent_value} not found.')

    def find(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found_node = self.find(child, value)
            if found_node:
                return found_node
        return None


# Example usage
if __name__ == "__main__":
    tree = Tree("Root")
    tree.add("Root", "Child 1")
    tree.add("Root", "Child 2")
    tree.add("Child 1", "Child 1.1")
    tree.add("Child 1", "Child 1.2")
    tree.add("Child 2", "Child 2.1")

    print("Tree Structure:")
    tree.traverse(tree.root)
