def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    # part2
    lines = [l[l.index(": ") + 1:].strip() for l in lines]

    power_sum = 0

    for idx in range(len(lines)):
        l = lines[idx]
        # split on semicolon to get the handfuls
        handfuls = l.split(";")

        maxs = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        for h in handfuls:
            cubes = [c.strip() for c in h.split(",")]
        
            # check r, g, b
            for c in cubes:
                num = int(c.split(" ")[0])
                color = c.split(" ")[1]
                # check our dict with max cubes
                maxs[color] = max(maxs[color], num)

        power = 1
        for val in maxs.values():
            power *= val
        
        power_sum += power
    
    print(power_sum)

if __name__ == "__main__":
    main()