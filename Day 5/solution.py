import math


def solution():
    f = open("input.txt", "r")
    data = f.read()
    dataArray = data.split(',')
    dataArray = [int(i) for i in dataArray]

    index = 0

    while str(dataArray[index])[:-3:-1] != "99":

        codeStr = str(dataArray[index]).zfill(5)
        opcode = int(codeStr[3:])
        leap = 0

        if opcode in [1, 2, 4, 5, 6, 7, 8]:
            first = dataArray[index +
                              1] if int(codeStr[2]) else dataArray[dataArray[index + 1]]
        if opcode in [1, 2, 5, 6, 7, 8]:
            second = dataArray[index +
                               2] if int(codeStr[1]) else dataArray[dataArray[index + 2]]

        if opcode in [1, 2, 7, 8]:
            leap = 4

            if opcode == 1:
                dataArray[dataArray[index + 3]] = first + second
            elif opcode == 2:
                dataArray[dataArray[index + 3]] = first * second
            elif opcode == 7:
                dataArray[dataArray[index + 3]] = first < second
            elif opcode == 8:
                dataArray[dataArray[index + 3]] = first == second

        elif opcode in [3, 4]:
            leap = 2
            if opcode == 3:
                dataArray[dataArray[index + 1]] = int(input())
            elif opcode == 4:
                print(first)

        elif opcode in [5, 6]:
            if (opcode == 5 and first) or (opcode == 6 and not first):
                index = second
            else:
                leap = 3
        index += leap
    f.close()


if __name__ == "__main__":
    # For Part 1 input 1
    # For Part 2 input 5
    solution()
