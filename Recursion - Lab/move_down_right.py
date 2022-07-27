rows = int(input())
cols = int(input())
paths = 0


def find_path(r, c):
    global paths

    if r > rows or c > cols:
        return
    if r == rows and c == cols:
        paths += 1

    find_path(r + 1, c)
    find_path(r, c + 1)


find_path(1, 1)
print(paths)
