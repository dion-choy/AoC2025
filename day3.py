with open("day3.txt") as txt:
    input = txt.read().strip().split("\n")

# txt = '''987654321111111
# 811111111111119
# 234234234234278
# 818181911112111'''

txt = '''2232212212212222211221231124224222213132222133122224222123222112324122222122221322222225222342243112
2222312114222314322223142323251122424322142244122212213222222222242526225232262212234353242222112242
3325444446453345434534234244443254434533443354443344424431124344542134454433534353443542455544444483
2334235313232232645234524223233333333323323333233334323332325633143222333322242333132233233132212325
2234311224123424222222224432222333212224412234223312244413252153222112433222334322772215422121224273'''
input = txt.split("\n")

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
        first_digit = sorted(i[:-12])[-1]
        num += first_digit

        remaining = i[i.index(first_digit):]
        # while(len(remaining)>12):
        next_highest = sorted(remaining[1:])

        while len(remaining) - remaining.index(next_highest[-1], 1) >= 12:
            num += next_highest[-1]
            print("NUM", num)
            remaining = remaining[remaining.index(next_highest[-1], 1):]
            next_highest = sorted(remaining[1:])


        print(i)
        print(remaining)
        print(next_highest)
        print(next_highest[-1])
        print(remaining.index(next_highest[-1], 1))

        if len(remaining) - remaining.index(next_highest[-1], 1) < 12:
            print("NOT ENOUGH LENGTH", len(remaining) - remaining.index(next_highest[-1], 1))
            print("NUM", num)

        # if len()
        # num_str = first_digit + remaining[remaining.index(next_highest[-2], 1)]
        #
        # print(num_str)

        remaining = i[i.index(first_digit):]

        # count += int(remaining)

    return count

# 2222312114222314322223142323251122424322142244122212213222222222242526225232262212234353242222112242
# 6225232262212234353242222112242
# 665422222242
# 653634353442
# 656454222242

print(part1())
print(part2())
