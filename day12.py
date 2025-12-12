with open("./day12.txt") as txt:
    input = txt.read().strip().split("\n")

    presents = [{"shape": [list(input[i+1]), list(input[i+2]), list(input[i+3])], "area": input[i+1].count("#") + input[i+2].count("#") + input[i+3].count("#")} for i in range(0, 6*5, 5)]
    input = [[[int(j) for j in i.split(" ")[0][:-1].split("x")], [int(j) for j in i.split(" ")[1:]]] for i in input[6*5:]]


def part1():
    count = 0
    for region, shapes in input:
        area = region[0] * region[1]

        shape_area = 0
        shape_area = sum([shapes[i]*presents[i]["area"] for i in range(len(shapes))])

        if shape_area > area:
            continue

        count += 1

    return count

print(part1())
