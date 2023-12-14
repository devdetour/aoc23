import copy
def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    # # doesn't move
    # O does but only up until the #
    def getColumn(grid, col):
        return [r[col] for r in grid]

    grid = lines

    def fillLeft(existingCol):
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

    def fillRight(existingCol):
        newCol = []

        # want to shift everything right
        # start at len(existingCol) - 1
        # track # of Os and .s
        # when we hit a "#"
        # - fill Os
        # - fill ".s"
        # - then fill #

        numPeriod = 0
        numO = 0
        for i in range(len(existingCol) - 1, -1, -1):
            if existingCol[i] == "#":
                newCol = ["O"] * numO + newCol
                newCol = ["."] * numPeriod + newCol
                newCol = ["#"] + newCol
                numO = 0
                numPeriod = 0
            elif existingCol[i] == ".":
                numPeriod += 1
            else:
                numO += 1
        # at the end we need to fill in any missing things
        newCol = ["O"] * numO + newCol
        newCol = ["."] * numPeriod + newCol
        return newCol

    # print(getColumn(grid, 7))
    # print(fillLeft(getColumn(grid, 7)))

    # rotated 90 degrees, so score is len(grid) - c, + 1?
    def getScore(grid):
        score = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "O":
                    score += len(grid) - r
        return score
    
    def fillCol(grid, col, colNum):
        for i in range(len(col)):
            grid[i][colNum] = col[i]


    def cycle(grid):
        # first check cache <= maybe do this outside

        # rotate north
        newGrid = [list(r) for r in grid]
        # for l in newGrid:
        #     print("".join(l))

        for colNum in range(len(lines)):
            newCol = fillLeft(getColumn(grid, colNum))
            # print(newCol)
            fillCol(newGrid, newCol, colNum)

        grid = newGrid
        # print("NORTH")
        # for l in grid:
        #     print("".join(l))

        newGrid = []

        # rotate west
        for row in grid:
            # reverse the row, do the thing, reverse it back
            rRow = fillLeft(row)
            newGrid.append(rRow)


        grid = newGrid
        # print("WEST")
        # for l in grid:
        #     print("".join(l))

        newGrid = [list(r) for r in grid]

        # south
        for colNum in range(len(lines)):
            newCol = fillRight(getColumn(grid, colNum))
            # print(newCol)
            fillCol(newGrid, newCol, colNum)

        grid = newGrid
        # print("SOUTH")
        # for l in grid:
        #     print("".join(l))

        newGrid = []

        for row in grid:
            # reverse the row, do the thing, reverse it back
            rRow = fillRight(row)
            newGrid.append(rRow)

        # east

        return newGrid


    # rotatedGrid = []
    # for colNum in range(len(lines)):
    #     rotatedGrid.append(fillLeft(getColumn(grid, colNum)))

    # for l in rotatedGrid:
    #     print("".join(l))

    # key is the stringified whole grid, value is the next state after cycling
    cache = {}

    # first time we hit the cache, start keeping track of what our state is
    # when we miss, reset
    # eventually, we'll have a list of the cycle, in grids. if we do some math we can figure out where
    # we end up..

    # math:
    # i iterations in, we start our cycle.
    # we finish our cycle <= need to know the cycle has ended, so check grid in path

    fullCycle = []
    path = []

    for i in range(1000000000):
        if i % 1000 == 0:
            print("Done", i)
        grid = cycle(grid)

        key = "".join(["".join(r) for r in grid])
        # print(key)
        if key in cache:
            grid = copy.deepcopy(cache[key])
            if key in path:
                fullCycle = path
                break
            else:
                path.append(key)
            continue
        else:
            # print("Cache miss")
            path = []
            grid = cycle(grid)
            cache[key] = grid

    print(f"Full cycle found after {i} runs: {len(fullCycle)}")

    finalGridKey = (1000000000 - i + 3) % len(fullCycle) # you know what they say, 3 is the magic number
    grid = cache[fullCycle[finalGridKey]]

    for l in grid:
        print("".join(l))

    print(getScore(grid))




if __name__ == "__main__":
    main()