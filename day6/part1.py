def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    times = [int(t) for t in lines[0][11:].split(" ") if len(t) > 0]
    distances = [int(d) for d in lines[1][11:].split(" ") if len(d) > 0]

    print(times)
    print(distances)

    # check how many ways we can win.

    # option to hold for x seconds, then move for times - x seconds

    # start at the middle, then increase & decrease times until we can't win anymore, then we know how many we can win

    # how do we tell if we can win?
    # speed * timeLeft > distance

    total = 0
    for idx in range(len(times)):
        waysToWin = 0

        time = times[idx]
        distance = distances[idx]

        # i is how many seconds to charge
        for i in range(1, time):
            speed = i
            timeLeft = time - i
            if speed * timeLeft > distance:
                waysToWin += 1
    
        if total == 0:
            total = waysToWin
        else:
            total *= waysToWin

    print(total)

if __name__ == "__main__":
    main()