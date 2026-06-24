a = [1, 3, 5, 7]
x = 4
i = len(a) - 1
a.append(x)
while i >= 0 and a[i] > x:
    a[i + 1] = a[i]
    i -= 1
a[i + 1] = x
print(a)
