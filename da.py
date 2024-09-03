import random
import time
import matplotlib.pyplot as plt

# Sorting algorithms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Benchmarking function
def benchmark_sorting_algorithms(array_sizes):
    insertion_sort_times = []
    selection_sort_times = []
    bubble_sort_times = []
    
    for size in array_sizes:
        arr = random.sample(range(1, size * 10), size)
        
        # Insertion Sort
        arr_copy = arr[:]
        start_time = time.time()
        insertion_sort(arr_copy)
        elapsed_time = time.time() - start_time
        insertion_sort_times.append(elapsed_time)
        print(f"Insertion Sort - Array Size: {size}, Time: {elapsed_time:.6f} seconds")
        
        # Selection Sort
        arr_copy = arr[:]
        start_time = time.time()
        selection_sort(arr_copy)
        elapsed_time = time.time() - start_time
        selection_sort_times.append(elapsed_time)
        print(f"Selection Sort - Array Size: {size}, Time: {elapsed_time:.6f} seconds")
        
        # Bubble Sort
        arr_copy = arr[:]
        start_time = time.time()
        bubble_sort(arr_copy)
        elapsed_time = time.time() - start_time
        bubble_sort_times.append(elapsed_time)
        print(f"Bubble Sort - Array Size: {size}, Time: {elapsed_time:.6f} seconds")
    
    return insertion_sort_times, selection_sort_times, bubble_sort_times

# Plotting function
def plot_benchmark_results(array_sizes, insertion_sort_times, selection_sort_times, bubble_sort_times):
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, insertion_sort_times, label="Insertion Sort", marker='o')
    plt.plot(array_sizes, selection_sort_times, label="Selection Sort", marker='o')
    plt.plot(array_sizes, bubble_sort_times, label="Bubble Sort", marker='o')
    
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmarking Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main program
if __name__ == "__main__":
    # User inputs
    input_sizes = input("Enter the input sizes separated by commas (e.g., 5,10,20,50): ")
    array_sizes = list(map(int, input_sizes.split(',')))
    
    # Benchmark sorting algorithms
    insertion_sort_times, selection_sort_times, bubble_sort_times = benchmark_sorting_algorithms(array_sizes)
    
    # Plot results
    plot_benchmark_results(array_sizes, insertion_sort_times, selection_sort_times, bubble_sort_times)
