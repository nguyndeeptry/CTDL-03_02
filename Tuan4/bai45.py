a = [8, 6, 7, 5, 3, 1, 4, 2]
n = len(a)
gaps = []
gap = n // 2
while gap > 0:
    gaps.append(gap)
    gap //= 2

shifts_total = 0
for gap in gaps:
    for i in range(gap, n):
        key = a[i]
        j = i
        while j >= gap and a[j - gap] > key:
            a[j] = a[j - gap]
            j -= gap
            shifts_total += 1
        a[j] = key

print(a)
print("Tong shifts Shell sort:", shifts_total)
