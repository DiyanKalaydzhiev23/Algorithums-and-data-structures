def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    print(' '.join(str(n) for n in nums))


insertion_sort([int(n) for n in input().split()])
