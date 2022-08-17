def find_tunnel(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if matrix[r][c] == "d":
        return

    matrix[r][c] = "d"

    find_tunnel(r + 1, c)
    find_tunnel(r - 1, c)
    find_tunnel(r, c + 1)
    find_tunnel(r, c - 1)
    find_tunnel(r + 1, c + 1)
    find_tunnel(r - 1, c - 1)

    return 1


rows, cols = int(input()), int(input())
tunnels = 0
matrix = [list(input()) for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "t":
            tunnels += find_tunnel(row, col)

print(tunnels)
