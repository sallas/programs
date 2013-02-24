import operator
x = {1: (2,2), 3: (4,), 4:(3,2), 2:(1,2), 0:(0,0)}
sorted_x = sorted(x, key=x.get)
