def quick_sort(start, end):
    if start >= end:
        return nums

    pivot, left, right = start, start + 1, end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]

    quick_sort(start, right - 1)
    quick_sort(right + 1, end)


nums = [int(n) for n in input().split()]
quick_sort(0, len(nums) - 1)
print(' '.join(str(n) for n in nums))
