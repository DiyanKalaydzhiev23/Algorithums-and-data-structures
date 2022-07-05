def get_nested_loops(idx, loop_idx, max_n, loops):
    print(loops)

    if loop_idx == n * n:
        return

    if loops[-idx] == max_n:
        if idx == n:
            loop_idx += 1
            idx = 0
        loops[-idx] = 1
        idx += 1

    loops[-idx] += 1

    get_nested_loops(idx, loop_idx + 1, max_n, loops)


n = 3
get_nested_loops(1, 0, n, [1] * n)
