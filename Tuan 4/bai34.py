import bisect

a = [5, 2, 4, 6, 1, 3]
n = len(a)
cmp_normal = 0
cmp_binary = 0

b = a[:]
for i in range(1, n):
    key = b[i]
    j = i - 1
    while j >= 0 and b[j] > key:
        cmp_normal += 1
        b[j + 1] = b[j]
        j -= 1
    cmp_normal += 1 if j >= 0 else 0
    b[j + 1] = key

c = a[:]
for i in range(1, n):
    key = c[i]
    pos = bisect.bisect_left(c, key, 0, i)
    cmp_binary += int(i).bit_length()
    c[pos + 1:i + 1] = c[pos:i]
    c[pos] = key

print("Ket qua:", c)
print("So sanh thuong:", cmp_normal)
print("So sanh binary (uoc tinh):", cmp_binary)
