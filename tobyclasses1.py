class Kangaroo(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch_contents = contents
        

    def __str__(self):
        return '%s' % (self.pouch_contents)

    def print_time(self):
        print str(self)

    def put_in_pouch(self, o):
        self.pouch_contents.append(o)

    



kanga = Kangaroo(5)
roo = Kangaroo()
kanga.put_in_pouch('o')
kanga.put_in_pouch(5)
kanga.put_in_pouch(roo)

print kanga
print roo
