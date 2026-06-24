import random

k = 3
n = 10000
a = list(range(1, n + 1))
for i in range(0, n - 1, k):
    end = min(i + k, n - 1)
    a[i], a[end] = a[end], a[i]

shifts = 0
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
        shifts += 1
    a[j + 1] = key

print(f"n={n}, k={k}, tong shifts={shifts}")
print(f"O(n*k) = {n * k}, thuc te gan voi du doan")
