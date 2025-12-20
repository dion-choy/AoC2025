import time

with open("day1.txt") as txt:
    input = txt.read().strip().split("\n")

def part1():
    cur = 50
    count = 0
    for i in input:
        num = int(i[1:])

        if i[0] == "L":
            cur += num
        elif i[0] == "R":
            cur -= num

        if cur>0:
            cur = (cur+1)%100-1
        elif cur<0:
            cur = (cur+100)%100
        
        if cur == 0:
            count += 1
    return count

def part2():
    cur = 50
    count = 0
    for i in input:
        num = int(i[1:])

        if i[0] == "L":
            for i in range(num):
                cur += 1
                cur = (cur+1)%100-1
                if cur == 0:
                    count += 1
        elif i[0] == "R":
            for i in range(num):
                cur -= 1
                cur = (cur+100)%100
                if cur == 0:
                    count += 1
    return count

start = time.time()
print(part1(), "(%fs)" % (time.time()-start))
start = time.time()
print(part2(), "(%fs)" % (time.time()-start))
