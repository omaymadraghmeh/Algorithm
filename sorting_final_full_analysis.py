
import random
import time
import pandas as pd

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort with Random Pivot
def quick_sort_random_pivot(arr):
    a = arr.copy()
    stack = [(0, len(a) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = random.randint(low, high)
            a[pivot_index], a[high] = a[high], a[pivot_index]
            p = partition(a, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))
    return a

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Data generators
def generate_data(size, data_type='random'):
    if data_type == 'random':
        return [random.randint(0, 100000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reversed':
        return list(range(size, 0, -1))
    elif data_type == 'partial':
        data = list(range(size))
        for i in range(size // 2, size):
            data[i] = random.randint(0, 10000)
        return data

# Main experiment
def run_experiments():
    sizes = [100, 1000, 3000, 5000, 10000 , 500000]
    data_types = ['random', 'sorted', 'reversed', 'partial']
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort_random_pivot)
    ]
    trials = 5
    results = []

    for alg_name, func in algorithms:
        for dtype in data_types:
            for size in sizes:
                total_time = 0
                for _ in range(trials):
                    data = generate_data(size, dtype)
                    start = time.perf_counter()
                    func(data)
                    end = time.perf_counter()
                    total_time += (end - start)
                avg_time = total_time / trials
                results.append([alg_name, dtype, size, round(avg_time, 6)])

    df = pd.DataFrame(results, columns=["Algorithm", "Input Type", "Size", "Avg Time (sec)"])
    print(df.to_string(index=False))
    df.to_excel("final_all_sorts_results.xlsx", index=False)

if __name__ == "__main__":
    run_experiments()
