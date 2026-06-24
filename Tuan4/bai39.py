students = [('An', 8), ('Ba', 9), ('Cu', 8)]
n = len(students)
for i in range(1, n):
    key = students[i]
    j = i - 1
    while j >= 0 and (students[j][1] < key[1] or (students[j][1] == key[1] and students[j][0] > key[0])):
        students[j + 1] = students[j]
        j -= 1
    students[j + 1] = key
print(students)
