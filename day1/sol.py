def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        print(lines)

    # part1
    # define the numbers we're interested in
    nums = "123456789"
    total = 0

    dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # loop thru line, if it's a number keep it, if it's not, continue
    for l in lines:
        num1 = 0
        num1_idx = 0
        num2 = 0
        num2_idx = 0

        # check real numbers first
        for idx in range(len(l)):
            c = l[idx]
            if c in nums:
                if num1 == 0:
                    num1 = c
                    num1_idx = idx
                num2 = c
                num2_idx = idx

        print(num1, num2)
        print(num2_idx)
        # check string numbers
        # if l[-1] not in nums:

        for s in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
            # check num1_idx and num2_idx
            start = 0
            "sevenone2one58one"
            while s in l[start:]:
                idx = l[start:].index(s) + start
                start += len(s)
                if idx <= num1_idx:
                    num1 = dict[s]
                    num1_idx = idx
                if idx > num2_idx:
                    print(f"{idx} > {num2_idx}")
                    num2 = dict[s]
                    num2_idx = idx

            if s not in l:
                continue
            
        partial = str(num1) + str(num2)
        print(partial)
        total += int(partial)
    print(total)



if __name__ == "__main__":
    main()