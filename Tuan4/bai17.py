a = [7, 2, 5, 1, 9]
k = 3
n = len(a)
b = a[:]
for i in range(k):
    min_idx = i
    for j in range(i + 1, n):
        if b[j] < b[min_idx]:
            min_idx = j
    b[i], b[min_idx] = b[min_idx], b[i]
print("Phan tu nho thu", k, ":", b[k - 1])
