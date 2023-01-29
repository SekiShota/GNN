# 結合情報からサブグラフ作成
import numpy as np

def make_subgraph(data,hops,node):
    # 特定ノード
    start_node=node
    print("start_node:",start_node)
    # ホップ数
    num_hops=hops+1
    print("num_hops:",hops)

    # 結合情報
    edges=data["edge_index"]
    print("edges:",edges)

    # エッジ数
    num_edges=data.num_edges

    source=edges[0]
    target=edges[1]

    print("source:",source,num_edges)
    print("target:",target)
    print()

    """
    結合しているノード抽出してリスト作成
    # 1.特定ノードと結合しているノードを抽出
    # 2.1のノードをcheck_nodes.append()
    # 3.さらにそれらと結合しているノードを抽出,,ただし既にあるものはappendしない
    # 4.hop=num_hopsで終了
    """

    # 1
    check_nodes=[]
    check_nodes.append(start_node)
    for i in range(num_edges):
        # 2
        if source[i]==start_node:
            check_nodes.append(target[i].item())
    # print("特定ノードと直接結合している：",check_nodes)

    # 3
    hop=0
    while(1):
        if hop<num_hops:
            check_nodes=bfs(check_nodes,hop,num_edges,source,target)
            hop+=1
        else:
            break

    print()
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("check_nodes: ",check_nodes)
    print("BFS finished.")

    """
    サブグラフを作成する
    # 抽出ノードリストから新しくdata["edge_index"]を作成する
    """
    subgraph=[[],[]]
    for n in check_nodes:
        for i in range(num_edges):
            if n==source[i]:
                subgraph[0].append(source[i].item())
                subgraph[1].append(target[i].item())

    print("<サブグラフ>")
    # print(subgraph)
    print("ノード数：",len(check_nodes))
    print("エッジ数：",np.array(subgraph).shape[1])


# 結合しているノードを抽出する関数
def bfs(check_nodes,hop,num_edges,source,target):
    print(f"hop = {hop}")
    print(f"check_nodes: {len(check_nodes)}")
    
    for j in range(len(check_nodes)):
        for k in range(num_edges):
            if source[k]==check_nodes[j] and not(target[k].item() in check_nodes):
                check_nodes.append(target[k].item())
    # print(f"{hop}:{check_nodes}")
    print()

    return check_nodes