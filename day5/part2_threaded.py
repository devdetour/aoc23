import multiprocessing as mp



def getBestSeed(map_order, ranges, start, go):
    best = float('inf')
    print(f"Processing {go} starting from range {start}")
    for s in range(start, start + go):
        curr = s
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

def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    # part1
    # get seeds we want
    seed_ranges = []
    seeds = [int(s) for s in lines[0][len("seeds: "):].split(" ")]

    i = 0
    
    while i < len(seeds):
        seed_ranges.append([seeds[i], seeds[i + 1]])
        i += 2

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

    # i paid for 8 p-cores and dammit i'm gonna use them!
    procs = []

    # do in batches of 8 cuz that's how many cores I have
    completed = 0
    while completed < len(seed_ranges):
        currBatch = 0
        for i in range(8):
            if i >= len(seed_ranges):
                break
            s = seed_ranges[i + completed]
            p = mp.Process(target=getBestSeed, args=(map_order, ranges, s[0], s[1]))
            p.start()
            procs.append(p)
        currBatch += 8

        while len(procs) > 0:
            p = procs.pop()
            p.join()

        completed += 8



if __name__ == "__main__":
    main()