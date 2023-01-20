row, col = map(int, input().split())
floor = [list(input()) for _ in range(row)]

count = 0
for i in range(row):
    for j in range(col):
        if floor[i][j] != "-" or (j - 1 >= 0 and floor[i][j - 1] == "-"):
            continue
        else:
            count += 1
for i in range(col):
    for j in range(row):
        if floor[j][i] != "|" or (j - 1 >= 0 and floor[j - 1][i] == "|"):
            continue
        else:
            count += 1
            
print(count)
