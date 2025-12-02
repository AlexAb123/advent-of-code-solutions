lines = open('Python/Advent_of_Code/AOC2023/day 7 input.txt', 'r').read().strip().split("\n")
cards = [[line.split(" ")[0], int(line.split(" ")[1])] for line in lines]

def countDupe(letter, string):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count
def processCard(card, bid):
    dupes = []
    checked = set()
    for cha in card:
        if cha not in checked:
            dupes.append(countDupe(cha, card))
            checked.add(cha)
    ones = countDupe(1, dupes)
    twos = countDupe(2, dupes)
    threes = countDupe(3, dupes)
    fours = countDupe(4, dupes)
    fives = countDupe(5, dupes)
    if ones == 5:
        return (originalCard, bid, 0)
    if twos == 1 and ones == 3:
       return (originalCard, bid, 1)
    if twos == 2 and ones == 1:
        return (originalCard, bid, 2)
    if threes == 1 and ones == 2:
        return (originalCard, bid, 3)
    if threes == 1 and twos == 1:
        return (originalCard, bid, 4)
    if fours == 1 and ones == 1:
        return (originalCard, bid, 5)
    if fives == 1:
        return (originalCard, bid, 6)

cardRankings1 = []
cardRankings2 = []

for card, bid in cards:

    originalCard = card

    #Can initially set mostCommon to anything, just can't be an empty string
    mostCommon = [0, "J"]
    for cha in card:
        if cha != "J":
            count = countDupe(cha, card)
            if count > mostCommon[0]:
                mostCommon = [count, cha]
    newCard = ""
    for cha in card:
        if cha == "J":
            newCard += mostCommon[1]
        else:
            newCard += cha
            
    cardRankings1.append(processCard(card, bid))
    cardRankings2.append(processCard(newCard, bid))

def sort(lst, values):
    for i in range(len(lst)):
        swaps = 0
        for j in range(len(lst)-1):
            if lst[j][2] > lst[j+1][2]:
                swaps += 1
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
            elif lst[j][2] == lst[j+1][2]:
                isSorted = False
                for cha in range(len(lst[j][0])):
                    if not isSorted and values.index(lst[j][0][cha]) != values.index(lst[j+1][0][cha]):
                        if values.index(lst[j][0][cha]) > values.index(lst[j+1][0][cha]):
                            swaps += 1
                            temp = lst[j]
                            lst[j] = lst[j+1]
                            lst[j+1] = temp
                            isSorted = True
                        else:
                            isSorted = True
        if swaps == 0:
            return lst
    return lst

part1Values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
part2Values = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]

cardRankings1 = sort(cardRankings1, part1Values)
cardRankings2 = sort(cardRankings2, part2Values)

part1Score = 0
part2Score = 0

for i in range(len(cards)):
    part1Score += (i+1) * cardRankings1[i][1]
    part2Score += (i+1) * cardRankings2[i][1]

print(f"Part 1: {part1Score}")
print(f"Part 2: {part2Score}")