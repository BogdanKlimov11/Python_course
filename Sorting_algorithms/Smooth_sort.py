def down_heap(a, first, last):
    largest = 2 * first + 1
    while largest <= last:
        if (largest < last) and (a[largest] < a[largest + 1]):
            largest += 1
        if a[largest] > a[first]:
            a[largest], a[first] = a[first], a[largest]
            first = largest
            largest = 2 * first + 1
        else:
            return

def heapify(a):
    n = len(a)
    i = n // 2 - 1
    while i >= 0:
        down_heap(a, i, n - 1)
        i -= 1

def smoothSort(a):
    heapify(a)
    i = len(a) - 1
    while i > 0:
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)
        i -= 1
