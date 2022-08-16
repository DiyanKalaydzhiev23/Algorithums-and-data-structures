import itertools
from collections import deque

alphabets = input()
n = int(input())
result = deque()

for el in [''.join(i) for i in itertools.product(alphabets, repeat=n)][::-1]:
    if el[::-1] not in result:
        result.append(el)

print(*sorted(result), sep='\n')
