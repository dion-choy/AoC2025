with open("./day6.txt") as txt:
    input = txt.read().split("\n")

def part1():
    ls = [[k for k in j if k != ""] for j in [i.split(" ") for i in input if i != ""]]

    count = 0
    for j in range(len(ls[0])):
        cur = 1
        for i in range(len(ls)-1):
            if ls[-1][j] == "+":
                cur += int(ls[i][j])
            else:
                cur *= int(ls[i][j])

        count += cur-1 if ls[-1][j] == "+" else cur

    return count

def part2():
    ls = [i for i in input if i != ""]
    ops = [i for i in ls[-1].split(" ") if i != ""]

    count = 0
    col = 0
    cur = 1
    for j in range(len(ls[0])):
        num = ""
        for i in range(len(ls)-1):
            num += ls[i][j] if ls[i][j] != " " else ""

        if num.strip() == "":
            count += cur-1 if ops[col] == "+" else cur
            cur = 1
            col += 1
        else:
            if ops[col] == "+":
                cur += int(num)
            else:
                cur *= int(num)

    count += cur-1 if ops[col] == "+" else cur

    return count

print(part1())
print(part2())
