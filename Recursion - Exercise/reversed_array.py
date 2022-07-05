def reverse_array(idx, array, new_array):
    if idx > len(array):
        return ' '.join(new_array)

    new_array.append(array[-idx])

    return reverse_array(idx + 1, array, new_array)


print(reverse_array(1, input().split(' '), []))
