with open("day3.txt") as txt:
    input = txt.read().strip().split("\n")

def part1():
    count = 0
    for i in input:
        batts = [int(j) for j in i]
        nums = sorted(set(batts), reverse=True)
        if batts.index(nums[0]) != len(i)-1:
            count += nums[0]*10 + int(sorted(set(i[batts.index(nums[0])+1:]), reverse=True)[0])
        else:
            count += nums[1]*10 + int(sorted(set(i[batts.index(nums[1])+1:]), reverse=True)[0])

    return count

def part2():
    count = 0
    for i in input:
        num = ""

        index = [-1]
        for digit in range(12, 0, -1):
            maxPtr = len(i)-digit
            for curPtr in range(len(i)-digit, index[-1], -1):
                if int(i[curPtr]) >= int(i[maxPtr]):
                    maxPtr = curPtr
            index.append(maxPtr)

        num = ""
        index.pop(0)
        for j in index:
            num += i[j]

        count += int(num)

    return count

print(part1())
print(part2())
