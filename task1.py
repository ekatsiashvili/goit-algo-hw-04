import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_sorting_algorithms(arr):
    # Вимірювання часу сортування -  merge_sort
    merge_sort_time = timeit.timeit(stmt='merge_sort(arr)',
                                    globals=globals(),
                                    number=10)
    
    # Вимірювання часу сортування -  insertion_sort
    insertion_sort_time = timeit.timeit(stmt='insertion_sort(arr)',
                                        globals=globals(),
                                        number=10)
    
    # Вимірювання часу сортування - Timsort
    timsort_time = timeit.timeit(stmt='sorted(arr)',
                                  globals=globals(),
                                  number=10)
    
    print(f"Час merge_sort: {merge_sort_time}")
    print(f"Час insertion_sort: {insertion_sort_time}")
    print(f"Час вбудованого Timsort: {timsort_time}")

# Випадковий масив для тестів
arr = [random.randint(0, 1000) for _ in range(1000)]

test_sorting_algorithms(arr)
