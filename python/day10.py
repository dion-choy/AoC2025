import itertools
import z3

with open("./day10.txt") as txt:
    input = [
        [
            i.split(" ")[0][1:-1],
            [eval(j) if type(eval(j))==tuple else (eval(j), ) for j in i.split(" ")[1:-1]],
            eval(f"[{i.split(' ')[-1][1:-1]}]")
        ]
        for i in txt.read().strip().split("\n")
    ]

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
    count = 0
    for machine in input:
        s = z3.Optimize()
        vars = []
        for i in range(len(machine[1])):
            vars.append(z3.Int(str(i)))

        for i in range(len(machine[2])):
            buttons = [j for j in range(len(machine[1])) if i in machine[1][j]]
            eq = None
            for j in buttons:
                if eq is None:
                    eq = vars[j]
                else:
                    eq += vars[j]

            s.add(eq == machine[2][i])

        for i in vars:
            s.add(i >= 0)

        min = s.minimize(sum(vars))
        s.check()
        s.model()
        count += min.value().as_long()

    return count

print(part1())
print(part2())
