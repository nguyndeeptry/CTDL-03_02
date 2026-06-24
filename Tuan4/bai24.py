import heapq

def partial_selection(a, k):
    b = a[:]
    n = len(b)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if b[j] < b[min_idx]:
                min_idx = j
        b[i], b[min_idx] = b[min_idx], b[i]
    return b[:k]

def heap_k_smallest(a, k):
    return sorted(heapq.nsmallest(k, a))

a = [5, 3, 8, 1, 9, 2, 7, 4, 6]
k = 3
print("Partial selection:", partial_selection(a, k))
print("Heap approach:", heap_k_smallest(a, k))
print("k nho -> dung partial selection O(n*k); k lon -> dung heap O(n + k log n)")
