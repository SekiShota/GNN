"""各ノードのホップ数リストを作成"""

import collections
import numpy as np

def solve_shortest_path_unweighted_graph(graph, start):
    start = graph.get_vertex(start)
    start.set_distance(0)
    start.set_previous(None)
    queue = collections.deque()
    queue.append(start)
    # 各ノードのホップ数リスト
    num_hop=[]

    while queue:
        current_vertex = queue.popleft()
        for neighbor in current_vertex.get_connections():
            if neighbor.get_distance() == -1:
                neighbor.set_distance(current_vertex.get_distance() + 1)
                neighbor.set_previous(current_vertex)
                queue.append(neighbor)
    
    for vertex in graph.vertex_dict.values():
        if vertex.get_distance() == -1 or vertex.get_distance() == 0:
            num_hop.append(0)
            continue
        else:
            num_hop.append(vertex.get_distance()-1)
                    
        # アクセスしたノード初期化
        vertex.set_distance(-1)
        vertex.set_previous(None)
    # 始点ノード初期化
    start.set_distance(-1)
    start.set_previous(None)

    return num_hop


from graph_config import Graph

def num_hop_calc(data):
    graph=Graph()
    edge_index=data["edge_index"]
    source=edge_index[0]
    target=edge_index[1]

    num_edges=np.array(edge_index).shape[1]

    node_list=list(set(source.tolist()))
    if len(node_list)!=len(data.y):
        node_list=np.arange(0,len(data.y))

    for n in node_list:
        graph.add_vertex(n)
    for i in range(num_edges):
        graph.add_edge(edge_index[0][i].item(), edge_index[1][i].item())

    num_hop_list=[]
    for i,n in enumerate(node_list):
        num_hop=solve_shortest_path_unweighted_graph(graph=graph, start=n)
        num_hop_list.append(num_hop)

    return num_hop_list

