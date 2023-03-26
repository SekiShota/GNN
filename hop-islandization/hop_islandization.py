"""ホップ数ベースのグラフ分割"""
from torch_geometric.data import Data
import torch
import numpy as np

from num_hop_calc import num_hop_calc
from solve_shortest_path import solve_shortest_path
from graph_config import Graph

def hop_islandization(data, num_hops):
    print("ホップ数の初期値：", num_hops)
    print("扱うグラフデータセット：", data)

    # 各ノードのホップ数リスト
    num_hop_list=num_hop_calc(data=data)
    for i in range(np.array(num_hop_list).shape[0]):
        print(f"ノード番号：{i}")
        print(num_hop_list[i])
        print("")
    print("---------------------")

    # 各ノードのnum_hopsで到達できるノード（目的ノード）を取得
    for i in range(np.array(num_hop_list).shape[0]):
        print("ノード番号：",i)
        for j in range(np.array(num_hop_list).shape[0]):
            if num_hop_list[i][j]==num_hops:
                print(j)
    print("---------------------")

    # グラフ定義
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
    
    # グラフ、始点、ホップ数を指定して、始点から目的ノードまでの経路を算出
    # key: 始点ノード、value: 目的ノードまでの経路のリスト
    route_dict={}
    for i in range(np.array(num_hop_list).shape[0]):
        routes=solve_shortest_path(graph=graph, start=i, num_hops=num_hops)
        route_dict[i]=routes
        print("")

    for i in range(np.array(num_hop_list).shape[0]):
        print(i," : ",route_dict[i])
    print("")

    # route_dictを使って、分割を行う
    visited=[]
    flag=0
    partition_edge_index=[[],[]]
    for i in range(np.array(num_hop_list).shape[0]):
        for route_idx in range(len(route_dict[i])):
            print(route_dict[i][route_idx])
            for node in route_dict[i][route_idx]:
                # 未探索かつ経路の中に探索済みがない
                if not(node in visited):
                    if flag==0:
                        visited.append(node)
                    else:
                        continue
                else:
                    flag=1
                    continue
        # ある始点ノードの探索終了のタイミングで経路に探索済みがあるフラグを0に戻す
        flag=0

        print("探索済み：", visited)
        print("")








if __name__ == '__main__':
    # エッジ定義
    source=[0,1,2,3,3,3,4,5,5,6,6,7,7,7,7,8,8,9,9,10,10,10,11,12,12,12,13,13,14,15,15,15,15,16,17,18]
    target=[3,3,8,0,1,7,5,4,6,5,7,3,6,8,9,2,7,7,10,9,11,12,10,10,13,15,12,14,13,12,16,17,18,15,15,15]
    edge_index=torch.tensor([source,target])
    # カテゴリ定義
    cates=[i for i in range(len(list(set(source))))]
    cates=torch.tensor(cates)
    # グラフデータセット定義
    data=Data(y=cates, edge_index=edge_index)
    # ホップ数
    num_hops=3

    # ホップ数ベースのグラフ分割
    hop_islandization(data=data, num_hops=num_hops)

