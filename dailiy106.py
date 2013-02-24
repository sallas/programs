words_dict = {}
string = ''
scr = ''
for i in open('scrambled.txt').read():
    scr += i
for i in open('match.txt').read():
    string += i
for i in scr.split():
    for l in string.split():
        if sorted(i) == sorted:
            words_dict[i] = l
for i in words_dict:
    print i, words_dict[i]
