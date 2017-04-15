#!/usr/bin/python3.5

import graphviz as gv
from styles import *

g1 = gv.Digraph(format='png')
g1.node('START', fillcolor='#21BA65')
g1.node('STOP', fillcolor='#B44B6E')

g1.node('B', 'how many?',shape='hexagon')

g1.node('C', '2')
g1.node('D', '40')
g1.node('E', '58')

g1.edge('START', 'B')

g1.edge('B', 'C')
g1.edge('B', 'D')
g1.edge('B', 'E')

g1.edge('C', 'STOP')
g1.edge('D', 'STOP')
g1.edge('E', 'STOP')

g1.graph_attr['label']='A hella fancy grapherino'

g1 = apply_styles(g1, styles)
g1.render('img/g1')
