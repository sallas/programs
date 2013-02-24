

st =''
word = "map"
for i in word:
    if i == ' ' or i == '.' or i == '(' or i == ')':
        st += i
    else:
        u = ord(i) + 2
        if u > 122:
            st += chr(96+u%122)
        else:
            st += chr(ord(i)+2)

print st

