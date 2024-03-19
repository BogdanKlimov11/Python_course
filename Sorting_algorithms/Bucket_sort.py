def bucket_sort(array):
    n = len(array)
    max_value = max(array)
    min_value = min(array)
    bucket_size = 10

    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in array:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array
