import random
def monto():
    heads = 0
    for i in range(3):
        if random.random() > 0.5:
            heads += 1
    return heads == 1

def test(num):
    num = num
    true = 0.0
    for i in range(num):
        if monto():
            true += 1
    this = (true/num)*100
    print "This much: ", this
        
