a = [3, 1, 4, 1, 5, 9, 2, 6]
n = len(a)
swap_count = 0
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]
        swap_count += 1
print(a)
print("So swap thuc su:", swap_count)
