from swampy.TurtleWorld import *
import math
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    """Draws n sided polygon with side length long using the function polyline,
    t is a turle"""
    angle = 360.0 / n
    polyline(t, n, length, angle)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """
    #print "inside polyline"
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    """using the function arc to draw a full circle with r radius"""
    #print "inside circle"
    arc(t, r, 360)

def arc(t, r, angle):
    #print "inside arc"
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)




def triangle(t, r):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    
    fd(t, r)
    lt(t, 360/3)
    fd(t, math.sqrt(r**2+r**2))
    lt(t, 360/3)
    fd(t, r)
    lt(t, 360/3)
def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


# draw a sequence of three flowers, as shown in the book.

lt(bob, 360/7/2)
triangle(bob, 40)
lt(bob, 360/7)
triangle(bob, 40)
lt(bob, 360/7)
triangle(bob, 40)
lt(bob, 360/7)
triangle(bob, 40)
lt(bob, 360/7)
triangle(bob, 40)
lt(bob, 360/7)
triangle(bob, 40)
lt(bob, 360/7)

wait_for_user()



