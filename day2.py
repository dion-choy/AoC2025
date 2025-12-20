import time

with open("day2.txt") as txt:
    input = txt.read().strip().split(",")
    input = [i.split("-") for i in input]

def part1():
    count = 0
    for i in input:
        for j in range(int(i[0]), int(i[1])+1):
            j = str(j)
            if j[:len(j)//2] == j[len(j)//2:]:
                count += int(j)
    return count

def split(num, splits):
    if len(num) % splits == 0:
        seg_len = len(num) // splits
        arr = []
        for i in range(0, len(num), seg_len):
            arr.append(num[i:i+seg_len])
        return arr

def part2():
    count = 0
    for i in input:
        for j in range(int(i[0]), int(i[1])+1):
            j = str(j)
            for k in range(2, len(i[1])+1):
                splits = split(j, k)
                if splits is not None and len(set(splits)) == 1:
                    count += int(j)
                    break
    return count

start = time.time()
print(part1(), "(%fs)" % (time.time()-start))
start = time.time()
print(part2(), "(%fs)" % (time.time()-start))

