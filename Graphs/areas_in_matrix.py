def find_area(r, c, let):
    if [r, c] in visited_points:
        return
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if matrix[r][c] != let:
        return

    visited_points.append([r, c])

    find_area(r + 1, c, let)
    find_area(r - 1, c, let)
    find_area(r, c + 1, let)
    find_area(r, c - 1, let)

    return 1


rows, cols = int(input()), int(input())
matrix = [list(input()) for _ in range(rows)]
result = {}
visited_points = []

for row in range(rows):
    for col in range(cols):
        letter = matrix[row][col]
        area = find_area(row, col, letter)

        if area:
            if letter not in result:
                result[letter] = 0

            result[letter] += area

print(f"Areas: {sum(result.values())}")
result = sorted(result.items(), key=lambda x: x[0])
[print(f"Letter '{r[0]}' -> {r[1]}") for r in result]
