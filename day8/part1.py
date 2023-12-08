class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    nodes = {}

    n = Node(1, 2, 3)

    directions = lines[0]

    for l in lines[2:]:
        # build nodes
        val = l.split("=")[0].strip() # AAA = (BBB, CCC)
        dirs = l.split("=")[1].replace(")", "").replace("(", "").split(", ")
        left = dirs[0].strip()
        right = dirs[1].strip()

        n = Node(val, left, right)
        nodes[val] = n

    # print(nodes)

    curr = "AAA"
    totalSteps = 0
    idx = 0
    while curr != "ZZZ":
        # do directions again and again
        totalSteps += 1

        direction = directions[idx]
        if direction == "L":
            curr = nodes[curr].left
        else:
            curr = nodes[curr].right
        
        idx += 1
        idx %= len(directions)

    print(totalSteps)


if __name__ == "__main__":
    main()