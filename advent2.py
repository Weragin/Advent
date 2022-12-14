points = {"A X\n": 3, "A Y\n": 4, "A Z\n": 8, "B X\n": 1, "B Y\n": 5,
          "B Z\n": 9, "C X\n": 2, "C Y\n": 6, "C Z\n": 7}
total = 0
fr = open("data/advent2", "r")
for row in fr.readlines():
    temp = row
    total += points[temp]
print(total)
