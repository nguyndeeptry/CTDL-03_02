def count_comparisons(n):
    return n * (n - 1) // 2

for n in [3, 5, 10]:
    print(f"n={n}: so so sanh = {count_comparisons(n)}")

a = [1, 2, 3, 4, 5]
n = len(a)
cmp = 0
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        cmp += 1
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
print(f"Thuc te: {cmp}, Ly thuyet: {count_comparisons(n)}")
