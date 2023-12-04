def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    total = 0
    # part1
    for l in lines:
        # split on colon to get rid of card #
        l = l.split(":")[1]
        parts = l.split("|")
        winning = parts[0].lstrip().rstrip()
        have = parts[1].lstrip().rstrip()

        winningSet = set([w for w in winning.split(" ") if len(w) > 0])
        haveSet = set([h for h in have.split(" ") if len(h) > 0])

        result = winningSet.intersection(haveSet)
        # print(result)
        if len(result) == 0:
            continue
        total += 2 ** (len(result) - 1)

    print(total)




if __name__ == "__main__":
    main()