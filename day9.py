with open("./day9.txt") as txt:
    input = [[int(j) for j in i.split(",")] for i in txt.read().strip().split("\n")]

def part1():
    biggest_area = 0
    for i in range(len(input)):
        for j in range(i, len(input)):
            if (abs(input[i][0] - input[j][0])+1) * (abs(input[i][1] - input[j][1])+1) > biggest_area:
                biggest_area = (abs(input[i][0] - input[j][0])+1) * (abs(input[i][1] - input[j][1])+1)

    return biggest_area

def part2():
    lines = set()
    for i in range(0, len(input)):
        if input[i][0] == input[i-1][0]:
            lines.update((input[i][0], j) for j in range(min(input[i][1], input[i-1][1]), max(input[i][1], input[i-1][1])+1))
        else:
            lines.update((j, input[i][1]) for j in range(min(input[i][0], input[i-1][0]), max(input[i][0], input[i-1][0])+1))

    biggest_area = 0
    for i in range(len(input)):
        for j in range(i, len(input)):
            if i == j:
                continue

            if (abs(input[i][0] - input[j][0])+1) * (abs(input[i][1] - input[j][1])+1) > biggest_area:
                for k in lines:
                    if (k[0] > min(input[i][0], input[j][0]) and k[0] < max(input[i][0], input[j][0])) and \
                        (k[1] > min(input[i][1], input[j][1]) and k[1] < max(input[i][1], input[j][1])):
                        break
                else:
                    biggest_area = (abs(input[i][0] - input[j][0])+1) * (abs(input[i][1] - input[j][1])+1)

    return biggest_area

print(part1())
print(part2())
