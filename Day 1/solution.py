import math


def part1():
    f = open("input.txt", "r")
    totalSum = 0
    for line in f:
        totalSum += math.floor(int(line) / 3) - 2
    f.close()
    return totalSum


def part2():
    f = open("input.txt", "r")
    totalSum = 0
    for line in f:
        value = math.floor(int(line) / 3) - 2
        while True:
            if (value <= 0):
                break
            totalSum += value
            value = math.floor(int(value) / 3) - 2
    f.close()
    return totalSum


if __name__ == "__main__":
    part1 = part1()
    print("Part1 Solution: {}".format(part1))
    part2 = part2()
    print("Part2 Solution: {}".format(part2))
