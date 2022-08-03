from collections import deque


n = int(input())
i = 0
nums = [1] * n
result = deque()

result.appendleft([*nums])

while len(nums) > 1:
    if len(nums) == 2:
        if nums[0] == n - 1:
            break
        else:
            nums[0] += 1
            nums[1] -= 1
    else:
        nums[i] += 1
        nums.pop()
        i += 1

        if i >= len(nums):
            i = 0

        if sum(nums) < n:
            for _ in range(n - sum(nums)):
                nums.append(1)
        if len(nums) == 2:
            if nums[0] == n - 1:
                result.appendleft([*nums])
                break
            else:
                nums[0] += 1
                nums[1] -= 1

    result.appendleft([*nums])


print(n)
print(*[' + '.join(str(x) for x in res) for res in result], sep='\n')
