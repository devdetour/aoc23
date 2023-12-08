from functools import cmp_to_key

from enum import Enum

class HandType(Enum):
    HIGHCARD = 1
    PAIR = 2
    TWOPAIR = 3
    THREEOFKIND = 4
    FULLHOUSE = 5    
    FOUROFKIND = 6
    FIVEOFKIND = 7

def getHandType(h):
    
    # 4 of a kind
    def fourOfKind(h):
        return h.count(h[0]) == 4 or h.count(h[1]) == 4

    # Fullhouse
    def fullHouse(h):
        return len(set(h)) == 2 and threeOfKind(h)

    # 3 of a kind
    def threeOfKind(h):
        return h.count(h[0]) == 3 or h.count(h[1]) == 3 or h.count(h[2]) == 3

    # two pair
    def twoPair(h):
        return len(set(h)) == 3 and not threeOfKind(h)

    # pair
    def pair(h):
        s = set(h)
        return len(s) == 4

    # 5 of a kind
    def fiveOfKind(h):
        return h.count(h[0]) == 5

    # do all the checks
    if fiveOfKind(h):
        return 7 # HandType.FIVEOFKIND
    if fourOfKind(h):
        return 6 # HandType.FOUROFKIND
    if fullHouse(h):
        return 5 #HandType.FULLHOUSE
    if threeOfKind(h):
        return 4 #HandType.THREEOFKIND
    if twoPair(h):
        return 3 #HandType.TWOPAIR
    if pair(h):
        return 2 #HandType.PAIR
    return 1 #HandType.HIGHCARD    

# break tie for hands with same level
def breakTie(a, b):
    values = {
        "A": 15,
        "K": 14,
        "Q": 13,
        "J": 1,
        "T": 11,
    }

    for i in range(len(a)):
        # compare a & b
        aval = a[i]
        bval = b[i]
        if not aval.isdigit():
            aval = values[aval]
        else:
            aval = int(aval)

        if not bval.isdigit():
            bval = values[bval]
        else:
            bval = int(bval)
        
        if aval < bval:
            return -1
        elif aval > bval:
            return 1
    return 0

# item1 < means -1
def compare(item1, item2):
    best_score1 = getHandType(item1)
    best_score2 = getHandType(item2)

    for c in "AKQJT98765432":
        curr1 = getHandType(item1.replace("J", c))
        curr2 = getHandType(item2.replace("J", c))

        if curr1 > best_score1:
            best_score1 = curr1

        if curr2 > best_score2:
            best_score2 = curr2

    if best_score1 < best_score2:
        return -1
    elif best_score1 > best_score2:
        return 1
    return breakTie(item1, item2)

def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        # print(lines)

    # part1
    hands = []
    bets = {}

    for l in lines:
        vals = l.split(" ")
        hands.append(vals[0])
        bets[vals[0]] = vals[1]
    # print(hands)
    # print(bets)
    
    s = sorted(hands, key=cmp_to_key(compare))

    score = 0

    for i in range(len(s)):
        score += (i + 1) * int(bets[s[i]] )
    print(score)


if __name__ == "__main__":
    main()