import json

MDKA = {
    'q0': {'q1': 'a', 'q4': 'b'},
    'q1': {'q4': 'b', 'q2': 'a'},
    'q2': {'q5': 'a', 'q2': 'b'},
    'q3': {'q7': 'a', 'q5': 'b'},
    'q4': {'q5': 'b', 'q2': 'a'},
    'q5': {'q5': 'b', 'q6': 'a'},
    'q6': {'q7': 'a', 'q6': 'b'},
    'q7': {'q7': 'a', 'q6': 'b'}
}

start_vertex = 'q0'
final_vertices = {'q7', 'q6', 'q3'}


def remove_unreachable_vertices(graph, start_vertex):
    visited = set()
    stack = [start_vertex]

    # Обход графа в глубину
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(neighbour for neighbour in graph[vertex] if neighbour not in visited)

    # Удаляем недостижимые вершины из графа
    for vertex in list(graph.keys()):
        if vertex not in visited:
            del graph[vertex]


def print_graph(graph):
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d.get('weight', '') for u, v, d in G.edges(data=True)})
    plt.show()


def minimaze_graph(graph):
    new_graph = {}
    groups = [list(set(graph.keys()) - final_vertices), list(final_vertices & set(graph.keys()))]
    doing = True
    while doing:
        doing = False
        # for veys in groups:
        veys = groups[0]
        if len(veys) == 1:
            continue
        this_vay = []
        i = []
        for vey in veys:
            # ищем вершины которые связаны с другой группой
            set1 = set(veys)
            ch = list(graph.get(vey).keys())
            check = all(elem in set1 for elem in ch)
            if not check:
                i.append(veys.index(vey))
        [this_vay.append(veys[j]) for j in i]
        if this_vay:
            groups.append(this_vay)
            for index in sorted(i, reverse=True):
                del veys[index]
            i.clear()
            doing = True
    if not groups[0]:
        del groups[0]
    # for vey in groups:
    #     veys = {}
    #
    #     new_graph[vey[0]] =


if __name__ == "__main__":
    remove_unreachable_vertices(MDKA, 'q0')
    minimaze_graph(MDKA)
    # print_graph(MDKA)
