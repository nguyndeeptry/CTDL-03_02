def selection_swaps(a):
    b = a[:]
    n = len(b)
    count = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if b[j] < b[min_idx]:
                min_idx = j
        if min_idx != i:
            b[i], b[min_idx] = b[min_idx], b[i]
            count += 1
    return count

def bubble_swaps(a):
    b = a[:]
    n = len(b)
    count = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                count += 1
    return count

a = [4, 3, 1, 2]
print("Selection swaps:", selection_swaps(a))
print("Bubble swaps:", bubble_swaps(a))
