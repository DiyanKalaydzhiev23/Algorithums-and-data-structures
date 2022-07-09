rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]
solutions = {}
solution_number = 1


def explore_area(r, c):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return 0
    if matrix[r][c] != '-':
        return 0

    matrix[r][c] = 'v'
    result = 1

    result += explore_area(r + 1, c)
    result += explore_area(r - 1, c)
    result += explore_area(r, c + 1)
    result += explore_area(r, c - 1)

    return result


for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col)
        if size:
            solutions[solution_number] = {
                'start_point': (row, col),
                'size': size,
            }
            solution_number += 1

print(f'Total areas found: {len(solutions)}')
for el in sorted(solutions.items(), key=lambda x: (-x[1]['size'], x[0])):
    print(f'Area #{el[0]} at {el[1]["start_point"]}, size: {el[1]["size"]}')
