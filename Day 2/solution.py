import math


def part1(pos1, pos2):
    f = open("input.txt", "r")
    data = f.read()
    dataArray = data.split(',')
    dataArray = [int(i) for i in dataArray]
    index = 0
    dataArray[1] = pos1
    dataArray[2] = pos2

    while dataArray[index] != 99:
        first = dataArray[dataArray[index + 1]]
        second = dataArray[dataArray[index + 2]]
        if(dataArray[index] == 1):
            dataArray[dataArray[index + 3]] = first + second
        elif (dataArray[index] == 2):
            dataArray[dataArray[index + 3]] = first * second
        else:
            break

        index += 4
    f.close()
    return dataArray


def part2():
    f = open("input.txt", "r")
    for x in range(99):
        for y in range(99):
            res = part1(x, y)
            if res[0] == 19690720:
                return 100 * res[1] + res[2]


if __name__ == "__main__":
    part1Res = part1(12, 2)
    print("Part1 Solution: {}".format(part1Res[0]))
    part2Res = part2()
    print("Part2 Solution: {}".format(part2Res))
