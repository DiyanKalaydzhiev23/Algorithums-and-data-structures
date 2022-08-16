nums = [int(x) for x in input().split()]
length = len(nums)
min_sum = 0

for i in range(0, length, 4):
    if length - i < 4:
        min_sum += min(nums[i:])
    else:
        min_sum += min(nums[i:i + 4])

print(min_sum)
