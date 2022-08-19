from itertools import permutations

perm = permutations(input().split(), int(input()))
print(*[' '.join(x) for x in list(perm)], sep='\n')
