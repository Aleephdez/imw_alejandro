import math
import sys

quantity = int(sys.argv[1])

if quantity >= 50:
    
    fifty_bill = math.trunc(quantity/50)
    quantity %= 50
    if fifty_bill == 1:
        print(fifty_bill, 'billete de 50€')
    else:
        print(fifty_bill, 'billetes de 50€')
    
if quantity >= 20:

    twenty_bill = math.trunc(quantity/20)
    quantity %= 20
    if twenty_bill == 1:
        print(twenty_bill, 'billete de 20€')
    else:
        print(twenty_bill, 'billetes de 20€')

if quantity >= 10:
    
    ten_bill = math.trunc(quantity/10)
    quantity %=10
    if ten_bill == 1:
        print(ten_bill, 'billete de 10€')
    else:
        print(ten_bill, 'billetes de 10€')

if quantity >= 5:

    five_bill = math.trunc(quantity/5)
    quantity %=5
    if five_bill == 1:
        print(five_bill, 'billete de 5€')
    else:
        print(five_bill, 'billetes de 5€')

if quantity >= 2:

    two_coin = math.trunc(quantity/2)
    quantity %=2
    if two_coin == 1:
        print(two_coin, 'moneda de 2€')
    else:
        print(two_coin, 'monedas de 2€')

if quantity >= 1:

    one_coin = math.trunc(quantity/1)
    if one_coin == 1:
        print(one_coin, 'moneda de 1€')
    else:
        print(one_coin, 'monedas de 1€')

