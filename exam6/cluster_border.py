from collections import deque

single_entry = [int(x) for x in input().split()]
combined_entry = [int(x) for x in input().split()]

memory = [0] * (len(single_entry) + 1)
memory[1] = single_entry[0]

for i in range(2, len(single_entry) + 1):
    single_ship_time = memory[i - 1] + single_entry[i - 1]
    pair_ship_time = memory[i - 2] + combined_entry[i - 2]

    memory[i] = min(single_ship_time, pair_ship_time)

print(f"Optimal Time: {memory[-1]}")

idx = len(memory) - 1
result = deque()

while idx > 0:
    if memory[idx - 1] + single_entry[idx - 1] == memory[idx]:
        line = f"Single: {idx}"
        idx -= 1
    else:
        line = f"Pair of {idx - 1} and {idx}"
        idx -= 2
    result.appendleft(line)

print('\n'.join(result))
