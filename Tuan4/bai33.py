a = [4, 3, 2, 1]
k = 1
n = len(a)
for i in range(1, k + 1):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
print(a)
