def generate_vectors(vector, idx):
    if idx == n:
        print(''.join(str(x) for x in vector))
        return

    for number in range(0, 2):
        vector[idx] = number
        generate_vectors(vector, idx + 1)


n = int(input())
vector = [0 for num in range(n)]

generate_vectors(vector, 0)
