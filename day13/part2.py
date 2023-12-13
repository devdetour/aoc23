def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)
    
    grids = []

    currGrid = []
    for l in lines:
        if len(l) > 0:
            currGrid.append(list(l))
        else:
            grids.append(currGrid)
            currGrid = []
    
    grids.append(currGrid)

    print(grids)


    # for l in list(zip(*grids[0][::-1])):
    #     print("".join(l))
    # return

    def get_column(grid, num):
        col = []
        for r in range(len(grid)):
            col.append(grid[r][num])
        return col

    def validateGridRows(g, rowUp, rowDown):
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
                # print(f"{idx}: {a[idx]} != {b[idx]}")
                diff.append(idx)
            # never need to change more than 1
            if len(diff) > 1:
                return [1, 2]
        return diff

    def getGridScore(g, scoreIgnore=0):

        for r in range(len(g) - 1):
            # if this row starts reflection, we can add r + 1 * 100
            if validateGridRows(g, r, r + 1):
                score =  (r + 1) * 100
                if score != scoreIgnore:
                    # print(f"Grid rows good! {score}")
                    return score
 
        for c in range(len(g[0]) - 1):
            if validateGridCols(g, c, c + 1):
                score = c + 1
                if score != scoreIgnore:
                    # print(f"Grid cols good! {score}")
                # for l in g:
                #     print("".join(l))
                    return score
        return 0

    # print(getGridScore(grids[0], 100))
    # return

    # return
    total = 0

    for g in grids:
        # check rows first
        solved = False
        initialScore = getGridScore(g)
        for r in range(len(g)):
            # if this row is off by 1, try flipping that, then try validating.
            if not solved:
                for r1 in range(r + 1, len(g)):
                    if not solved:
                        diff = getDifferentIndices(g[r], g[r1])
                        if len(diff) == 1:
                            # change r at that index
                            if g[r][diff[0]] == "#":
                                g[r][diff[0]] = "." 
                            else:
                                g[r][diff[0]] = "#"

                            score = getGridScore(g, initialScore)
                            if score > 0 and score != initialScore:
                                total += score
                                solved = True
                                break

                            if g[r][diff[0]] == "#":
                                g[r][diff[0]] = "." 
                            else:
                                g[r][diff[0]] = "#"
        if solved:
            print("Solved on rows")
        
        if not solved:
            # get current row/col reflection #. can use score fn as-is
            initialScore = getGridScore(g)
            # print("Initial score:", initialScore )

            for c in range(len(g[0])):
                
                if not solved:
                    for c1 in range(c + 1, len(g[0])):
                        if not solved:
                            diff = getDifferentIndices(get_column(g, c), get_column(g, c1))
                            if len(diff) == 1:
                                if g[diff[0]][c] == "#":
                                    g[diff[0]][c] = "."
                                else:
                                    g[diff[0]][c] = "#"
                                
                                score = getGridScore(g, initialScore)
                                if score > 0 and score != initialScore:
                                    total += score
                                    solved = True
                                    print("Solved on cols")
                                    # for l in g:
                                    #     print("".join(l))
                                    break
                    
                                if g[diff[0]][c] == "#":
                                    g[diff[0]][c] = "."
                                else:
                                    g[diff[0]][c] = "#"

        if not solved:
            print("FAILED TO SOLVE GRID!")
            for l in g:
                print("".join(l))
            return
    print(total)



if __name__ == "__main__":
    main()