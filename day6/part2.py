def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    times = [t for t in lines[0][11:].split(" ") if len(t) > 0]
    distances = [d for d in lines[1][11:].split(" ") if len(d) > 0]

    time = int("".join(times))
    distance = int("".join(distances))

    total = 0
    # for idx in range(len(times)):

    # i is how many seconds to charge
    for i in range(1, time):
        speed = i
        timeLeft = time - i
        if speed * timeLeft > distance:
            total += 1

    print(total)

if __name__ == "__main__":
    main()