class FenwickTree:
    def __init__(self, input_data):
        """
        Initialize FenwickTree with either size or input array
        """
        if isinstance(input_data, int):
            self.size = input_data
            self.tree = [0] * (input_data + 1)
        elif isinstance(input_data, (list, tuple)):
            self.size = len(input_data)
            self.tree = [0] * (self.size + 1)
            # Build tree from input array
            for i, val in enumerate(input_data):
                self.update(i + 1, val)
        else:
            raise TypeError("Input must be either an integer or a list/tuple")

    def update(self, index, delta):
        """Update the tree with the given delta at the specified index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        """Returns the sum of the range [1, index]."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_query(self, left, right):
        """Returns the sum of the range [left, right]."""
        return self.query(right) - self.query(left - 1)


# Example usage
if __name__ == "__main__":
    # Using list as input
    arr = [1, 2, 3, 4, 5]
    fenwick_tree1 = FenwickTree(arr)
    print("Sum of first 3 elements:", fenwick_tree1.query(3))  # Output: 6
    print("Sum of elements from index 2 to 4:", fenwick_tree1.range_query(2, 4))  # Output: 9

    # Using size as input
    fenwick_tree2 = FenwickTree(5)
    for i, val in enumerate([1, 2, 3, 4, 5]):
        fenwick_tree2.update(i + 1, val)
    print("Sum of first 3 elements:", fenwick_tree2.query(3))  # Output: 6
    print("Sum of elements from index 2 to 4:", fenwick_tree2.range_query(2, 4))  # Output: 9
