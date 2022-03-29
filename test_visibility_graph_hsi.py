from visibility_graph import visibility_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns

# series = [0.87, 0.49, 0.36, 0.83, 0.87]
# series = np.random.random((100,1))
df = pd.read_csv('HSI-s.csv')
data=df
# data = df[(df.datadate >= 20200101) & (df.datadate <= 20210101)]

print(data)
data=data.sort_values(['datadate','tic'])
series = data['prcld']
date = data['datadate']
series = series.diff()
series = series[1:-1]
date = date[1:-1]
# plt.plot(date,series)
G = visibility_graph( series )
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

Uids=G.nodes()
Edges=G.edges()       
Edges=list(Edges)
Uids=list(Uids)
# # print(Edges) 
# a = open(f'HSI_edgelist.txt', "w",encoding='UTF-8')
# for i in range(len(Edges)):
#     edge = Edges[i]
#     a.write(edge[0]+' '+edge[1]+'\n')
# a.close()

Index1=np.zeros((len(Edges),1))
Index2=np.zeros((len(Edges),1))
for i in range(len(Edges)):
    edge = Edges[i]
    # print(edge) 
    n1 = edge[0]
    n2 = edge[1]
    Index1[i]=Uids.index(n1)
    Index2[i]=Uids.index(n2)
# print(Index1)


fid= open(f'HSI_Network.txt','w',encoding='utf-8')
for j in range(len(Index1)):
    txt='%d %d\n'%(Index1[j],Index2[j])
    fid.write(txt)
fid.close()
fid= open(f'HSI_Network_names.txt','w',encoding='utf-8')
for j in range(len(Uids)):
    txt='%s\n'%(Uids[j])
    fid.write(txt)
fid.close()

