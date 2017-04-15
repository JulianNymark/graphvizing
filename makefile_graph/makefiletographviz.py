#!/usr/bin/python3.5
# stolen & modified from https://github.com/vak/makefile2dot

import re
import sys

from sys import stdin, stdout, stderr
from styles import *

def _line_emitter(input):
    line_to_emit = ''

    for line in input:
        if line.endswith('\\'):
            line_to_emit += line[:-1]
        else:
            line_to_emit += line
            yield line_to_emit
            line_to_emit = ''

_pat_colon = re.compile(':')
def _dependency_emitter(lines):
    for line in lines:
        if (
            len(line) == 0 or
            line[0] in ['#'] or
            line.find('=') > 0 or
            line.find('?') > 0
        ):
            continue
        elif line[0] in ['\t']:
            #print('NODE_CONTENTS:', line)
            continue

        parts = _pat_colon.split(line)
        if len(parts) == 1:
            continue
        elif len(parts) == 2:
            if len(parts[1]) == 0 or parts[1][0] != '=':
                yield tuple(parts)
        else:
            print('more then one ":" not yet implemented ;^)\n got the following:\n%s' % parts, file=sys.stderr)

_pat_whitespacing = re.compile('[ \t]+')
def _single_dep_emitter(out_deps_pairs):
    for outs_str, deps_str in out_deps_pairs:
        for out in _pat_whitespacing.split(outs_str.strip()):
            nodes.append(out)
            deps = _pat_whitespacing.split(deps_str.strip())
            for dep in deps:
                if dep:
                    if dep[0] == '#':
                        break
                    edges.append(tuple([dep, out]))

def parse(makefile):
    """convert makefile (from stdin) -> nodes & edges
    """
    _single_dep_emitter(_dependency_emitter(_line_emitter(''.join(makefile).split('\n'))))

def makefile2dot():
    print('#!/usr/bin/python3.5\n')
    print('import graphviz as gv')
    print('from styles import *\n')
    print('g = gv.Digraph(format=\'png\')')

    # nodes
    print()
    for n in nodes:
        print('g.node(\'' + n + '\')')

    # edges
    print()
    for e in edges:
        print('g.edge(\'' + e[1] + '\',\'' + e[0] + '\')')

    print('g.graph_attr[\'label\']=\'Makefile\'')
    print('g.render(\'img/g\')')
    print()

nodes = []
edges = []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('Usage:\n\t./makefile2graphviz.py <Makefile >out.py\n', file=sys.stderr)
    else:
        parse(stdin)
        makefile2dot()
