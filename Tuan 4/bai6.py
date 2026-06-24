a = [5, 3, 1, 4, 2]
n = len(a)
cmp_count = 0
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        cmp_count += 1
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
print(a)
print("So lan so sanh:", cmp_count)
print("Ly thuyet n*(n-1)/2 =", n * (n - 1) // 2)
