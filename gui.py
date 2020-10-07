"""
Visualización gráfica
"""
import networkx as nx
import matplotlib.pyplot as plt
import EoN.auxiliary as eon

from arbol import Arbol


def visualizar_arbol(arbol: Arbol):
    """
    Visualizar gráficamente el árbol mediante networkx

    :param arbol: El árbol a dibujar
    """
    G = nx.Graph()
    nodos = arbol.pre_orden()
    if len(nodos) < 2:
        return False
    G.add_nodes_from([n.valor for n in nodos])

    for nodo in nodos:
        if nodo.izquierdo:
            G.add_edge(nodo.valor, nodo.izquierdo.valor, edge_type='Izq')
        if nodo.derecho:
            G.add_edge(nodo.valor, nodo.derecho.valor, edge_type='Der')

    plt.plot()

    pos = eon.hierarchy_pos(G, root=arbol.raiz.valor)
    labels = nx.get_edge_attributes(G, 'edge_type')

    nx.draw(G, pos, node_color='#aaa', with_labels=True, node_size=800, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    return True
