text = input('Enter the fiel name: ')
if len(text) < 1 : text = "mbox-short.txt"
handle = open(text)
r=""
final={}

#Gets the lines where there are emails from the file
for i in handle:
    if not i.startswith('From '):
        continue
    else:
        r = r + i

stuff = r.split()
lis=[]

#Gets the emails into a list
for j in stuff:
    if "@" in j:
        lis.append(j)

# Gets the emails into a dictionary
for mai in lis:
    final[mai] = final.get(mai, 0) + 1

name = None
times = None

#Checks which email wrote more emails
for email, number in final.items():
    if times is None or number > times:
        name = email
        times = number

print(name, times)

