def selection_sort_verified(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        assert a[:i+1] == sorted(a)[:i+1], f"Bat bien vi pham tai vong {i}"
    return a

a = [4, 2, 7, 1, 3, 6, 5]
result = selection_sort_verified(a[:])
print("Bat bien vong lap: sau vong i, a[0..i] chua i+1 phan tu nho nhat da sap xep.")
print("Ket qua:", result)
