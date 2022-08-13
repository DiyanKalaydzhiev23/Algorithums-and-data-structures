class Exchange:
    def __init__(self, first, second, rate):
        self.first = first
        self.second = second
        self.rate = rate


def deep(currency, exchange_with=None, max_rate=0):
    global money

    went_by.append(currency)
    went_by_money_data.append(money)

    for c in graph[currency]:
        if c.rate > max_rate:
            exchange_with = c

    money *= exchange_with.rate

    if exchange_with.second == target:
        return

    deep(exchange_with.second)


pairs = int(input())
graph = {}
money = 1

for _ in range(pairs):
    first, second, rate = input().split()
    exchange = Exchange(first, second, float(rate))

    if first not in graph:
        graph[first] = []

    graph[first].append(exchange)

target = input()
went_by = []
went_by_money_data = []

deep(target)

if money > 1:
    print(True)
    print(' '.join(went_by) + ' ' + target)
else:
    print(False)
    print('\n'.join([f"{went_by[i]}: {went_by_money_data[i]:.3f}" for i in range(len(went_by_money_data))]))
