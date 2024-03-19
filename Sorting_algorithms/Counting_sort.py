def counting_sort(array):
    max_val = max(array)
    counts = [0] * (max_val + 1)

    for num in array:
        counts[num] += 1

    sorted_array = []
    for i in range(len(counts)):
        sorted_array.extend([i] * counts[i])

    return sorted_array
