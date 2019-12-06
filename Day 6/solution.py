with open('input.txt') as f:
    data = f.readlines()
data = [x.strip().split(')') for x in data]


def createGraph(root, data, graph=None):
    if not graph:
        graph = {root: [], **{k[1]: [] for k in data}}

    for a, b in data:
        if a == root:
            graph[b] = graph[a] + [b]
            createGraph(b, data, graph)
    return graph


def part1():
    g = createGraph('COM', data)
    return sum(len(v) for k, v in g.items())


def part2():
    cnt = 0
    g = createGraph('COM', data)
    pFrom = g['YOU']
    pTo = g['SAN']
    for o in pFrom[::-1][1:]:
        if o not in pTo:
            cnt += 1
        else:
            break

    pFrom = g['SAN']
    pTo = g['YOU']
    for o in pFrom[::-1][1:]:
        if o not in pTo:
            cnt += 1
        else:
            break

    return cnt


if __name__ == "__main__":
    solution1 = part1()
    print("Part1 Solution: {}".format(solution1))
    solution2 = part2()
    print("Part2 Solution: {}".format(solution2))
