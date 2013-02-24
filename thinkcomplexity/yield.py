import string

def alphabet_cycle():
    i = 0
    while True:
        for c in string.lowercase:
            if c == 'a':
                i += 1
            yield c+str(i)

for letter in alphabet_cycle():
    print letter
