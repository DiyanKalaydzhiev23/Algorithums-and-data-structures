from collections import deque

nums = [int(x) for x in input().split()]

length = [0] * len(nums)
parent = [0] * len(nums)

best_len = 0
best_idx = -1

for curr_idx in range(len(nums)):
    curr_num = nums[curr_idx]
    curr_len = 1
    curr_parent = -1

    for prev_idx in range(curr_idx - 1, -1, -1):
        prev_number = nums[prev_idx]
        prev_len = length[prev_idx]
        if curr_num > prev_number and prev_len + 1 >= curr_len:
            curr_len = prev_len + 1
            curr_parent = prev_idx

    length[curr_idx] = curr_len
    parent[curr_idx] = curr_parent

    if curr_len > best_len:
        best_len = curr_len
        best_idx = curr_idx

lis = deque()
idx = best_idx

while idx != -1:
    lis.appendleft(nums[idx])
    idx = parent[idx]

print(*lis, sep=' ')

# 3 14 5 12 15 7 8 9 11 10 1
