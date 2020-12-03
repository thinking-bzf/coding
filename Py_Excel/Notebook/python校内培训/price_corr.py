#%%
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:13:18 2019

@author: 15941
"""

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

plt.style.use("ggplot")
font = {'family':'SimHei'}
matplotlib.rc('font',**font)
matplotlib.rcParams['axes.unicode_minus']=False

#%%

dataset = pd.read_csv('corr.csv')

price_corr = pd.DataFrame({'fac':dataset['Unnamed: 0'],'价格':dataset['价格']})
price_corr['价格'] = price_corr['价格'].abs()
price_corr = price_corr.sort_values('价格',ascending= False)
price_corr = price_corr[1:]
colors = ["darkred","brown","red","chocolate","tomato","orange","gold"]
explodes = (0.05,0.05,0,0,0,0,0)

plt.figure(figsize=(12,8))
plt.title('各指标对价格影响占比',fontsize=20,y=0.95)
plt.pie(price_corr['价格'],explode =explodes ,colors=colors,shadow=True,labels=price_corr['fac'],autopct='%1.1f%%',startangle=90,textprops={'fontsize':18})
plt.legend(loc="upper left",bbox_to_anchor=(1.1,0.47),fancybox=True,shadow=True,fontsize=15)
plt.savefig('price_corr.png', dpi=200)


#%%
dataset=pd.read_csv('corr.csv')

dataset['价格']=[-0.27,-0.14,0.27,0.30,0.43,0.62,0.87,1.00]
dataset['id']=['车龄','里程','健康度','排放标准','排量','自动挡','新车价','价格']
data1=dataset['价格']
data2=dataset['id']


plt.figure(figsize=(8,6))
   

plt.title('不同指标对价格影响条形图', fontsize = 24)
plt.bar(data2, data1, color = ("darkred","brown","firebrick","red","chocolate","tomato","orange","gold")
)
plt.xlabel('指标',fontsize=17)
plt.ylabel('权重',fontsize=17)
plt.xticks(np.arange(len(data2)), data2, fontsize=15)
plt.yticks(np.arange(-0.4, 1.2,0.2),fontsize=18)
        
for a,b in zip(data2,data1):
    if b<0:
        plt.text(a,b-0.05,'%.2f'%b,ha='center',fontsize=15)
    else:
        plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=15)

plt.savefig('pirce_corr_zhuzhuangtu.png', dpi=200)
plt.show()




