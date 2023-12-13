from collections import deque
def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)
    
    #
    def getGroups(s):
        groups = []
        currSize = 0
        for c in s:
            if c == "." and currSize > 0:
                groups.append(currSize)
                currSize = 0
            elif c == "#":
                currSize += 1
        if currSize > 0:
            groups.append(currSize)
        return groups
    
    # print(getGroups("#.#.###"))
    # print(getGroups("####.#...#..."))

    total = 0
    # try out different combinations, until we find a valid one
    def backtrack(s, groups):
        nonlocal total
        if "?" not in s:
            if getGroups(s) == groups:
                total += 1
            return

        # change a thing
        period = s.replace("?", ".", 1)
        pound = s.replace("?", "#", 1)

        # backtrack
        backtrack(period, groups)
        backtrack(pound, groups)
        
        # undo the thing ?? do we need to???

    for l in lines:
        springs = l.split(" ")[0]
        groups = [int(n) for n in l.split(" ")[1].split(",")]
        
        backtrack(l, groups)
        # some loop that tries all the permutations, and if groups == getGroups(s), add to total
        # print(springs, groups)
    
    print(total)
    # start by lining up # of springs we know about

if __name__ == "__main__":
    main()