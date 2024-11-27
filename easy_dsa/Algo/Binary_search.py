def binary_search(collection, target):
    # Convert input to list if it's a tuple or set
    if isinstance(collection, (tuple, set)):
        arr = sorted(list(collection))
    elif isinstance(collection, list):
        arr = sorted(collection)
    else:
        raise TypeError("Input must be a list, tuple, or set")

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
if __name__ == "__main__":
    # List example
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List search:", binary_search(sorted_list, 7))

    # Tuple example
    number_tuple = (5, 2, 8, 1, 9, 3, 7)
    print("Tuple search:", binary_search(number_tuple, 8))

    # Set example
    number_set = {4, 2, 7, 1, 9, 5}
    print("Set search:", binary_search(number_set, 4))

    # Unsorted list example
    unsorted_list = [9, 3, 5, 1, 7, 2, 8]
    print("Unsorted list search:", binary_search(unsorted_list, 5))
