with open("day5.txt") as txt:
    input = txt.read().strip().split("\n\n")
    input[0] = input[0].split("\n")
    input[1] = input[1].split("\n")

ranges = [[int(j) for j in  i.split("-")] for i in input[0]]
fruits = [int(i) for i in input[1]]

def part1():
    count = 0

    for i in fruits:
        for j in ranges:
            if i >= j[0] and i <= j[1]:
                count += 1
                break

    return count

def part2():
    rnges = sorted(ranges)
    all_ranges = [rnges[0]]

    for i in range(1, len(rnges)):
        if rnges[i][0] <= all_ranges[-1][1]:
            all_ranges[-1] = [min(*all_ranges[-1], *rnges[i]), max(*all_ranges[-1], *rnges[i])]

        else:
            all_ranges.append(rnges[i])

    count = 0
    for i in all_ranges:
        count += i[1]-i[0]+1
    return count

print(part1())
print(part2())
