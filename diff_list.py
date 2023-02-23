# リストの中身を比較して、一方に含まれない内容を抽出
# https://qiita.com/KALDI_Smash/items/1d428fbeb8081707b154

import numpy as np

def make_deleted_edges(original, partition):
    # 元データのエッジ情報
    original_edge_index=np.array(original)
    # 分割後のエッジ情報
    partition_edge_index=np.array(partition)

    edge1=[]
    for i in range(original_edge_index.shape[1]):
        edge1.append([original_edge_index[0][i], original_edge_index[1][i]])
    print("元データのエッジ情報")
    print(edge1)

    edge2=[]
    for i in range(partition_edge_index.shape[1]):
        edge2.append([partition_edge_index[0][i], partition_edge_index[1][i]])
    print("分割後のエッジ情報")
    print(edge2)

    A=set(map(tuple,edge1))
    B=set(map(tuple,edge2))

    deleted_edges = sorted(list(A.difference(B)))

    return deleted_edges


import torch

original_edge_index=torch.tensor([[1,1,2,2,3,4,5,99,99],[6,7,7,8,8,9,10,11,12]])
partition_edge_index=torch.tensor([[1,2,3],[6,7,8]])

result=make_deleted_edges(original=original_edge_index, partition=partition_edge_index)

output_file=open("output.txt","w")
output_file.write("< deleted edges >\n")
output_file.write(f"num: {len(result)}\n")
print("\n削除したエッジ")
for i in range(len(result)):
    print(result[i])
    output_file.write(f"{result[i]}\n")