name = input('Enter the file name: ')
x = 0
w = 0
try:
    n = open(name)
except:
    print('Your file could not be read or found')

for i in n:
    if not i.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        x = x + 1
        j = i[20:]
        j = j.strip()
        try:
            f = float(j)
        except:
            print('Bro we mess up')
            break
        w = w + f
done = w / x
print('Average spam confidence:', done)