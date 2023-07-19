# Advent of Code Day 3 part 2
from string import ascii_letters

with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

    
sum = 0

for i in range(0, len(data), 3):
    entry = [data[i], data[i+1], data[i+2]]
    for value, character in enumerate(ascii_letters):
        if character in entry[0] and character in entry[1] and character in entry[2]:
            sum += value + 1


print(sum)