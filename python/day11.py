with open("./day11.txt") as txt:
    input = {i.split(" ")[0][:-1]: i.split(" ")[1:] for i in txt.read().strip().split("\n")}

def part1():
    return depth_search(tuple(input["you"]))

def part2():
    return depth_search(tuple(input["dac"])) * depth_search(tuple(input["svr"]), target="fft") * depth_search(tuple(input["fft"]), target="dac")

memo = {}
def depth_search(cur_dev, target="out"):
    count = 0
    for dev in cur_dev:
        if dev == target:
            return 1
        if dev == "out":
            return 0

        args = (tuple(input[dev]), target)
        if args not in memo:
            memo[args] = depth_search(*args)
        count += memo[args]
    return count

print(part1())
print(part2())
