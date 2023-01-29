# networkxを使って可視化

import networkx as nx
from torch_geometric.utils import to_networkx
import matplotlib.pyplot as plt
import time

def networkx_show(data,dataset_name):
    num_nodes=data.num_nodes
    num_edges=data.num_edges
    edges=data["edge_index"]

    print("ノード数：",num_nodes)
    print("エッジ数：",num_edges)
    print("結合情報：",edges)

    # グラフオブジェクト生成
    data_nx=to_networkx(data)

    # グラフ作成
    start=time.time()
    plt.figure(figsize=(12,10))
    nx.draw(
        data_nx,
        node_color=data.y,
        node_size=5
    )
    plt.savefig("networkx_"+dataset_name+".png")

    finish=time.time()
    print("処理時間：", finish-start)
