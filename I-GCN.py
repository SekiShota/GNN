# 探索済み（ハブ、島に属する）ノード
visited_nodes=[]

def i_gcn(dataset):
    print(dataset)

    edge_index=dataset["edge_index"]
    source=edge_index[0]
    target=edge_index[1]
    print("source:",source)
    print("target:",target)
    print()

    # ノードごとの隣接ノード数
    import collections

    source=source.tolist()
    target=target.tolist()

    source=[0,1,2,3,3,3,4,5,5,6,6,7,7,7,7,8,8,9,9,10,10,10,11,12,13,14,14,14,15,15,16,17,17,17,17,18,19,20,21,22,22,22,23,23,23,24,24,25,26,27,27,28]
    target=[3,3,8,0,1,7,5,4,6,5,7,3,6,8,9,2,7,7,10,9,11,14,10,13,12,10,15,17,14,16,15,14,18,19,20,17,17,17,22,21,23,27,22,24,26,23,25,24,23,22,28,27]
    adjnode_count=collections.Counter(source)
    print(adjnode_count)
    print("グラフの含まれるノード")
    print(sorted(list(set(source))))

    # 隣接ノード数が100以上のノードをハブとする
    hubs=[]
    for node,adjacents in adjnode_count.items():
        if adjacents>=4:
            hubs.append(node)
            visited_nodes.append(node)
    print("ハブとなるノード：",hubs)
    print()

    # ハブと隣接しているノード=島を作るための始点ノード
    island_start=[] 
    for h in hubs:
        # ハブを探索済みノードに追加
        visited_nodes.append(h)
        # ハブに隣接しているノードを取得
        for i,s in enumerate(source):
            if h==s and not(target[i] in island_start):
                # ハブに隣接しているノードを探索済みノードに追加
                visited_nodes.append(target[i])
                island_start.append(target[i])

        print("ハブ：",h)
        print("島の始点ノードの集合：",island_start)
        print()
        island_start.clear()
    # # print(visited_nodes)

    # # ハブに隣接しているノードだけループ
    # # for i_node in island_start:
    # # 島の始点ノード
    # i_node=island_start[0]
    # print("島の始点ノード：",i_node)
    # # 島に含まれているノードのリスト
    # island_member=[]
    # # 島の始点ノードを島に追加
    # island_member.append(i_node)

    # while(1):
    #     island_member=bfs(source=source, target=target, island_member=island_member)
    #     # 島に含まれるノードの数の最大を20としたとき
    #     if len(island_member)>10: 
    #         break

    # print()
    # print("<最終結果>")
    # print("島に含まれるノードの数：", len(island_member))
    # print(island_member)
    # print()



# 幅優先探索
def bfs(source, target, island_member):
    print("[bfs]")
    print("初期メンバー：",island_member)

    # 始点ノードと隣接しているノード取得
    for start_node in island_member:
        # # 島に含まれるノードの数が閾値以上になったら抜ける
        # if len(island_member)>=5:
        #     break

        print("始点ノード：",start_node)
        for i,s in enumerate(source):
            if start_node==s and not(target[i] in island_member) and not(target[i] in visited_nodes):
                # 始点ノードと隣接しているノードをリストに追加（=島に追加）
                island_member.append(target[i])
                # 島に追加したノードを探索済みノードのリストに追加
                visited_nodes.append(target[i])
                
    
        print("島に含まれているノード：",island_member)
        print("島に含まれるノードの数：",len(island_member))
        print()
        

    return island_member


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import torch

# データセット読み込み
dataset=torch.load("./subgraph.pt")
# 関数:i_gcnに渡す
i_gcn(dataset=dataset)