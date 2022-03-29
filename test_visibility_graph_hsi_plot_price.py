from visibility_graph import visibility_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns

# data=np.loadtxt('Vec_HSI_Network.txt',skiprows=1)
# # data_zs=data[1:len(data),:]
# print(data)
# data=data[:,1:]
# data=data.T
# data=pd.DataFrame(data)

# corr = data.corr()
# cmap = sns.diverging_palette(230, 20, as_cmap=True)
# # sns.heatmap(corr,cmap=cmap)


df = pd.read_csv('HSI-s.csv')
data=df
# data = df[(df.datadate >= 20200101) & (df.datadate <= 20210101)]

print(data)
data=data.sort_values(['datadate','tic'])
price = data['prcld']
date = data['datadate']

date = date[1:-1]

plt.axes([0.2, 0.2, 0.7, 0.5])
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.plot(price)
xt=np.array(range(0,len(date),50))
plt.xticks(xt,date[0:len(date):50],rotation=60)
plt.ylabel('Price')
plt.savefig(f'HSI_price.pdf')
