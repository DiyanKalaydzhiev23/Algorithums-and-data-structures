def find_other_subset(first_subset):
    second_subset = []

    for b in boxes:
        if b not in first_subset:
            second_subset.append(b)

    return sorted(second_subset)


def find_subset(sums, target):
    subset = set()

    while target != 0:
        element = sums[target]
        subset.add(element)

        target -= element

    return sorted(subset)


def find_all_sums(elements, target):
    sums = {0: 0}

    for el in elements:
        for s in list(sums.keys()):
            new_sum = s + el

            if new_sum in sums:
                continue

            sums[new_sum] = el

            if new_sum == target:
                return sums

    return sums


boxes = [int(x) for x in input().split()]
target = sum(boxes) // 2
all_sums = find_all_sums(boxes, target)
josh_boxes = find_subset(all_sums, target)
parkash_boxes = find_other_subset(josh_boxes)

print(*josh_boxes, sep=' ')
print(*parkash_boxes, sep=' ')
