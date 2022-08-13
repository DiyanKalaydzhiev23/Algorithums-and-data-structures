def resolver(line, idx, result, has_to_be_true):
    if line[idx] == "t":
        has_to_be_true = True
    elif line[idx] == "f":
        has_to_be_true = False
    else:
        if has_to_be_true:
            result = [line[idx], True, idx + 1]
        else:
            if idx < len(line) - 1:
                result = [line[idx + 1], False, idx]
            else:
                result = [line[idx], False, idx]
        return result

    result = resolver(line, idx + 1, result, has_to_be_true)

    if result[1] and not has_to_be_true:
        line[idx+1:result[2]+1] = result[0]
        result = resolver(line, idx, result, has_to_be_true)

    return result


line = input().split(" ? ")
second = line.pop().split(" : ")

for el in second:
    line.append(el)

print(resolver(line, 0, [], False)[0])
