def read_input(filename):
    """Read numbers and target from text file"""
    with open(filename, 'r') as file:
        # First line contains the collection of numbers
        numbers = list(map(int, file.readline().strip().split()))
        # Second line contains the target value
        target = int(file.readline().strip())
    return numbers, target

def binary_search(collection, target):
    """Binary search implementation"""
    if not collection:
        return -1
        
    arr = sorted(collection)
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) >> 1
        current = arr[mid]
        
        if current == target:
            return mid
        if current < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def main():
    try:
        # Read input from file
        numbers, target = read_input('input.txt')
        result = binary_search(numbers, target)
        
        # Print results
        print(f"Collection: {numbers}")
        print(f"Target: {target}")
        print(f"Result: {result}")
        
    except FileNotFoundError:
        print("Error: input.txt file not found")
    except ValueError:
        print("Error: Invalid input format in file")

if __name__ == "__main__":
    main()
