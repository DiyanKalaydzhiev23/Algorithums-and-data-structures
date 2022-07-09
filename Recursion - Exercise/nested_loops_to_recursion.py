def get_nested_loops(idx, array):
    if idx >= len(array):
        print(*array, sep=' ')
        return
    for num in range(1, len(array) + 1):
        array[idx] = num
        get_nested_loops(idx + 1, array)


n = int(int(input()))
get_nested_loops(0, [None] * n)
