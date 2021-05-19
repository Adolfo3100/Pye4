file = input('Enter the name of the file: ') #Use the file mbox-short.txt
mail = open(file)
r = ""
numbers = {}
w=""
k=0

for i in mail:
    if not i.startswith('From '):
        continue
    else:
        r = r + i

stuff = r.split() #Separets every sentence in pieces on every space

for j in stuff: #Selects the strings where there are :
    if (':') in j:
        w = w + j + ":"
        
        
time = w.split(":") #Separates the numbers where there are :
x=len(time)

for p in time: #Take de firts number and ands it to a dictionary
    if k == 0 or k%3 == 0:
        if k == (x-1):
            continue
        else:
            numbers[p] = numbers.get(p, 0) + 1
    k = k + 1

#reverse the order of values and puts them into a list
final= sorted( [ (k,v) for k,v in numbers.items()]) 

for w,q in final:
    print(w,q)
