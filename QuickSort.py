import time
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_helper(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_helper(arr, low, pivot_index - 1)
        quicksort_helper(arr, pivot_index + 1, high)

def quick_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    quicksort_helper(arr, 0, n-1)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Compare with sorted array
    if arr == sorted(arr.copy()):
        print(f"Sorting took {execution_time:.6f} seconds")
    else:
        print("Sort failed!")
    
    return arr

if __name__ == "__main__":
    # Create an array of 10,000 random numbers between 1 and 100,000
    arr = [random.randint(1, 100000) for _ in range(10000)]
    quick_sort(arr)