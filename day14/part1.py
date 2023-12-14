def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    # # doesn't move
    # O does but only up until the #

    def getColumn(grid, col):
        return [r[col] for r in grid]

    grid = lines

    def buildColumn(existingCol):
        newCol = []

        numPeriod = 0
        numO = 0
        for i in range(len(existingCol)):
            if existingCol[i] == "#":
                newCol += ["O"] * numO
                newCol += ["."] * numPeriod
                numO = 0
                numPeriod = 0
                newCol.append("#")
            elif existingCol[i] == ".":
                numPeriod += 1
            else:
                numO += 1
        # at the end we need to fill in any missing things
        newCol += ["O"] * numO
        newCol += ["."] * numPeriod
        return newCol

    # print(getColumn(grid, 7))
    # print(buildColumn(getColumn(grid, 7)))

    # rotated 90 degrees, so score is len(grid) - c, + 1?
    def getScore(grid):
        score = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "O":
                    score += len(grid[0]) - c
        return score


    rotatedGrid = []
    for colNum in range(len(lines)):
        rotatedGrid.append(buildColumn(getColumn(grid, colNum)))

    for l in rotatedGrid:
        print("".join(l))
    
    print(getScore(rotatedGrid))



if __name__ == "__main__":
    main()