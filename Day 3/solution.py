import math


def calculateDistance(intersects):

    distances = []

    for x in intersects:
        distance = abs(x[0]) + abs(x[1])
        distances.append(distance)

    distances.sort()
    return distances


def checkIntersections(wire1, wire2):

    intersections = []
    i1 = 0
    i2 = 0

    for _ in wire1:

        if i1 >= len(wire1):
            return intersections

        dir1 = wire1[i1][2]
        x1 = wire1[i1][0]
        x2 = wire1[i1 + 1][0]
        y1 = wire1[i1][1]
        y2 = wire1[i1 + 1][1]

        for _ in wire2:

            if i2 >= len(wire2) - 1:
                break

            dir2 = wire2[i2][2]
            x3 = wire2[i2][0]
            x4 = wire2[i2 + 1][0]
            y3 = wire2[i2][1]
            y4 = wire2[i2 + 1][1]

            if(dir1 == 'H' and dir2 == 'V'):
                if (x1 <= x3 <= x2 or x2 <= x3 <= x1) and (y3 <= y1 <= y4 or y4 <= y1 <= y3):
                    intersections.append([x3, y1, i1, i2])
            if(dir1 == 'V' and dir2 == 'H'):
                if (y1 <= y3 <= y2 or y2 <= y3 <= y1) and (x3 <= x1 <= x4 or x4 <= x1 <= x3):
                    intersections.append([x1, y3, i1, i2])

            i2 += 2

        i1 += 2
        i2 = 0

    return intersections


def createWire(wire):

    wireCoords = []
    lastPosX = 0
    lastPosY = 0
    lastDir = 'T'

    for pos in wire:

        wireCoords.append([lastPosX, lastPosY, lastDir])

        if pos.startswith('R'):
            num = int(pos.lstrip('R'))
            wireCoords.append([lastPosX + num, lastPosY, 'H'])
        elif pos.startswith('L'):
            num = int(pos.lstrip('L'))
            wireCoords.append([lastPosX - num, lastPosY, 'H'])
            lastDir = 'H'
        elif pos.startswith('U'):
            num = int(pos.lstrip('U'))
            wireCoords.append([lastPosX, lastPosY - num, 'V'])
            lastDir = 'V'
        else:
            num = int(pos.lstrip('D'))
            wireCoords.append([lastPosX, lastPosY + num, 'V'])
            lastDir = 'V'

        lastPosX = wireCoords[len(wireCoords) - 1][0]
        lastPosY = wireCoords[len(wireCoords) - 1][1]
        wireCoords[len(wireCoords) - 2][2] = wireCoords[len(wireCoords) - 1][2]

    wireCoords[0][2] = wireCoords[1][2]

    return wireCoords


def sumWireIntersections(intersections, wire, n):
    index = 0
    sums = []

    for i in intersections:
        sumTimes = 0
        x = 0
        y = 0
        index2 = math.floor(i[n]/2)

        while index < index2:
            val = wire[index]
            num = int(val[1:])
            sumTimes += num
            index += 1
            if val.startswith('U'):
                y -= num
            elif val.startswith('D'):
                y += num
            elif val.startswith('L'):
                x -= num
            else:
                x += num

        if (i[2] != 0):
            if wire[index2].startswith('U'):
                sumTimes += y - i[1]
            elif wire[index2].startswith('D'):
                sumTimes += i[1] - y
            elif wire[index2].startswith('R'):
                sumTimes += i[0] - x
            elif wire[index2].startswith('L'):
                sumTimes += x - i[0]

        sums.append(sumTimes)
        index = 0

    return sums


def sumLists(sums1, sums2):

    allSums = []
    for i in range(len(sums1)):
        allSums.append(sums1[i] + sums2[i])

    allSums.sort()
    return allSums


def part1():
    f = open("input.txt", 'r')
    wire1 = f.readline().split(',')
    wire1Coords = createWire(wire1)

    wire2 = f.readline().split(',')
    wire2Coords = createWire(wire2)

    allIntersections = checkIntersections(wire1Coords, wire2Coords)

    allDists = calculateDistance(allIntersections)

    f.close()

    if allDists[0] != 0:
        return allDists[0]
    else:
        return allDists[1]


def part2():
    f = open("input.txt", 'r')
    wire1 = f.readline().split(',')
    wire1Coords = createWire(wire1)

    wire2 = f.readline().split(',')
    wire2Coords = createWire(wire2)

    allIntersections = checkIntersections(wire1Coords, wire2Coords)

    sums1 = sumWireIntersections(allIntersections, wire1, 2)
    sums2 = sumWireIntersections(allIntersections, wire2, 3)

    allSums = sumLists(sums1, sums2)
    print(allSums)

    f.close()

    if allSums[0] != 0:
        return allSums[0]
    else:
        return allSums[1]


if __name__ == "__main__":
    part1Res = part1()
    print("Part1 Solution: {}".format(part1Res))
    part2Res = part2()
    print("Part2 Solution: {}".format(part2Res))
