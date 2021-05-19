name = input('Enter de file name: ')
try:
    n = open(name)
except:
    print("The file name you enter might be wrong")
    quit()
for i in n:
    i = i.rstrip()
    i = i.upper()
    print(i)


