def online_insertion_sort(stream):
    result = []
    for x in stream:
        i = len(result) - 1
        result.append(x)
        while i >= 0 and result[i] > result[i + 1]:
            result[i], result[i + 1] = result[i + 1], result[i]
            i -= 1
        print(result[:])
    return result

online_insertion_sort([5, 2, 8, 1])
