import math

def intro_sort(arr):
    max_depth = 2 * math.ceil(math.log2(len(arr)))
    introsort_rec(arr, 0, len(arr) - 1, max_depth)

def introsort_rec(arr, low, high, max_depth):
    n = high - low + 1
    if n <= 1:
        return
    elif max_depth == 0:
        heap_sort(arr, low, high)
    elif n <= 16:
        insertion_sort(arr, low, high)
    else:
        pivot = partition(arr, low, high)
        introsort_rec(arr, low, pivot, max_depth - 1)
        introsort_rec(arr, pivot + 1, high, max_depth - 1)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr, low, high):
    n = high - low + 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[low], arr[low + i] = arr[low + i], arr[low]
        heapify(arr, i, 0)

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
