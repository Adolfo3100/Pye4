file = input('Enter the name of the file: ') #Use the file mbox-short.txt
mail = open(file)
r = ""
end = list()
hours = {}

for i in mail:
    if not i.startswith('From '):
        continue
    else:
        r = r + i

stuff = r.split() #Separets every sentence in pieces on every space

for j in stuff:
    if "@" in j:
        end.append(j)
        print(j)

print('There were', len(end), 'lines in the file with From as the first word')