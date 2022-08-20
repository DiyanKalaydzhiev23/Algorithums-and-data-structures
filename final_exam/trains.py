arrivals = [float(t) for t in input().split()]
departures = [float(t) for t in input().split()]

trains = {i: [arrivals[i], departures[i]] for i in range(len(arrivals))}
platforms = {}
platforms_count = 0

for h in range(24):
    if h not in [int(a) for a in arrivals] and h not in [int(d) for d in departures]:
        continue

    for m in range(60):
        time = round(h + m / 100, 2)

        for i in range(len(trains)):
            curr_arr, curr_dep = trains[i]

            while time in [v[1] for v in platforms.values()]:
                key, values = next(filter(lambda x: x[1][1] == time, platforms.items()))
                print(platforms[key])
                del platforms[key]

            if curr_arr == time:
                platforms[i] = [curr_arr, curr_dep]
                if len(platforms) > platforms_count:
                    platforms_count += 1
            if curr_dep == time:
                if curr_dep >= curr_arr and i in platforms:
                    print(platforms[i])
                    del platforms[i]

print(platforms_count)
