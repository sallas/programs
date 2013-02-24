import string
import random
import math

from itertools import chain

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas
from graphworld import *
from Graph import Vertex
from Graph import Edge
from Graph import Graph
from Graph import RandomGraph


def main(script, n='10', *args):

    # create n Vertices
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = RandomGraph(vs)
    g.add_random_edges(0.1)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
    
if __name__ == '__main__':
    import sys
    main(*sys.argv)
