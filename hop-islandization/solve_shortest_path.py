# 始点ノードから、特定のホップ数で到達できる目的ノードまでの経路算出

import collections
from graph_config import Graph

# 探索済みノードリスト
visited=[]
# エッジ情報
partition_edge_index=[[],[]]

def solve_shortest_path(graph, start, num_hops):
    print(f"ホップ数：{num_hops}")
    routes=[]
    start = graph.get_vertex(start)
    start.set_distance(0)
    start.set_previous(None)
    queue = collections.deque()
    queue.append(start)
    while queue:
        current_vertex = queue.popleft()
        for neighbor in current_vertex.get_connections():
            if neighbor.get_distance() == -1:
                neighbor.set_distance(current_vertex.get_distance() + 1)
                neighbor.set_previous(current_vertex)
                queue.append(neighbor)
    
    for vertex in graph.vertex_dict.values():
        if vertex.get_distance() == -1:
            print(f'{start.get_vertex_id()} から {vertex.get_vertex_id()} へは移動できません。')
            continue
        elif vertex.get_distance() == 0:
            continue
        else:
            # 指定したホップ数:num_hopsのノードのみ
            if vertex.get_distance()-1==num_hops:
                # 最短経路の出力           
                if vertex.get_distance()>0:
                    route = [vertex.get_vertex_id()]
                    current_vertex = vertex
                    while current_vertex.get_previous():
                        route.append(current_vertex.get_previous().get_vertex_id())
                        current_vertex = current_vertex.get_previous()
                    print(f'{start.get_vertex_id()} から {vertex.get_vertex_id()} の移動ルート:', route[::-1])
                    # routes.append(route[::-1])
                    routes.append(route)
                

    # アクセスしたノード初期化 
    for vertex in graph.vertex_dict.values():
        vertex.set_distance(-1)
        vertex.set_previous(None)

    return routes
