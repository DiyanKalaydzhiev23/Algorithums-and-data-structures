def sum_list(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + sum_list(numbers, idx + 1)


print(sum_list([int(x) for x in input().split(' ')], 0))
