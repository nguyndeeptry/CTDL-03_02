a = [1, 2, 3]
n = len(a)
cmp_count = 0
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0:
        cmp_count += 1
        if a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        else:
            break
    a[j + 1] = key
print(a)
print("So lan so sanh:", cmp_count)
