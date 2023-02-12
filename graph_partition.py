# スペクトラルクラスタリングを使ったグラフデータ分割
from sklearn.cluster import SpectralClustering
import numpy as np

def graph_partition(data,th_edge):
    print("データセット：",data)
    print("エッジ閾値：",th_edge)

    edge_index=data["edge_index"]
    # 隣接行列作成
    adj_matrix=make_adjmat(edge_index=edge_index)
    print("隣接行列")
    print(adj_matrix)

    # スペクトラルクラスタリングのインスタンス作成
    sc=SpectralClustering(n_clusters=10,affinity='precomputed', n_init=100,assign_labels='kmeans',random_state=0)
    sc.fit(adj_matrix)
    # print(sc.labels_)






def make_adjmat(edge_index):
    nodes=list(set(edge_index[0].tolist()))
    # print("データセットに存在するノード")
    # print(nodes)
    num_nodes=len(nodes)
    print("ノード数：",num_nodes)

    # 隣接行列
    adj_matrix=np.zeros((num_nodes,num_nodes))
    sources=edge_index[0].tolist()
    targets=edge_index[1].tolist()
    num_edge=len(sources)
    # edges=edge_index.tolist()
    for i in range(num_edge):
        source=sources[i]
        target=targets[i]
        adj_matrix[source][target]=1

    return adj_matrix
