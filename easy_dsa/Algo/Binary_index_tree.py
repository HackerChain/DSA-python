class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

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
    arr = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(len(arr))

    # Build the tree
    for i in range(len(arr)):
        fenwick_tree.update(i + 1, arr[i])

    print("Sum of first 3 elements:", fenwick_tree.query(3))  # Output: 6
    print("Sum of elements from index 2 to 4:", fenwick_tree.range_query(2, 4))  # Output: 9
