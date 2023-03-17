from visibility_graph import visibility_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns

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
L=100
# plt.plot(date,series)
for j in range(0,len(date)-L,5):
    s=series[j:j+L]
    G = visibility_graph( s )

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()