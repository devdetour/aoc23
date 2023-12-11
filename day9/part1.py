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
        # each list's last value is the last value from the previous list
        # + the last value from the current list.
        ans = 0
        for sublist in lists[1:]:
            ans += sublist[-1]
        
        # get NEXT element of initial list by getting last value of first list + ans
        print(ans + lists[0][-1])
        total += ans + lists[0][-1]

    print("Total: ", total)



if __name__ == "__main__":
    main()