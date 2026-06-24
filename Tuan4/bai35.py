def count_inversions_and_shifts(a):
    b = a[:]
    n = len(b)
    shifts = 0
    for i in range(1, n):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
            shifts += 1
        b[j + 1] = key

    inversions = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inversions += 1
    return shifts, inversions

a = [2, 4, 1, 3]
s, inv = count_inversions_and_shifts(a)
print(f"So shift: {s}, So nghich the: {inv}, Bang nhau: {s == inv}")
