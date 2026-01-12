with open("day4.txt") as txt:
    input = [list(i) for i in txt.read().strip().split("\n")]

def part1():
    count = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == ".":
                continue

            surr = -1
            for x_off in range(-1, 2):
                if i+x_off < 0 or i+x_off >= len(input[i]):
                    continue
                for y_off in range(-1, 2):
                    if j+y_off < 0 or j+y_off >= len(input[j]):
                        continue
                    if input[i+x_off][j+y_off] == "@":
                        surr += 1
            if surr < 4:
                count += 1

    return count

def part2():
    count = 0
    global input

    copy = [[j for j in i] for i in input]

    curCount = -1
    while (curCount !=0):
        curCount = 0
        for i in range(len(input)):
            for j in range(len(input)):
                if input[i][j] == ".":
                    continue

                surr = -1
                for x_off in range(-1, 2):
                    if i+x_off < 0 or i+x_off >= len(input[i]):
                        continue
                    for y_off in range(-1, 2):
                        if j+y_off < 0 or j+y_off >= len(input[j]):
                            continue
                        # print(i+x_off, j+y_off)
                        if input[i+x_off][j+y_off] == "@":
                            surr += 1

                if surr < 4:
                    curCount += 1
                    copy[i][j] = "."

        input = [[j for j in i] for i in copy]
        count += curCount

    return count

print(part1())
print(part2())
