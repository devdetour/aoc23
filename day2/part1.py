def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    # part1
    lines = [l[l.index(": ") + 1:].strip() for l in lines]

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    valid_line_sum = 0

    for idx in range(len(lines)):
        l = lines[idx]
        # split on semicolon to get the handfuls
        handfuls = l.split(";")

        valid = True
        for h in handfuls:
            if not valid:
                break

            cubes = [c.strip() for c in h.split(",")]
        
            # check r, g, b
            for c in cubes:
                num = int(c.split(" ")[0])
                color = c.split(" ")[1]
                # check our dict with max cubes
                if num > max_cubes[color]:
                    valid = False
                    break

        if valid: 
            valid_line_sum += idx + 1
    
    print(valid_line_sum)



if __name__ == "__main__":
    main()