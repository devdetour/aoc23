def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

        print(lines)

    total = 0

    for l in lines:
        vals = [int(elt) for elt in l.split(" ")]
        lists = [vals]
        curr = vals
        # process lists until we get 0
        while curr.count(0) != len(curr):
            # get differences between each elt in list
            newList = []
            for i in range(len(curr) - 1):
                newList.append(curr[i + 1] - curr[i])
            lists.append(newList)
            curr = newList
        # extrapolate
        # each step we want to take the current lists's 1st value and subtract the previous list's 1st value from it

        ans = 0
        r = list(reversed(lists))
        for i in range(1, len(r)):
            ans = (r[i][0] - ans)-
        total += ans

    print("Total: ", total)


if __name__ == "__main__":
    main()