with open("./day8.txt") as txt:
    input = [[int(j) for j in i.split(",")] for i in txt.read().strip().split("\n")]

def dist(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)**(0.5)

def part1():
    distance = []
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                continue
            distance.append((min(i, j), max(i, j), dist(input[i], input[j])))

    shortlist = sorted(set(distance), key=lambda x: x[2])[:1000]

    circuits = []
    for i in range(len(shortlist)):
        for j in circuits:
            if shortlist[i][0] in j or shortlist[i][1] in j:
                j.update((shortlist[i][0], shortlist[i][1]))
                break
        else:
            circuits.append({shortlist[i][0], shortlist[i][1]})

    changes = True
    while changes:
        changes = False
        for i in range(len(circuits)):
            for j in range(len(circuits)):
                if len(circuits[i] & circuits[j]) > 0 and circuits[i] != circuits[j]:
                    changes = True
                    circuits[i] = circuits[i].union(circuits[j])

    circuits = list(set([tuple(sorted(list(i))) for i in circuits]))
    circuits.sort(key=lambda x: len(x), reverse=True)

    return len(circuits[0])*len(circuits[1])*len(circuits[2])

def part2():
    distance = []
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                continue
            distance.append((min(i, j), max(i, j), dist(input[i], input[j])))

    shortlist = sorted(set(distance), key=lambda x: x[2])

    circuits = []
    for i in range(len(shortlist)):
        for j in circuits:
            if shortlist[i][0] in j or shortlist[i][1] in j:
                j.update((shortlist[i][0], shortlist[i][1]))
                break
        else:
            circuits.append({shortlist[i][0], shortlist[i][1]})

        changes = True
        while changes:
            changes = False
            for k in range(len(circuits)):
                for l in range(len(circuits)):
                    if len(circuits[k] & circuits[l]) > 0 and circuits[k] != circuits[l]:
                        changes = True
                        circuits[k] = circuits[k].union(circuits[l])
        circuits = [set(i) for i in list(set([tuple(sorted(list(i))) for i in circuits]))]

        if len(circuits[0]) == len(input):
            break

    return input[shortlist[i][0]][0] * input[shortlist[i][1]][0]

print(part1())
print(part2())
