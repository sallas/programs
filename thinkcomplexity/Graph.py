import sys
import random
import string

from collections import deque

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
        
    def get_edge(self,v1,v2):
        try:
            return self[v1][v2]
        except KeyError:
            return None
    def remove_edge(self,e):
        v, w = e
        del self[v][w]
        del self[w][v]

    def vertices(self):
        vert_list = []
        for i in self.iterkeys():
            vert_list.append(i)
        return vert_list
    def edges(self):
        edge_list = []
        for i in self:
            for d in self[i]:
                edge_list.append(self[i][d])
        return edge_list
    def out_vertices(self,v):
        out = []
        for i in self[v]:
            out.append(i)
        return out
    def out_edges(self,v):
        out = []
        for i in self[v]:
            out.append(self[v][i])
        return out
    def add_all_edges(self):
        for i in self.vertices():
            for d in self.vertices():
                if i != d:
                    self[i][d] = Edge(i,d)
    def add_regular_edges(self, n):
        k = 0
        nel = len(self.vertices())
        listy = self.vertices()[:]
        for s in range(1,n):
            for i in range(nel):
                self.add_edge(Edge(listy[i],listy[(i+s)%(nel)]))
        
            
##        for d in listy1:
##            print 'd', d
##            print 'len', len(self.out_vertices(i))
##            if len(self.out_vertices(i)) < k and len(self.out_vertices(d)) < k:
##                print 'edge', self.get_edge(i,d)
##                if i != d and self.get_edge(i,d) == None:
##                    self.add_edge(Edge(i,d))
##                    print 'here'

    
class RandomGraph(Graph):
    def add_random_edges(self,p):
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j <= i: continue
                if random.random() > p: continue
                self.add_edge(Edge(v, w))

    def bfs(self, s, visit=None):
        """Breadth first search, starting with (s).
        If (visit) is provided, it is invoked on each vertex.
        Returns the set of visited vertices.
        """
        visited = set()

        # initialize the queue with the start vertex
        queue = deque([s])
        
        # loop until the queue is empty
        while queue:

            # get the next vertex
            v = queue.popleft()

            # skip it if it's already visited
            if v in visited: continue

            # mark it visited, then invoke the visit function
            visited.add(v)
            if visit: visit(v)

            # add its out vertices to the queue
            queue.extend(self.out_vertices(v))

        # return the visited vertices
        return visited

    def is_connected(self):
        """Returns True if there is a path from any vertex to
        any other vertex in this graph; False otherwise.
        """
        vs = self.vertices()
        visited = self.bfs(vs[0])
        return len(visited) == len(vs)

##    def is_connected(self):
##        v = random.choice(self.vertices())
##        vs = self.vertices()
##        visited = set()
##        que = []
##        que.append(v)
##        while que != []:
##            t = que.pop(0)
##            for edge in self.out_edges(t):
##                u = edge[1]
##                if u not in visited:
##                    visited.add(u)
##                    que.append(u)
##        return len(visited) == len(vs)
            
def test(n,tests):
    n = int(n)
    testlist = []
    for i in range(100):
        print i
        testlist.append(graphtest(n,i/100.0,tests))
    print testlist
            

def graphtest(n,prob,tests):
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]
    istrue = 0.0
    for i in range(tests):
        g = RandomGraph(vs)
        g.add_random_edges(prob)
        if g.is_connected():
            istrue += 1
    return [prob,istrue/tests]

    
    v = Vertex('v')
    w = Vertex('w')
    b = Vertex('b')
    c = Vertex('c')
    e_edge = Edge(v, w)
    n_edge = Edge(c, b)
    m_edge = Edge(c, v)
    g = Graph([v,w,b,c])
    g.add_all_edges()
    print g.edges()
    print 'out_edges (v): ', g.out_edges(v)
    print
    print 'out_vertices (v): ', g.out_vertices(v)
    print 
    print 'edges: ', g.edges()
    print
    print 'graph: ', g
    print
    print 'vertices:', g.vertices()
    print
    print 'get_edge. b and w:', g.get_edge(b,w)
    print
    print 'get_edge. c and b:', g.get_edge(c, b)
    print
    print 'get_edge. v and w:', g.get_edge(v,w)
    print
    g.remove_edge(e_edge)
    print 'get_edge (v, w) after removal:', g.get_edge(v,w)
    print
    print 'out_vertices (v): ', g.out_vertices(v)



###test()
##v = Vertex('v')
##w = Vertex('w')
##b = Vertex('b')
##c = Vertex('c')
##e_edge = Edge(v, w)
##n_edge = Edge(c, b)
##m_edge = Edge(c, v)
##g = Graph([v,w,b,c])
##g.add_all_edges()

