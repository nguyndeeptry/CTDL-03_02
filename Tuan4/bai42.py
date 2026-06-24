a = [1, 2, 4, 3, 5]
n = len(a)
shifts = 0
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
        shifts += 1
    a[j + 1] = key
print(a)
print("So shift:", shifts)
print("Mang gan sap xep nen shifts rat nho, xap xi O(n)")
