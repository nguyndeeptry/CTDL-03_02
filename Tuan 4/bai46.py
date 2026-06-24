def count_inversions_merge(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, l_inv = count_inversions_merge(a[:mid])
    right, r_inv = count_inversions_merge(a[mid:])
    merged = []
    inv = l_inv + r_inv
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

import random
a = random.sample(range(1, 100001), 1000)
_, total_shifts = count_inversions_merge(a)
print("Tong so shift (=nghich the):", total_shifts)
