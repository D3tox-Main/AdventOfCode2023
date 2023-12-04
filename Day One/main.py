import os

with open(os.path.join("Day One","calibrationValues.txt")) as f:
    file = [line.rstrip() for line in f]

total = []
numbers = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5) , ("six", 6), ("seven", 7), ("eight", 8) , ("nine", 9)]


def findFirstNum(line):
    numFound = []

    for word, digit in numbers:
        start_pos = 0
        while True:
            pos = line.find(word, start_pos)
            if pos == -1:
                break
            numFound.append((int(digit), pos))
            start_pos = pos + 1

    for i in range(len(line)):
        if line[i].isdigit():
            numFound.append((int(line[i]), i))

    sortedList = sorted(numFound, key=lambda tup: tup[1])


    return sortedList[0][0]
   
       


def findLastNum(line):
    numFound = []

    for word, digit in numbers:
        start_pos = 0
        while True:
            pos = line.find(word, start_pos)
            if pos == -1:
                break
            numFound.append((int(digit), pos))
            start_pos = pos + 1

    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            numFound.append((int(line[i]), i))

    sortedList = sorted(numFound, key=lambda tup: tup[1], reverse=True)

    return sortedList[0][0]

for count, line in enumerate(file):
    number = ''
   

    number += str(findFirstNum(line))

    number += str(findLastNum(line))

    total.append(int(number))

print(sum(total))