import string
import math

def zeros(max_plus):
    plus = 2**max_plus
    print 'zeros', plus
    return plus

def stones(max_plus):
    total =(zeros(max_plus)/2)*(max_plus-1)
    print 'stones', total
    total += max_plus
    return total

def price(max_plus, zero_price, stone_price):
    price2 = (zeros(max_plus) * zero_price) + (stones(max_plus) * stone_price)
    print 'price', price2
    return price2 

def worthit(max_plus, zero_price, stone_price, plus_price):
    cost = price(max_plus, zero_price, stone_price)
    profit = plus_price - cost
    print 'profit', profit
    if profit <= 0:
        print 'It is not worth it, the cost will be %i, while a %i cost %i on the market' % (cost,max_plus,plus_price)
    elif profit > 0:
        if profit > 1000000:
            profit /= 1000000
            print "You'll make %i million by doing this, you need %i +0 and %i stones" % (profit,zeros(max_plus),stones(max_plus))
        else:
            print "You'll make %i by doing this, you need %i +0 and %i stones" % (profit,zeros(max_plus),stones(max_plus))
        proc = (float(cost)/plus_price)*100
        print "The cost is %i procent of the cost for a + %i" % (proc,max_plus)
        print (float(plus_price)/cost)*100


zero_price = int(raw_input("Price for a +0: " ))
zero_price *= 1000000
max_plus = int(raw_input("To what +? " ))
plus_price = int(raw_input("How much for a +%i on the market right now?: " %max_plus))
plus_price *= 1000000
stone_price = int(raw_input("Price for enchant stone atm: "))
stone_price *= 1000000

worthit(max_plus, zero_price, stone_price, plus_price)
