import time
import random

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
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
    bubble_sort(arr)