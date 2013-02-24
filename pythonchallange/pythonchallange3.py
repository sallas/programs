import string
inside = 0
save = ''
alosave = ''
word_dict = dict()
with open('symbols.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if c == '\n':
        continue
    if inside == 0:
        if not c.islower():
            inside = 1
            alosave = c
    elif inside in [1,2,5,6,7]:
        if not c.islower():
            inside += 1
            alosave += c
        else:
            inside = 0
    elif inside == 3:
        if c.islower():
            lower = True
            inside = 5
            temp = c
            alosave += c
        else:
            inside = -1
            
    elif inside == 4:
        inside = 0
    elif inside == 8:
        if not c.islower():
            inside = 0
        else:
            save += temp
            print alosave
            inside = 0
    elif inside == -1:
        if c.islower():
            inside = 0


