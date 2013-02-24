def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def print_hist(h):
    keylist = h.keys()
    keylist.sort()
    for c in keylist:
        print c, h[c]
        
h = histogram('brontosaurus')
print_hist(h)
