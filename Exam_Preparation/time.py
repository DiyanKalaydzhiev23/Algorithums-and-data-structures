from collections import deque

first = input().split()
second = input().split()

rows = len(first) + 1
cols = len(second) + 1
lcs = [[0] * cols for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            prev = lcs[row - 1][col - 1]
            lcs[row][col] = prev + 1
        else:
            up = lcs[row - 1][col]
            left = lcs[row][col - 1]
            lcs[row][col] = max(up, left)

lcs_nums = deque()
row = rows - 1
col = cols - 1

while row >= 0 and col >= 0:
    if first[row - 1] == second[col - 1]:
        lcs_nums.appendleft(first[row - 1])
        row -= 1
        col -= 1
    elif lcs[row - 1][col] > lcs[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(*lcs_nums, sep=' ')
print(len(lcs_nums))
