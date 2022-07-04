def draw(n):
    if n == 0:
        return 

    print('*' * n)
    draw(n - 1)
    print('#' * n)


draw(int(input()))
