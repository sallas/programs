fin = open('words.txt')

def has_no_e(s):
    for c in s:
        if c == 'e':
            return False
    return True

def avoid(string, forbidden_string):
    for c in string:
        for d in forbidden_string:
            if c == d:
                return False
    return True

def uses_only(word, string):
    for c in word:
        if c not in string:
            return False
    return True

def uses_all(word, string):
    return uses_only(string, word)

def is_abecedarian(word):
    i = 0
    for c in word:
        if i > 0:
            if c < d:
                return False
        d = c
        i += 1
    return True

def three_letters(word):
    double = 0
    tripple = 0
    for c in word:
        #print 'c =', c
        if double == 0:
            d = c
            double +=1
        elif double == 2:
            d = c
            double = 1
        else:
            if c == d:
                tripple +=1
                double += 1
            else:
                double = 1
                tripple = 0
                d = c
        if tripple == 3:
            return True
        #print 'double =', double
        #print 'tripple =', tripple
        
    return False

def is_palindrome(word):
    
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else: return False

def miles():
    for i in range(111111,999999):
        mile = i
        original = i
        if is_palindrome(str(mile)[2:]):
            mile += 1
            if is_palindrome(str(mile)[1:]):
                print 'second', mile
                mile += 1
                if is_palindrome(str(mile)[1:-1]):
                    print 'third', mile
                    mile += 1
                    if is_palindrome(str(mile)[:]):
                        print 'fourth', mile
                        print original
                

def age():
    count = 0
    save = 0
    for i in range(0,99-13):
        c = 0
        count = 0
        save = 0
        for d in range (13+i,99):
            if str(c).zfill(2) == str(d)[::-1]:
                count += 1
                print 'c', c
                print 'd', d
            if save == 0:
                if count == 6:
                    print 'c at c = 5', c
                    save = c
            if count == 8:
                return save
            c +=1
    return 0
    
        
'''dont_contain = 0

string = 'aeiuoy'
for line in fin:
    word = line.strip()
    if avoid(word,string):
        dont_contain += 1'''
string = 'acefhlo'
for line in fin:
    word = line.strip()
    if three_letters(word):
        print word

word = 'haabbcc'
if three_letters(word):
    print word
    

