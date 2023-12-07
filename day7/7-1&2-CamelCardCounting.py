from collections import Counter

def convert(h):
    hand = []
    for c in h:
        if c == 'A':
            hand.append(13)
        elif c == 'K':
            hand.append(12)
        elif c == 'Q':
            hand.append(11)
        elif c == 'T':
            hand.append(10)
        elif c == 'J':
            hand.append(0)
        else:
            hand.append(int(c))
    return hand

lines = []
with open("day7/day7", 'r') as f:
    lines = f.readlines()

hands = []
sum = 0
for l in lines:
    hand, bid = l.split()
    hand = convert(hand)
    bid = int(bid)
    
    c = Counter(hand)
    if 0 in c:
        most_common = c.most_common()
        if most_common[0][0] == 0:
            if len(most_common) == 1:
                mc = most_common[0][0]
            else:
                mc = most_common[1][0]
                c[mc] += c[0]
                c[0] = 0
        else:
            mc = most_common[0][0]
            c[mc] += c[0]
            c[0] = 0
    
    c = list(c.values())
    if 5 in c:
        hands.append((6, hand, bid))
    elif 4 in c:
        hands.append((5, hand, bid))
    elif 3 in c and 2 in c:
        hands.append((4, hand, bid))
    elif 3 in c:
        hands.append((3, hand, bid))
    elif 2 in c and c.count(2) == 2:
        hands.append((2, hand, bid))
    elif 2 in c:
        hands.append((1, hand, bid))
    else:
        hands.append((0, hand, bid))

hands.sort(reverse=True)
for i in range(len(hands)):
    x = len(hands) - i
    sum += x * hands[i][2]

print(sum)