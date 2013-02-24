import urllib
import string
list2 = list()
string = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
for i in xrange(400):
    opener = urllib.FancyURLopener({})
    f = opener.open(string)
    f = f.read()
    k = f.split()
    k[-1]
    string = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + k[-1]
    print string


urllib.urlopen("http://www.google.com")
