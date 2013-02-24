# -*- coding: cp1252 -*-
import random
worst = [50,"Ingen"]
while (True):
    name = raw_input("Namnet på spelaren?")
    if name == "Slut":
        break;
    print "Tarningskasten blev:"
    total = 0
    for i in range(0,3):
        one = random.randrange(1,6)
        two = random.randrange(1,6)
        total += one + two
        print one, two, "=", one + two
    print "Summa:", total
    if total < worst[0]:
        worst[0] = total
        worst[1] = name
        
print worst[1], "hade mest otur och fick tarningssumman",  worst[0], "!"


