import networkx as nx
import matplotlib.pyplot as plt

def load_nodes():
    text = '''  Node    Size
                1        523
                2        231
                3        102
                4         72
                1+2      710
                1+3      891
                1+3+4    621'''
    # load nodes into list, discard header
    # this may be replaced by some appropriate output 
    # from your program
    data = text.split('\n')[1:]
    data = [ d.split() for d in data ]
    data = [ tuple([ d[0], 
                    dict( size=int(d[1]) ) 
                    ]) for d in data]
    return data

def load_edges():
    text = '''  From   To
                1+2    1
                1+2    2
                1+3    1
                1+3    3
                1+3+4    1
                1+3+4    3
                1+3+4    4'''
    # load edges into list, discard header
    # this may be replaced by some appropriate output 
    # from your program
    data = text.split('\n')[1:]
    data = [ tuple( d.split() ) for d in data ]
    return data

if __name__ == '__main__':
    scale_factor = 5
    G = nx.Graph()
    nodes = load_nodes()
    node_sizes = [ n[1]['size']*scale_factor
                  for n in nodes ]

    edges = load_edges()
    G.add_edges_from( edges )

    nx.draw_networkx(G, 
                     pos=nx.spring_layout(G),
                     node_size = node_sizes)
    plt.axis('off')
    plt.show()
