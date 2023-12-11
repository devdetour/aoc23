from collections import deque
def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)
    
    grid = lines

    # just some variables
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    stringDirs = ["left", "right", "up", "down"]
    # transformations for direction we came from
    UP_DIR = (1, 0)
    DOWN_DIR = (-1, 0)
    RIGHT_DIR = (0, -1)
    LEFT_DIR = (0, 1)
    # . . .
    # . . .
    # . . .

    # all the directions we can go when we reach a character.
    directions = {
        "|": [None, None, (1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1), None, None],
        "L": [None, (-1, 0), (0, 1), None],
        "J": [(-1, 0), None, (0, -1), None],
        "7": [(1, 0), None, None, (0, -1)],
        "F": [None, (1, 0), None, (0, 1)]
    }

    seenCoords = set()

    q = deque()
    maxLength = 0

    class Pos():
        def __init__(self, prevCoord, pathLength, r, c):
            self.prevCoord = prevCoord
            self.pathLength = pathLength
            self.r = r
            self.c = c

    # once we have grid, expand it so we can reach interior not strictly enclosed by loop
    newGrid = []
    # add rows between each row
    for r in grid:
        newGrid.append(list(r))
        addRow = []
        for char in r:
            # if we have a character that goes DOWN, "7", "F", "|", add pipe
            if char in "F7|S":
                addRow.append("|")
            else:
                addRow.append("X")
        newGrid.append(addRow)

    newNewGrid = []
    # first add an empty row to top
    firstRow = ["X"] * (len(newGrid[0]) * 2 + 1)
    newNewGrid.append(firstRow)
    for r in range(len(newGrid)):
        currRow = ["X"]
        for c in range(len(newGrid[0])):
            # add current, then add new
            currRow.append(newGrid[r][c])
            if newGrid[r][c] in "FL-S":
                currRow.append("-")
            else:
                currRow.append("X")
        newNewGrid.append(currRow)

    grid = newNewGrid

    gridCopy = [l for l in grid]

    # loop thru til we find s
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                # check if we can get there from here
                # right
                if grid[r][c + 1] in "-J7":
                    q.append(Pos((r, c), 0, r, c + 1)) # right
                # left
                if grid[r][c - 1] in "FL-":
                    q.append(Pos((r, c), 0, r, c - 1)) # left
                # up
                if grid[r - 1][c] in "F7|":
                    q.append(Pos((r, c), 0, r - 1, c)) # up
                # down
                if grid[r + 1][c] in "JL|":
                    q.append(Pos((r, c), 0, r + 1, c)) # down

    while len(q) > 0:
        curr = q.popleft()

        # check in bounds
        if curr.r < 0 or curr.r > len(grid) - 1 or curr.c < 0 or curr.c > len(grid[0]) - 1 \
            or grid[curr.r][curr.c] not in directions or (curr.r, curr.c) in seenCoords:
            maxLength = max(maxLength, curr.pathLength)
            continue
        
        seenCoords.add((curr.r, curr.c))

        # otherwise, figure out where to go next and add to q
        directionFrom = (curr.r - curr.prevCoord[0], curr.c - curr.prevCoord[1])
        # print(f"Dirfrom: {directionFrom}")

        if directionFrom == UP_DIR:
            idx_to_check = UP
        elif directionFrom == DOWN_DIR:
            idx_to_check = DOWN
        elif directionFrom == RIGHT_DIR:
            idx_to_check = RIGHT
        elif directionFrom == LEFT_DIR:
            idx_to_check = LEFT

        # print(f"Current: {grid[curr.r][curr.c]}")
        # print(f"Coming from: {stringDirs[idx_to_check]}")

        # check if we can go somewhere else from current one given that's where we came from
        nextDir = directions[grid[curr.r][curr.c]][idx_to_check]
        # print(f"Going to: {nextDir}")

        # print("\n")
        if nextDir != None:
            gridCopy[curr.r][curr.c] = "0"
            q.append(Pos((curr.r, curr.c), curr.pathLength + 1, curr.r + nextDir[0], curr.c + nextDir[1]))

    with open("out.txt", 'w') as f:
        newCopy = ["".join(l) + "\n" for l in gridCopy]
        f.writelines(newCopy)

    # start at 0, 0
    # just turn everything into 1 until we hit 0

    seen = set()

    q.append((148, 137))
    # q.append((1, len(grid) - 1))
    # q.append((len(grid) - 1, len(grid[0]) - 1))

    while(len(q) > 0):
        curr = q.popleft()
        if curr[0] < 0 or curr[0] > len(gridCopy) - 1 or curr[1] < 0 or curr[1] > len(gridCopy[0]) - 1 \
            or curr in seen or gridCopy[curr[0]][curr[1]] in "0S":
            continue
        seen.add(curr)

        # set to I if inside
        gridCopy[curr[0]][curr[1]] = "I"

        q.append((curr[0] + 1, curr[1]))
        q.append((curr[0] - 1, curr[1]))
        q.append((curr[0], curr[1] + 1))
        q.append((curr[0], curr[1] - 1))
        # check all neighbors
    
    for l in gridCopy:
        print("".join(l))


    # shrink grid again
    finalGrid = []
    for r in range(1, len(gridCopy), 2):
        row = []
        for c in range(1, len(gridCopy[0]), 2):
            row.append(gridCopy[r][c])

        finalGrid.append(row)

    s = ""
    with open("out2.txt", 'w') as f:
        for l in finalGrid:
            currrow= "".join(l)
            f.write(currrow)
            s += currrow
            f.write("\n")

    print(s.count("I"))

    # total = 0
    # for r in range(len(finalGrid)):
    #     for c in range(len(finalGrid[0])):
    #         # odd column index == not part of original
    #         # odd row index == not part of original
    #         if finalGrid[r][c] not in "X0S":
    #             # print(f"Adding {gridCopy[r][c]}, {r}, {c}")
    #             total += 1

    # print(total)
    

if __name__ == "__main__":
    main()