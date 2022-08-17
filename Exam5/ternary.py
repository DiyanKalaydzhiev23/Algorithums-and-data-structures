import re


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

    if result[0] == 't':
        result = resolver(line, result[2] + 1, result, True)
    elif result[0] == 'f':
        result = resolver(line, result[2] + 1, result, False)

    return result


line = list(filter(lambda x:  x not in ['?', ':'], re.split(r' ? | : ', input())))

print(resolver(line, 0, [], False)[0])

# t ? f ? 0 : t ? 2 : 3
# t ? f ? 0 : f ? 1 : 2
# f ? t ? 0 : 1 : t ? f ? 2 : f ? 5 : 10
