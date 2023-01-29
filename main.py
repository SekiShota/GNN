# グラフデータの可視化
from torch_geometric.datasets import Planetoid,NELL,Reddit
from Networkx import networkx_show
from Graphviz import graphviz_show
# from Cytoscape import cytoscape_show
# from Pyvis import pyvis_show
# from Visdcc import visdcc_show

from make_subgraph import make_subgraph

def main():
    # データセット選択
    datasets={
        0:"Cora",
        1:"Citeseer",
        2:"Pubmed",
        3:"Nell",
        4:"Reddit",
        }
    print("Cora:0, Citeseer:1, Pubmed:2, NELL:3, Reddit:4")
    # d=int(input("Please input dataset -> "))
    d=0

    print("Dataset: ",datasets[d])

    # データセット用意
    if d<=2:
        dataset=Planetoid(root="/tmp/"+datasets[d],name=datasets[d])

    elif d==3:
        dataset=NELL(root="/tmp/"+datasets[d])

    elif d==4:
        dataset=Reddit(root="/tmp/"+datasets[d])

    data=dataset[0]

    # グラフデータの可視化
    # networkx_show(data,datasets[d])
    # graphviz_show(data,datasets[d])
    # cytoscape_show(data,datasets[d])
    # pyvis_show(data,datasets[d])
    # visdcc_show(data,datasets[d])

    # サブグラフ作成
    hops=2
    node=0
    make_subgraph(data,hops,node)


if __name__=="__main__":
    main()