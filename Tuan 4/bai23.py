def analyze(a):
    b = a[:]
    n = len(b)
    cmps = 0
    swaps = 0
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

sorted_a = [1, 2, 3, 4, 5]
random_a = [3, 1, 4, 5, 2]
reverse_a = [5, 4, 3, 2, 1]

for name, arr in [("Da sap xep", sorted_a), ("Ngau nhien", random_a), ("Nguoc", reverse_a)]:
    c, s = analyze(arr)
    print(f"{name}: so sanh={c}, swap={s}")
