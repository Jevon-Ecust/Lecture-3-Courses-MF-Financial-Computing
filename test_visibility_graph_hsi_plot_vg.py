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
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()