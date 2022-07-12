def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx
        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

    return ' '.join(str(x) for x in nums)


print(selection_sort([int(n) for n in input().split()]))
