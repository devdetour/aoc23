def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    # part1
    # get seeds we want

    seeds = [int(s) for s in lines[0][len("seeds: "):].split(" ")]
    # print(seeds)

    map_order = []

    ranges = {}

    current_ranges = []
    map_name = "seed-to-soil"
    for idx in range(3, len(lines)):
        l = lines[idx]
        if len(l) <= 0:
            continue
        if "-to-" in l:
            ranges[map_name] = current_ranges
            map_order.append(map_name)
            map_name = l.split(" ")[0]
            current_ranges = []
        else:
            nums = l.split(" ")
            current_ranges.append([int(n) for n in nums])

    ranges[map_name] = current_ranges
    map_order.append(map_name)

    print(ranges)
    
    best = float('inf')

    for s in seeds:
        curr = s
        path = [curr]
        for m in map_order:
            # check if this is in a special range
            for r in ranges[m]:
                # see if the seed is in source + length
                if curr >= r[1] and curr <= (r[1] + r[2] - 1):
                    curr += (r[0] - r[1])
                    break
            # path.append(curr)
        
            # print(f"curr after {m}: {curr}")
        
        best = min(best, curr)
        # print(path)
        path = []

    print(best)



if __name__ == "__main__":
    main()