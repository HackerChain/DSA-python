def binary_search(collection, target):
    """
    Optimized binary search that handles multiple collection types
    
    Args:
        collection: Input collection (list, tuple, or set)
        target: Value to find
        
    Returns:
        int: Index of target if found, -1 if not found
    """
    # Early validation
    if not collection:
        return -1
        
    # Use direct conversion to sorted list
    arr = sorted(collection)
    
    left, right = 0, len(arr) - 1
    
    # Binary search implementation
    while left <= right:
        mid = (left + right) >> 1  # Faster bitwise operation
        
        current = arr[mid]
        if current == target:
            return mid
        
        if current < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def main():
    # Test cases using different collection types
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        (5, 2, 8, 1, 9, 3, 7),
        {4, 2, 7, 1, 9, 5},
        [9, 3, 5, 1, 7, 2, 8]
    ]
    
    targets = [7, 8, 4, 5]
    
    for collection, target in zip(test_cases, targets):
        result = binary_search(collection, target)
        print(f"Searching {target} in {type(collection).__name__}: {result}")

if __name__ == "__main__":
    main()
