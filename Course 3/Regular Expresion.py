file = open('RegularExpresion.txt')
import re

suma = list()
for line in file:
    line = line.rstrip()
    stuff = re.findall("[0-9]+\s?", line)
    j = len(stuff)
    for i in range(j):
        number = int(stuff[i])
        suma.append(number)

print(sum(suma))