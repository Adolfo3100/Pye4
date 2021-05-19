file = input('Enter name file: ')
text = open(file)
final = list()
words = ""

for i in text:
    words = words + i

maybe = words.split()

for j in maybe:
    if j not in final:
        final.append(j)
    else:
        continue
final.sort()
print(final)