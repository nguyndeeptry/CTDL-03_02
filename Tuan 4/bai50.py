def insertion_sort_verified(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        assert a[:i+1] == sorted(a[:i+1]), f"Bat bien vi pham tai buoc {i}"
    return a

a = [5, 2, 8, 1, 9, 3]
result = insertion_sort_verified(a[:])
print("Bat bien: truoc vong lap ngoai thu i, a[0..i-1] da duoc sap xep.")
print("Ket qua:", result)
