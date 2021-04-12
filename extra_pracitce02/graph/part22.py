import os
from graphviz import Digraph
def tree_graphviz_imported(path):
    dot = Digraph()
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
         dot.edge(os.path.basename(dirpath),dirname)
        for filename in filenames:
            dot.edge(os.path.basename(dirpath),filename)
    print(dot.source)
def tree_graphviz_noimported(path):
    print('digraph {')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print('  ' + os.path.basename(dirpath) + " -> " + dirname)
        for filename in filenames:
            print('  ' + os.path.basename(dirpath) + " -> " + f'"{filename}"')
    print('}')
tree_graphviz_imported('/python-practice/practice01')
tree_graphviz_noimported(os.getcwd())

