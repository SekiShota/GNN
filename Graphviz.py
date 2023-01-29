# graphvizを使って可視化

import Graphviz
import time

def graphviz_show(data):
    num_nodes=data.num_nodes
    num_edges=data.num_edges
    edges=data["edge_index"]

    print("ノード数：",data.num_nodes)
    print("エッジ数：",data.num_edges)
    print("結合情報：",data["edge_index"])

    # グラフオブジェクト生成
    g=Graphviz.Graph(format="png")

    start=time.time()
    # ノード作成
    for n in range(1000):
        g.node(str(n))
    # g.node("a")
    # g.node("b")
    # g.node("c")

    # ノード結合（エッジ作成）
    for e in range(2000):
        s=str(edges[0][e].item())
        r=str(edges[1][e].item())
        # print(s, "->", r)
        g.edge(s,r)
    # g.edge("a","b")
    # g.edge("c","b")
    
    # g.view()
    g.render("graphviz_cora")
    finish=time.time()
    print("処理時間：", finish-start)
