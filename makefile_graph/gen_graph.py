#!/usr/bin/python3.5

import graphviz as gv
from styles import *

g = gv.Digraph(format='png')

g.node('all')
g.node('gen_graph.py')
g.node('img/g.png')
g.node('clean')

g.edge('all','img/g.png')
g.edge('gen_graph.py','Makefile')
g.edge('gen_graph.py','makefiletographviz.py')
g.edge('img/g.png','gen_graph.py')
g.graph_attr['label']='Makefile'
g.render('img/g')

