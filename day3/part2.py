def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    maxR = len(lines)
    maxC = len(lines[0])
    nums = "1234567890"

    def isAdjacent(r, c, lines):
        dirs = [
            [-1, 0], #left
            [1, 0],# right
            [0, -1],# up 
            [0, 1],# down
            [-1, -1],# up left
            [1, -1],# up right
            [-1, 1],# down left
            [1, 1],# down right
        ]
        
        adjacentGears = []

        for d in dirs:
            newR = r + d[0]
            newC = c + d[1]
            if newR >= 0 and newR < maxR and newC >= 0 and newC < maxC \
                and lines[newR][newC] == "*":
                    adjacentGears.append(f"{newR},{newC}")

        return adjacentGears

    # print(isAdjacent(0, 2, lines))        
    # part2

    # key will be (r, c)
    # value will be a list of numbers that border the gear
    gears = {}
    currNum = ""
    adjacentGears = set() # set of tuples
    for r in range(maxR):
        for c in range(maxC):
            # 2 cases: either current char is a number or it's not
            # if it is, we want to concat to currNum
            # if it's not, we want to check if current number was adjacent
                # if so, add it to sum
                # if not, discard
                #then, reset
            
            if lines[r][c] in nums:
                currNum += lines[r][c]
                for t in isAdjacent(r, c, lines):
                    adjacentGears.add(t)
            else:
                # print(f"Done with {currNum}")
                # loop thru the adjacent gears and add 1 to each in the dictionary
                for g in adjacentGears:
                    if g not in gears:
                        gears[g] = []
                    gears[g].append(int(currNum))
                    # print("Adding")
                    # total += int(currNum)
                currNum = ""
                adjacentGears = set()

    total = 0

    # loop thru gears, find ones with exactly 2 nums, add to total if 2
    for v in gears.values():
        if len(v) == 2:
            total += v[0] * v[1]
    print(total)

if __name__ == "__main__":
    main()