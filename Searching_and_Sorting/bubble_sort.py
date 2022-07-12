def bubble_sort(nums):
    for i in range(len(nums)):
        is_sorted = True

        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_sorted = False

        if is_sorted:
            break

    print(' '.join(str(x) for x in nums))


bubble_sort([int(n) for n in input().split()])
