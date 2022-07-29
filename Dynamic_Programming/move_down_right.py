from collections import deque

rows = int(input())
cols = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
dp = [[0] * cols for _ in range(rows)]

dp[0][0] = matrix[0][0]
queue = deque()

for row in range(1, rows):
    dp[row][0] = dp[row-1][0] + matrix[row][0]

for col in range(cols):
    dp[0][col] = dp[0][col-1] + matrix[0][col]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + matrix[row][col]

row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    queue.appendleft([row, col])

    if dp[row][col-1] >= dp[row-1][col]:
        col -= 1
    else:
        row -= 1

for idx in range(row, 0, -1):
    queue.appendleft([idx, col])

for idx in range(col, 0, -1):
    queue.appendleft([row, idx])

queue.appendleft([0, 0])

print(*queue, sep=' ')
