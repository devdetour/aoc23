# This one got me, I had to look it up. solution adapted from elements of AOC subreddit and HyperNeutrino on YT (great explanation, thanks!)
from functools import cache
def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    @cache
    def backtrack(springs, groups):
        # if we run out of springs AND groups, valid
        if len(springs) == 0:
            if len(groups) == 0:
                return 1
            return 0
        
        # if we run out of groups and there are no broken springs left, valid
        if len(groups) == 0:
            if "#" not in springs:
                return 1
            return 0

        total = 0

        curr = springs[0]

        # start a new group of springs
        if curr in ".?":
            total += backtrack(springs[1:], groups)

        # continue current group of springs
        if curr in "#?":
            # not valid if string is too short to have right num of #s for current group
            if len(springs) < groups[0]:
                pass
            # not valid if there is a . in the next groups[0] (we need a contiguous block at least that long for it to be valid)
            elif "." in springs[:groups[0]]:
                pass
            # need to have a . or a ? immediately after the next group, or end of line, invalid if not
            elif len(springs) > groups[0] and springs[groups[0]] == "#":
                pass
            # otherwise, we can keep going
            else:
                total += backtrack(springs[groups[0] + 1:], groups[1:])


        return total

    total = 0
    for l in lines:
        springs = l.split(" ")[0]
        springs = (springs + "?") * 5
        springs = springs[:-1]

        groups = [int(n) for n in l.split(" ")[1].split(",")] * 5
        
        total += backtrack(springs, tuple(groups))
    
    print(total)
    # start by lining up # of springs we know about

if __name__ == "__main__":
    main()