from collections import deque
def main():
    with open("input.txt", "r") as f:
        lines = [list(l.strip()) for l in f.readlines()]
        # print(lines)
    
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] + p2[1])

    def get_column(grid, num):
        col = []
        for r in range(len(grid)):
            col.append(grid[r][num])
        return col

    rowsExpanded = []
    # expand rows first
    for l in lines:
        rowsExpanded.append(l)
        if "#" not in l:
            rowsExpanded.append(l)


    # expand columns
    # go thru the whole grid, at each step if a certain column doesn't have a galaxy, add an extra space
    finalGrid = []
    for r in range(len(rowsExpanded)):
        currRow = []
        for c in range(len(rowsExpanded[0])):
            currRow.append(rowsExpanded[r][c])
            if "#" not in get_column(rowsExpanded, c):
                currRow.append(rowsExpanded[r][c])
        finalGrid.append(currRow)

    galaxies = []
    for r in range(len(finalGrid)):
        for c in range(len(finalGrid[0])):
            if finalGrid[r][c] == "#":
                galaxies.append((r, c))

    for line in finalGrid:
        s = "".join(line)
        print(s)


    # now get distances between galaxies
    totalDist = 0
    combos = set()
    for i in range(len(galaxies)):
        # compare to all the others
        for j in range(len(galaxies)):
            if i == j:
                continue
            # get key for combos
            keyArr = sorted([i, j])
            key = (keyArr[0], keyArr[1])
            if key in combos:
                continue
            else:
                combos.add(key)
                dist = manhattan_distance(galaxies[i], galaxies[j])
                print(f"Distance between {i + 1} and {j}: {dist}")
                totalDist += dist

    print(totalDist)




if __name__ == "__main__":
    main()