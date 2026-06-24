def analyze_insertion(a):
    b = a[:]
    n = len(b)
    cmps = 0
    shifts = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0:
            cmps += 1
            if b[j] > key:
                b[j + 1] = b[j]
                j -= 1
                shifts += 1
            else:
                break
        b[j + 1] = key
    return cmps, shifts

sorted_a = [1, 2, 3, 4, 5]
random_a = [3, 1, 4, 5, 2]
reverse_a = [5, 4, 3, 2, 1]

for name, arr in [("Da sap xep (best)", sorted_a), ("Ngau nhien (avg)", random_a), ("Nguoc (worst)", reverse_a)]:
    c, s = analyze_insertion(arr)
    print(f"{name}: so sanh={c}, shift={s}")
