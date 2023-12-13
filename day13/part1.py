def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)
    
    grids = []

    currGrid = []
    for l in lines:
        if len(l) > 0:
            currGrid.append(l)
        else:
            grids.append(currGrid)
            currGrid = []
    
    grids.append(currGrid)

    print(grids)

    def get_column(grid, num):
        col = []
        for r in range(len(grid)):
            col.append(grid[r][num])
        return col

    def validateGridRows(g, rowUp, rowDown):
        print(f"Checking {rowUp}, {rowDown}")
        while rowUp >= 0 and rowDown < len(g):
            if g[rowUp] != g[rowDown]:
                return False
            rowUp -= 1
            rowDown += 1
        
        return True
    
    def validateGridCols(g, colLeft, colRight):
        while colLeft >= 0 and colRight < len(g[0]):
            if get_column(g, colLeft) != get_column(g, colRight):
                return False
            colLeft -= 1
            colRight += 1
        return True

    def getDifferentIndices(a, b):
        diff = []
        for idx in range(len(a)):
            if a[idx] != b[idx]:
                diff.append(idx)
            # never need to change more than 1
            if len(diff) > 1:
                return 2
        return diff

    total = 0

    for g in grids:
        # check rows first
        solved = False
        for r in range(len(g) - 1):
            # if this row starts reflection, we can add r + 1 * 100
            if validateGridRows(g, r, r + 1):
                total += (r + 1) * 100
                solved = True
                break
        
        if not solved:
            for c in range(len(g[0]) - 1):
                if validateGridCols(g, c, c + 1):
                    total += c + 1
    

    print(total)



if __name__ == "__main__":
    main()