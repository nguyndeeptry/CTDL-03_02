a = ['abc', 'a', 'ab']
n = len(a)
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and len(a[j]) > len(key):
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
print(a)
