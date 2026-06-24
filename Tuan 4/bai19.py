a = [5, 1, 4, 2, 8, 0, 3]
n = len(a)
left = 0
right = n - 1
cmp_count = 0
while left < right:
    min_idx = left
    max_idx = left
    for k in range(left, right + 1):
        cmp_count += 2
        if a[k] < a[min_idx]:
            min_idx = k
        if a[k] > a[max_idx]:
            max_idx = k
    a[left], a[min_idx] = a[min_idx], a[left]
    if max_idx == left:
        max_idx = min_idx
    a[right], a[max_idx] = a[max_idx], a[right]
    left += 1
    right -= 1
print(a)
print("So so sanh:", cmp_count)
