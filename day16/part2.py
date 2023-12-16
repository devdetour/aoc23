from collections import deque

def main():
    with open("input.txt", "r") as f:
        lines = [list(l.strip()) for l in f.readlines()]
        # print(lines)

    for l in lines:
        print("".join(l))

    # start from top left going

    # keep track of direction
    
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

    # for \
    # which way we are GOING when we hit the backslash
    backSlashDirections = {
        RIGHT: DOWN, # > \,
        LEFT: UP,
        UP: LEFT,
        DOWN: RIGHT
    }

    # for /
    forwardSlashDirections = {
        RIGHT: UP, # > /
        LEFT: DOWN,
        UP: RIGHT,
        DOWN: LEFT
    }

    grid = lines
    
    def getScore(q):
        visitedDir = {}

        while len(q) > 0:
            curr = q.pop()
            r, c, direction = curr

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                continue

            if (r, c) not in visitedDir:
                visitedDir[(r, c)] = []

            if direction in visitedDir[(r, c)]:
                continue

            visitedDir[(r, c)].append(direction)

            if grid[r][c] == "/" and (r, c):
                direction = forwardSlashDirections[direction]
                q.append((r + direction[0], c + direction[1], direction))

            elif grid[r][c] == '\\' and (r, c):
                direction = backSlashDirections[direction]
                q.append((r + direction[0], c + direction[1], direction))
            
            # handle |
            elif grid[r][c] == "|" and direction in (LEFT, RIGHT) and (r, c):
                q.append((r + UP[0], c + UP[1], UP))
                q.append((r + DOWN[0], c + DOWN[1], DOWN))

            # handle -
            elif grid[r][c] == "-" and direction in (UP, DOWN) and (r, c):
                q.append((r + LEFT[0], c + LEFT[1], LEFT))
                q.append((r + RIGHT[0], c + RIGHT[1], RIGHT))

            else:
                q.append((r + direction[0], c + direction[1], direction))
        
        return len(visitedDir)


    best = 0

    # try top & bottom
    for c in range(len(grid[0])):
        best = max(best, getScore([(0, c, DOWN)]))
        best = max(best, getScore([(len(grid) - 1, c, UP)]))
    # try sides
    for r in range(len(grid)):
        best = max(best, getScore([(r, 0, RIGHT)]))
        best = max(best, getScore([(r, len(grid[0]) - 1, LEFT)]))

    print(best)




if __name__ == "__main__":
    main()