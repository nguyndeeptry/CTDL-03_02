a = [5, 2, 4, 6, 1, 3]
b = a[:]
n = len(a)

cmp_rtl = 0
for i in range(1, n):
    key = b[i]
    j = i - 1
    while j >= 0 and b[j] > key:
        cmp_rtl += 1
        b[j + 1] = b[j]
        j -= 1
    cmp_rtl += 1 if j >= 0 else 0
    b[j + 1] = key

c = a[:]
cmp_ltr = 0
for i in range(1, n):
    key = c[i]
    pos = 0
    while pos < i and c[pos] <= key:
        cmp_ltr += 1
        pos += 1
    c[pos + 1:i + 1] = c[pos:i]
    c[pos] = key

print("Phai sang trai - so sanh:", cmp_rtl)
print("Trai sang phai - so sanh:", cmp_ltr)
