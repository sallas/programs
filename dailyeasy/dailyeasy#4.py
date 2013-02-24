import random
random.seed(None)

amount = int(raw_input("How many passwords do you want?: "))
length = int(raw_input("How long shall they be?: "))

for i in xrange(0, amount):
    password = "";
    for j in xrange(0, length):
        password += chr(36 + random.randrange(0,93))
    print password
    
