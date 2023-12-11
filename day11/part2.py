from collections import deque
def main():
    with open("input.txt", "r") as f:
        lines = [list(l.strip()) for l in f.readlines()]
    
    def distance(emptyRows, emptyCols, p1, p2):
        scaleFactor = 1000000
        dist = 0

        # do row first
        rows = sorted([p1[0], p2[0]])
        start = rows[0] + 1
        end = rows[1]
        
        while start <= end:
            if start in emptyRows:
                dist += scaleFactor
            else:
                dist += 1
            start += 1

        cols = sorted([p1[1], p2[1]])
        start = cols[0] + 1
        end = cols[1]
        while start <= end:
            if start in emptyCols:
                dist += scaleFactor
            else:
                dist += 1
            start += 1

        return dist

    def get_column(grid, num):
        col = []
        for r in range(len(grid)):
            col.append(grid[r][num])
        return col

    emptyRows = []
    # expand rows first
    for idx in range(len(lines)):
        if "#" not in lines[idx]:
            emptyRows.append(idx)

    emptyCols = []
    for c in range(len(lines[0])):
        if "#" not in get_column(lines, c):
            emptyCols.append(c)

    galaxies = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "#":
                galaxies.append((r, c))

    for line in lines:
        s = "".join(line)
        print(s)


    # # now get distances between galaxies
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
                dist = distance(emptyRows, emptyCols, galaxies[i], galaxies[j])
                totalDist += dist
                
    print(totalDist)

if __name__ == "__main__":
    main()