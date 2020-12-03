import pandas as pd
movie_frame = pd.read_excel(r'C:\Coding\python_project\top250.xlsx')
import matplotlib.pyplot as plt
import numpy as np

score = movie_frame.groupby('评分')['标题'].count().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(np.array(score['评分']),
        np.array(score['标题']),
        width=0.08,
        align='center')
plt.xticks(score['评分'])
plt.tick_params(width=0.8)
for a, b in zip(score['评分'], score['标题']):
    plt.text(a, b, b, ha="center", va="bottom", fontsize=12)
np.array(score['评分'])
plt.show()