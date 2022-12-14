print(ord("a"))
fr = open("data/advent3", "r")
total = 0
for row in fr.readlines():
    temp = row.strip()
    firstHalf = set(temp[:len(temp)/2])
    secondHalf = set(temp[len(temp)/2:])
    char = str(firstHalf.intersection(secondHalf))
    total += char.islower() *
