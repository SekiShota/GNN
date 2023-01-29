# pyvisで可視化
from pyvis.network import Network
import time

def pyvis_show(data, dataset_name):
    num_nodes=data.num_nodes
    num_edges=data.num_edges
    edges=data["edge_index"]
    labels=data.y

    print("ノード数：",num_nodes)
    print("エッジ数：",num_edges)
    print("結合情報：",edges)

    # ネットワークのインスタンス生成
    network = Network(
        height="600px",  # デフォルト "500px"
        width="800px",  # デフォルト "500px"
        notebook=True,  # これをTrueにしておくとjupyter上で結果が見れる
        bgcolor='#ffffff',  # 背景色。デフォルト "#ffffff"
        directed=False,  # Trueにすると有向グラフ。デフォルトはFalseで無向グラフ
    )

    start=time.time()
    # add_node でノードを追加
    # label は省略可能。省略するとidと同じになる。
    colors=["purple","black","red","blue","yellow","green","pink"]
    for n_id in range(num_nodes):
        # print("n_id:",n_id, "label:",labels[n_id].item())
        network.add_node(n_id=n_id, label=labels[n_id].item(), color=colors[labels[n_id].item()])
    

    # # add_edge でエッジを追加
    for e in range(num_edges):
        s=edges[0][e].item()
        r=edges[1][e].item()
        # print(s, "->", r)
        network.add_edge(s,r,)

    # network.add_edge(1, 2,)
    # network.add_edge(2, 4, width=2)  # width で太さを変えられる
    # network.add_edge(3, 4, smooth="dynamic")  # smooth を指定することで、エッジを曲線にできる
    # network.add_edge(4, 3, smooth="dynamic")  # エッジを曲線にすると双方向のエッジを別の線にできる。(直線だと重なる)

    finish=time.time()
    print("処理時間：", finish-start)
    # # 指定したファイル名でHTMLを出力。
    network.show("pyvis_sample1.html")



















# サンプル===================================================
# ネットワークのインスタンス生成
# network = Network(
#     height="600px",  # デフォルト "500px"
#     width="800px",  # デフォルト "500px"
#     notebook=True,  # これをTrueにしておくとjupyter上で結果が見れる
#     bgcolor='#ffffff',  # 背景色。デフォルト "#ffffff"
#     directed=False,  # Trueにすると有向グラフ。デフォルトはFalseで無向グラフ
# )

# # add_node でノードを追加
# # label は省略可能。省略するとidと同じになる。
# network.add_node(n_id=1, label=1, shape="circle")
# network.add_node(n_id=2, label=2, shape="box", color="green")
# network.add_node(n_id=3, label=3, shape="triangle")
# network.add_node(n_id=4, label=4)  # shape を省略すると、 shape="dot"と同じになる

# # add_edge でエッジを追加
# network.add_edge(1, 2,)
# network.add_edge(2, 4, width=2)  # width で太さを変えられる
# network.add_edge(3, 4, smooth="dynamic")  # smooth を指定することで、エッジを曲線にできる
# network.add_edge(4, 3, smooth="dynamic")  # エッジを曲線にすると双方向のエッジを別の線にできる。(直線だと重なる)

# # 指定したファイル名でHTMLを出力。
# network.show("pyvis_sample1.html")