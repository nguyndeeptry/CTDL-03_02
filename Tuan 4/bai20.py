import heapq

def heap_sort(a):
    h = a[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

a = [5, 2, 4, 6, 1, 3]
print("Selection sort: O(n^2) comparisons, O(n) swaps")
print("Heap sort: O(n log n) comparisons and swaps")
print("Heap sort result:", heap_sort(a))
