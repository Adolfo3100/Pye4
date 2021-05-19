largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    try:
        num = int(num)
    except:
        if num == 'done':
            print('Maximum is',largest)
            print('Minimum is', smallest)
            break
        else:
            print('Invalid input')
            continue
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest =  num


