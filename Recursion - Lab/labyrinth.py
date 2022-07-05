def find_paths(r, c, lab, step, path):
    if r < 0 or c < 0 or r == rows or c == cols:
        return
    if lab[r][c] == '*' or lab[r][c] == '.':
        return
    if step:
        path.append(step)
    if lab[r][c] == 'e':
        print(''.join(path))
    else:
        lab[r][c] = '.'

        find_paths(r - 1, c, lab, "U", path)
        find_paths(r + 1, c, lab, "D", path)
        find_paths(r, c - 1, lab, "L", path)
        find_paths(r, c + 1, lab, "R", path)

        lab[r][c] = '-'

    if path:
        path.pop()


rows = int(input())
cols = int(input())

labyrinth = [list(input()) for _ in range(rows)]

find_paths(0, 0, labyrinth, '', [])
