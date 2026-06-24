def insertion_stats(a):
    b = a[:]
    n = len(b)
    cmps = shifts = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0:
            cmps += 1
            if b[j] > key:
                b[j + 1] = b[j]
                j -= 1
                shifts += 1
            else:
                break
        b[j + 1] = key
    return cmps, shifts

def selection_stats(a):
    b = a[:]
    n = len(b)
    cmps = swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            cmps += 1
            if b[j] < b[min_idx]:
                min_idx = j
        if min_idx != i:
            b[i], b[min_idx] = b[min_idx], b[i]
            swaps += 1
    return cmps, swaps

def bubble_stats(a):
    b = a[:]
    n = len(b)
    cmps = swaps = 0
    for i in range(n):
        for j in range(n - 1 - i):
            cmps += 1
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                swaps += 1
    return cmps, swaps

a = [5, 3, 8, 1, 9, 2, 7, 4, 6]
ic, ish = insertion_stats(a)
sc, ssw = selection_stats(a)
bc, bsw = bubble_stats(a)

print(f"{'Thuat toan':<20} {'So sanh':>10} {'Swap/Shift':>12}")
print(f"{'Insertion sort':<20} {ic:>10} {ish:>12}")
print(f"{'Selection sort':<20} {sc:>10} {ssw:>12}")
print(f"{'Bubble sort':<20} {bc:>10} {bsw:>12}")
