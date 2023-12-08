# NAIVE, brute force solution, don't use if you want to be done in any reasonable amt of time
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

    while not isDone(nodes):
        # do directions again and again
        totalSteps += 1

        for i in range(len(nodes)):
            direction = directions[idx]
            if direction == "L":
                nodes[i] = nodesDict[nodes[i]].left
            else:
                nodes[i] = nodesDict[nodes[i]].right
        
        idx += 1
        idx %= len(directions)

    print(totalSteps)


if __name__ == "__main__":
    main()