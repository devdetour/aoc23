def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    cards = [1] * len(lines)

    # part1
    for idx in range(len(lines)):
        l = lines[idx]
        # split on colon to get rid of card #
        l = l.split(":")[1]
        parts = l.split("|")
        winning = parts[0].lstrip().rstrip()
        have = parts[1].lstrip().rstrip()

        winningSet = set([w for w in winning.split(" ") if len(w) > 0])
        haveSet = set([h for h in have.split(" ") if len(h) > 0])

        result = winningSet.intersection(haveSet)
        if len(result) == 0:
            continue
        for i in range(len(result)):
            cards[idx + i + 1] += cards[idx]

    print(sum(cards))




if __name__ == "__main__":
    main()