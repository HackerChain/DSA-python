from typing import List, Union

def merge_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts the input array using merge sort algorithm
    
    Args:
        arr: List of numbers (integers or floats) to be sorted
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Example with different types of numeric inputs
    int_array = [38, 27, 43, 3, 9, 82, 10]
    float_array = [3.14, 1.41, 2.71, 0.58, 1.73]
    mixed_array = [5, 2.5, 8, 1.1, 9, 3.14]

    print("Original integer array:", int_array)
    merge_sort(int_array)
    print("Sorted integer array:", int_array)

    print("\nOriginal float array:", float_array)
    merge_sort(float_array)
    print("Sorted float array:", float_array)

    print("\nOriginal mixed array:", mixed_array)
    merge_sort(mixed_array)
    print("Sorted mixed array:", mixed_array)

if __name__ == "__main__":
    main()
