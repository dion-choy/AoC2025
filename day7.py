with open("day7.txt") as txt:
    input = txt.read().strip().split("\n")

def part1():
    beams = [0]*len(input[0])
    beams[input[0].index('S')] = 1

    count = 0
    for i in range(2, len(input), 2):
        for j in range(len(beams)):
            if input[i][j] == "^" and beams[j] == 1:
                count += 1
                beams[j-1] = 1
                beams[j+1] = 1
                beams[j] = 0

    return count

def part2():
    beams = [0]*len(input[0])
    beams[input[0].index('S')] = 1

    paths = []
    for i in range(2, len(input), 2):
        for j in range(len(beams)):
            if input[i][j] == "^" and beams[j] >= 1:
                beams[j-1] += beams[j]
                beams[j+1] += beams[j]
                beams[j] = 0

    return sum(beams)

print(part1())
print(part2())
