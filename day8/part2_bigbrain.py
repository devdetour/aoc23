import math

class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def isDone(ls):
    for elt in ls:
        if not elt.endswith("Z"):
            return False
        
    return True


def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    nodesDict = {}

    n = Node(1, 2, 3)

    directions = lines[0]

    for l in lines[2:]:
        # build nodes
        val = l.split("=")[0].strip() # AAA = (BBB, CCC)
        dirs = l.split("=")[1].replace(")", "").replace("(", "").split(", ")
        left = dirs[0].strip()
        right = dirs[1].strip()

        n = Node(val, left, right)
        nodesDict[val] = n

    # print(nodes)

    # curr = "AAA"
    totalSteps = 0
    idx = 0

    nodes = [n for n in nodesDict if n.endswith("A")]
    steps = []

    for n in nodes:
        # do directions again and again
        totalSteps = 0

        curr = n
        while not curr.endswith("Z"):
            totalSteps += 1

            direction = directions[idx]
            if direction == "L":
                curr = nodesDict[curr].left
            else:
                curr = nodesDict[curr].right
            
            idx += 1
            idx %= len(directions)
        steps.append(totalSteps)
        
    print(steps)

    # some math
    sol = 1
    for s in steps:
        sol *= s
    
    print(sol)
    print(math.lcm(*steps))



if __name__ == "__main__":
    main()