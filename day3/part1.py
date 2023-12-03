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
        
        for d in dirs:
            newR = r + d[0]
            newC = c + d[1]
            if newR >= 0 and newR < maxR and newC >= 0 and newC < maxC \
                and lines[newR][newC] not in nums and lines[newR][newC] != ".":
                    return True

        return False

    # print(isAdjacent(0, 2, lines))        
    # part1
    total = 0
    currNum = ""
    numAdjacent = False
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
                numAdjacent = numAdjacent or isAdjacent(r, c, lines)
            else:
                # print(f"Done with {currNum}")
                if numAdjacent:
                    # print("Adding")
                    total += int(currNum)
                currNum = ""
                numAdjacent = False
    print(total)


if __name__ == "__main__":
    main()