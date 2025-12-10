import itertools
from webbrowser import get

with open("./day10.txt") as txt:
    input = txt.read().strip().split("\n")

input = '''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''.strip().split("\n")

for i in range(len(input)):
    temp = []
    splits = input[i].split(" ")
    temp = [splits[0][1:-1], [eval(j) if type(eval(j))==tuple else (eval(j), ) for j in splits[1:-1]], eval(f"[{splits[-1][1:-1]}]")]

    input[i] = temp

def part1():
    count = 0
    for machine in input:
        done = False
        for i in range(len(machine[1])):
            for j in itertools.combinations(machine[1], i):
                lights = [0 for _ in range(len(machine[0]))]
                for k in j:
                    for l in k:
                        lights[l] += 1
                if [i%2 for i in lights] == [1 if machine[0][i]=='#' else 0 for i in range(len(machine[0]))]:
                    done = True
                    break
            if done:
                break

        count += len(j)

    return count

def part2():

    # count = 0
    # for machine in input:
    #     i = 0
    #     done = False
    #     while True:
    #         i += 1
    #         for j in itertools.combinations_with_replacement(machine[1], i):
    #             lights = [0 for _ in range(len(machine[0]))]
    #             done2 = False
    #             for k in j:
    #                 for l in k:
    #                     lights[l] += 1
    #                     if lights[l] > machine[2][l]:
    #                         done2 = True
    #                         break
    #                 if done2:
    #                     break
    #
    #             if lights == machine[2]:
    #                 done = True
    #                 break
    #         if done:
    #             break
    #
    #     count += len(j)

    count = 0
    for machine in input:
        lights = [0 for _ in range(len(machine[0]))]
        print("OUT", get_buttons(machine, 0, lights, 0))
            # if done:
            #     break
            # print(lights, buttons)
            # if lights == machine[2]:
            #     print("SAME")
            # print(test)
            # print(list(test))
        print("Test")

        # count += len(j)

    return count

def get_buttons(machine, index, prevLights, pressed):
    print(prevLights, machine[2], prevLights==machine[2], pressed)
    if prevLights == machine[2]:
        return prevLights, pressed
    if index == len(prevLights):
        return prevLights, pressed

    for i in itertools.combinations_with_replacement([i for i in machine[1] if index in i], machine[2][index]-prevLights[index]):
        lights = [i for i in prevLights]
        print(i)
        for j in i:
            for k in j:
                lights[k] += 1
        print(lights, i, index)

        if lights[index] == machine[2][index]:
            lights, pressed = get_buttons(machine, index+1, lights, pressed+len(i))
            return prevLights, pressed

        if lights[index] > machine[2][index]:
            return prevLights, pressed

    return prevLights, pressed

print()
print(part1())
print(part2())
