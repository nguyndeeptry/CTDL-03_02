a = [3, 2, 1]
n = len(a)
shift_count = 0
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
        shift_count += 1
    a[j + 1] = key
print(a)
print("So lan dich chuyen:", shift_count)
