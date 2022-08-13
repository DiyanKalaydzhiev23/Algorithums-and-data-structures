def resolver(line, idx):
    if line[idx] == "t":
        if line[idx + 1] not in ["t", "f"]:
            return line[idx + 1]
        return resolver(line, idx + 1)
    elif line[idx] == "f":
        if line[-idx-1] not in ["t", "f"]:
            return line[-idx-1]
        return resolver(line, len(line) - idx - 1)


line = input().split(" ? ")
second = line.pop().split(" : ")

for el in second:
    line.append(el)

print(resolver(line, 0))
