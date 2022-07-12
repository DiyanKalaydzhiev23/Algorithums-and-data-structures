def binary_search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2

        if nums[mid_idx] == target:
            return mid_idx
        if nums[mid_idx] > target:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1

    return -1


print(binary_search([int(n) for n in input().split(' ')], int(input())))
