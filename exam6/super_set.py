def subsets_util(A, subset, index):
    result.append([el for el in subset])

    for i in range(index, len(A)):
        subset.append(A[i])

        subsets_util(A, subset, i + 1)

        subset.pop(-1)

    return


def subsets(A):
    subset = []
    index = 0

    subsets_util(A, subset, index)


array = [int(x) for x in input().split(', ')]
result = []
subsets(array)

print(*[' '.join([str(x) for x in el]) for el in sorted(result, key=lambda x: len(x))], sep='\n')
