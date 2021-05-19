hrs = input('Enter hours:')
hrs = float(hrs)
rate = input('Enter rate:')
rate = float(rate)
if hrs <= 40:
    pay = hrs * rate
    print(pay)
else:
    extra = hrs - 40
    pay = 40 * rate
    rate = rate * 1.5
    bonus = extra * rate
    superpay = pay + bonus
    print(superpay)

