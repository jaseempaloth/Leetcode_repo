l = [1, 2, 3, 4, 5, 6, 7]
target = 9
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            print(i, j)
            break
