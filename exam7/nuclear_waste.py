import sys
from collections import deque

costs = [int(x) for x in input().split()]
n = int(input())

result = deque()

dp = [0] * (n + 1)
prev = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = sys.maxsize

    for j in range(1, i + 1):
        if j > len(costs):
            break

        new_value = dp[i - j] + costs[j - 1]

        if new_value < dp[i]:
            dp[i] = new_value
            prev[i] = j

print(f"Cost: {dp[n]}")

while n > 0:
    result.appendleft(f'{prev[n]} => {costs[prev[n] - 1]}')
    n -= prev[n]

print(*sorted(result, key=lambda x: x.split(' => ')[0]), sep='\n')
