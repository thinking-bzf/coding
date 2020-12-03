# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:44:31 2019

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
#各个价格区间占市场的百分比

def Draw_1():
    data = pd.read_csv('final_data.csv')
    bin=[0,50000,100000,150000,200000,1000000]
    ct=pd.cut(data["价格"],bin,labels=["<5w","5-10w","10-15w","15-20w",">20w"])
    dt=ct.value_counts()
    d1=dt["<5w"]
    d2=dt["5-10w"]
    d3=dt["10-15w"]
    d4=dt["15-20w"]
    d5=dt[">20w"]
    labels = ["<5W","5-10W","10-15W","15-20W",">20W"]
    #每个标签占多大，会自动去算百分比
    sizes = [d1,d2,d3,d4,d5]
    colors = ["red","chocolate","tomato","orange","gold"]
    #将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0.05,0.05,0,0,0)
    plt.figure(figsize=(12,8))
    patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.1f%%',shadow = True,
                                    startangle = 90,pctdistance = 0.6)

    #labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    #autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    #shadow，饼是否有阴影
    #startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    #pctdistance，百分比的text离圆心的距离
    #patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    #改变文本的大小
    #方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size=(25)
    for t in p_text:
        t.set_size=(25)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title("二手车市场价格区间分布图",fontsize=16,y=1.03)
    plt.legend(loc="upper left",bbox_to_anchor=(0.8,0.3),fancybox=True,shadow=True)
    
    plt.savefig('1.png', dpi=200)
    plt.show()
#Draw_1()

#%%
#车龄-残值率

def Draw_2():
    dataset = pd.read_csv('final_data.csv')
    data = dataset[(dataset['车龄']!=0) & (dataset['级别']!='微面') & (dataset['级别']!='中大型SUV')]
    sns.set_style("white",{"font.sans-serif":['simhei', 'Arial']})


    data.eval('残值率 = 价格 / 新车价', inplace=True)
    D_value = data['残值率']
    D_rats_year = D_value*100
    cars = pd.DataFrame({'级别':data['级别'],'车龄':data['车龄'],'残值率':D_rats_year})
    cars = cars.groupby(['级别','车龄']).mean()
    
    plt.figure(figsize=(18,12))
    plt.title('车龄与残值率的关系图',fontsize=30)
    #plt.rcParams['figure.facecolor'] = 'w'
    #plt.rcParams['axes.facecolor'] = 'w'
    
    
    ax=plt.subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.xlabel('车龄/年',fontsize=20)
    plt.ylabel('残值率/%',fontsize=20)
    plt.tick_params(axis='both',labelsize=20)
    for name in cars.index.levels[0]:
        plt.plot(cars.loc[name].index.tolist(),cars.loc[name]['残值率'].tolist(),label = name,linestyle='-')
    plt.legend(loc="upper left",bbox_to_anchor=(1,1),fontsize=15)
    plt.savefig('2.png', dpi=200)
Draw_2()
    
#%%
#不同级别车与里程数的关系

#from matplotlib.font_manager import _rebuild
#_rebuild() #reload一下
#from pyecharts import Bar

def Draw_3():
    
    dataset = pd.read_csv('final_data.csv')
    dataset = dataset[(dataset['级别']!='MPV') &(dataset['级别']!='跑车') & (dataset['级别']!='微面') & (dataset['级别']!='轻客') & (dataset['级别']!='中大型SUV') & (dataset['级别']!='微型车') ]
    #plt.figure(figsize=(12,8))
    data_length = dataset.groupby(['级别'],as_index = False).mean()
    #plt.title('不同级别车与里程数的关系',fontsize=25)
    factorData = data_length['里程']
    xaxislabel = data_length['级别']
    x = xaxislabel[np.argsort(-factorData)]
    y = factorData[np.argsort(-factorData)]
    #bar = Bar('不同级别车与里程数的关系')
    #bar.add('A',xaxislabel,factorData,is_stack=True)
    plt.figure(figsize=(12,8))
    plt.xticks(np.arange(len(xaxislabel)), x, fontsize=18)  # xticks旋转270度显示
    plt.bar(np.arange(len(xaxislabel)), y, color = ('maroon','darkred','brown','firebrick','firebrick','lightcoral','darksalmon'))
    plt.yticks(np.arange(0, 80000, 10000),fontsize=18,rotation=45)
    plt.xlabel('级别')
    plt.ylabel('里程/km')
    #sns.set(style='white')
    plt.fill(facecolor='w')
    plt.ylim(0,65000)
    ax=plt.subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.title('不同级别车与里程数的关系',fontsize=20)
    #plt.show()
    plt.savefig('3.png', dpi=200)
Draw_3()

#%%
#车辆里程数与残值率的关系

#from pylab import *
#from statsmodels.formula.api import ols
#from matplotlib.font_manager import _rebuild
#_rebuild() #reload一下

def Draw_4():
    dataset = pd.read_csv('final_data.csv')
    df = pd.DataFrame(dataset)
    df.eval('残值 = 价格 / 新车价', inplace=True)
    #plt.title('车辆里程数与残值率的关系', fontsize=25)
    s = 20 * np.array(dataset)
    plt.figure(figsize=(12,8))
    lm = ols('残值~里程', df).fit()
    plt.plot(df['里程']/10000, lm.fittedvalues*100, 'r', linewidth=5)
    plt.scatter(dataset['里程']/10000, dataset['残值']*100, s=20, color='lightsalmon', lw=2,alpha=0.8)
    plt.grid(True, linestyle='-.',color = 'lightsalmon')
    plt.xlabel("里程/万公里", fontsize = 16)
    plt.ylabel("残值率/%", fontsize = 16)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20, rotation=45)
    
    plt.title('车辆里程数与残值率的关系',fontsize=21,loc='center')

    #plt.show()
    plt.savefig('4.png', dpi=200)
Draw_4()
#%%
#二手市场中自动挡与手动挡的占比
    
from pylab import *
from statsmodels.formula.api import ols

plt.rcParams['font.sans-serif'] = ['SimHei']
from matplotlib.font_manager import _rebuild
_rebuild() #reload一下

def Draw_5():
    dataset = pd.read_csv('final_data.csv')
    dataset_selfmove = dataset[dataset['自动挡'] == 1]
    dataset_handmove = dataset[dataset['自动挡'] == 0]
    
    dataset_labels = ['自动挡', '手动挡']
    dataset_sizes = [dataset_selfmove.shape[0], dataset_handmove.shape[0]]
    dataset_explodes = (0.05, 0.05)
    plt.figure(figsize=(12, 8))
    plt.title('二手市场中自动挡与手动挡的占比', fontsize=21,loc='center')
    plt.pie(dataset_sizes, explode=dataset_explodes, colors=['orangered','darksalmon'],labels=dataset_labels, autopct='%1.1f%%', shadow=True,
            startangle=60, textprops={'fontsize': 18})
    plt.legend(loc="upper right", fontsize=15, bbox_to_anchor=(1.2, 0.95), borderaxespad=0.3)
    #plt.show()
    plt.savefig('5.png', dpi=200)
Draw_5()


#%%
#不同排放量汽车数占比

def Draw_6(): 
    data = pd.read_csv('final_data.csv')
    data_1 = data[data['排量']<=1.4]
    data_2 = data[data['排量']==1.5]
    data_3 = data[data['排量']==1.6]
    data_4 = data[data['排量']==1.8]
    data_5 = data[data['排量']==2.0]
    data_6 = data[data['排量']>2.0]
    
    data_labels = ['<1.5', '1.5', '1.6', '1.8', '2.0', '>2.0']
    data_sizes = [data_1.shape[0], data_2.shape[0], data_3.shape[0], data_4.shape[0], data_5.shape[0], data_6.shape[0]]
    data_explodes = (0,0.05,0.05,0,0,0)
    
    plt.figure(figsize=(12,8))
    plt.title('不同排放量汽车数占比',fontsize=23)
    plt.pie(data_sizes,explode=data_explodes, labels=data_labels,
            autopct='%1.1f%%',shadow=True,startangle=150,pctdistance = 0.7,
            colors=['red', 'chocolate', 'tomato', 'orange', 'y', 'gold'],textprops={'fontsize':18})
    plt.legend(loc='upper left', bbox_to_anchor=(1.1, 0.5),fontsize=18)
    #plt.show()
    plt.savefig('6.png', dpi=200)
Draw_6()    

#%%
#x：健康度 y：折旧率

def Draw_71():
    data = pd.read_csv('final_data.csv')
    data['健康度'] = data['健康度'].map(lambda x: (x-0.8)/0.2)
    
    sns.set_style("white",{"font.sans-serif":['simhei', 'Arial']})
    mv_data = data.groupby(['健康度']).mean()[data.groupby(['健康度']).agg('count')['id']>50]
    D_value = mv_data['新车价'].values-mv_data['价格'].values
    D_rate = D_value/mv_data['新车价']*100
    cars = pd.DataFrame({'健康度':mv_data.index,'折旧率':D_rate})
    cars['健康度'] = cars['健康度'].map(lambda x: x*100)
    
    plt.figure(figsize=(12,8))
    plt.title('折旧率与健康度的关系图',fontsize=20)
    plt.plot(cars['健康度'], cars['折旧率'], color = 'orangered', lw=1)

    
    ax=plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.xlabel('健康度/%',fontsize=15)
    plt.ylabel('折旧率/%',fontsize=15)
    plt.legend(fontsize=15)
    #plt.show()
    plt.savefig('7_1.png', dpi=200)
#x：里程 y：健康度
def Draw_72():
    data = pd.read_csv('final_data.csv')
    sns.set_style("white",{"font.sans-serif":['simhei', 'Arial']})
    data['里程'] = data['里程'].map(lambda x: int(x/5000)*0.5)  
    mv_data = data.groupby(['里程']).mean()[data.groupby(['里程']).agg('count')['id']>50]
    mv_data['健康度'] = mv_data['健康度'].map(lambda x: (x-0.8)/0.2)
    
    plt.figure(figsize=(12,8))
    plt.title('健康度与行车里程的关系图',fontsize=20)
    ax=plt.subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(mv_data.index, mv_data['健康度']*100, color = 'orangered', lw=1)

    plt.xlabel('里程/万公里',fontsize=15)
    plt.ylabel('健康度/%',fontsize=15)
    plt.legend(fontsize=15)
    #plt.show()
    plt.savefig('7_2.png', dpi=200)
#Draw_71()
#Draw_72()
    
#%%
#每种级别车辆数量在市场的占比

def Draw_8():
    data = pd.read_csv('final_data.csv')
    data_jcc = data[data['级别'] =='紧凑型车']
    data_jcSUV = data[data['级别'] == "紧凑型SUV"]
    data_zxc = data[data['级别'] == "中型车"]
    data_xxc = data[data['级别'] == "小型车"]
    data_xcSUV = data[data['级别'] == "小型SUV"]
    data_zdxSUV = data[data['级别'] == "中大型SUV"]
    data_zdx = data[data['级别'] == "中型SUV"]
    data_labels = ['紧凑型车', '紧凑型SUV', '中型车','小型车','小型SUV','中大型SUV','中型SUV']
    data_sizes = [data_jcc.shape[0], data_jcSUV.shape[0], data_zxc.shape[0],data_xxc.shape[0],data_xcSUV.shape[0],data_zdxSUV.shape[0],data_zdx.shape[0]]
    data_explodes = (0.08,0.08,0.05,0,0,0,0)
    colors = ["firebrick","red","chocolate","orangered","tomato","orange","gold"]
    #colors=['steelblue','deepskyblue','c','teal','cornflowerblue','skyblue','slategray']

    plt.figure(figsize=(12,8))
    plt.title('二手车市场车辆级别分布图',fontsize=20,y=1.05)

    patches,l_text,p_text = plt.pie(data_sizes,explode=data_explodes,labels=data_labels,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.1f%%',shadow = True,
                                    startangle = 90,pctdistance = 0.6,textprops={'fontsize':18})
    
    plt.axis('equal')
    for t in l_text:
        t.set_size=(25)
        if t.get_text()=="中大型SUV":
            t.set_visible(False)
    for t in p_text:
        t.set_size=(25)
        if t.get_text()=="0.2%":
            t.set_visible(False)
    plt.legend(loc="upper left",bbox_to_anchor=(0.8,0.3),fancybox=True,shadow=True,fontsize=18)
    plt.savefig('8.png', dpi=200)

    #plt.show()
    
#Draw_8()

#%%
#各种级别车辆指标评价

def pailiang(List):
    List[0]=(List[0]-1.4)/0.09*1.5
    
def jiangkangdu(List):
    List[1]=(List[1]-0.96)*300*1.8*1.5

def cheling(List):
    List[2]=(10-(List[2]-2.7)/2.31*10)*1.5
    
def jiage(List):
    List[3]=10-(List[3]-50000)/13000

def xinchejia(List):
    List[4]=10-(List[4]-90000)/28000
    
def licheng(List):
    List[5]=10-(List[5]-40000)/1800
    


def Draw_9():
    labels = np.array(['排量', '健康度', '车龄', '价格', '新车价', '里程'])
    
    dataset = pd.read_csv('final_data.csv')
    dataset=pd.DataFrame(dataset)
    dataset=dataset[['级别','排量','健康度','车龄','价格','新车价','里程']]
    dataset=dataset.groupby('级别').mean()
    dataset=pd.DataFrame(dataset)
    dataset=dataset.transpose()
  
    sta1=[]
    sta2=[]
    sta3=[]
    sta4=[]
    sta5=[]
    sta6=[]
    sta7=[]
    
    
    for i in dataset['紧凑型车']:
        sta1.append(i)
    for i in dataset['紧凑型SUV']:
        sta2.append(i)
    for i in dataset['中型车']:
        sta3.append(i)
    for i in dataset['小型车']:
        sta4.append(i)
    for i in dataset['小型SUV']:
        sta5.append(i)
    #for i in dataset['中大型SUV']:
        #sta6.append(i)
    for i in dataset['中型SUV']:
        sta7.append(i)
    
    pailiang(sta1)
    pailiang(sta2)
    pailiang(sta3)
    pailiang(sta4)
    pailiang(sta5)
    #pailiang(sta6)
    pailiang(sta7)
    
    jiangkangdu(sta1)
    jiangkangdu(sta2)
    jiangkangdu(sta3)
    jiangkangdu(sta4)
    jiangkangdu(sta5)
    #jiangkangdu(sta6)
    jiangkangdu(sta7)
    
    cheling(sta1)
    cheling(sta2)
    cheling(sta3)
    cheling(sta4)
    cheling(sta5)
    #cheling(sta6)
    cheling(sta7)

    jiage(sta1)
    jiage(sta2)
    jiage(sta3)
    jiage(sta4)
    jiage(sta5)
    #jiage(sta6)
    jiage(sta7)
    
    xinchejia(sta1)
    xinchejia(sta2)
    xinchejia(sta3)
    xinchejia(sta4)
    xinchejia(sta5)
    #xinchejia(sta6)
    xinchejia(sta7)
    
    licheng(sta1)
    licheng(sta2)
    licheng(sta3)
    licheng(sta4)
    licheng(sta5)
    #licheng(sta6)
    licheng(sta7)
    
    
    stats1 =  np.array(sta1)
    stats2 =  np.array(sta2)
    stats3 =  np.array(sta3)
    stats4 =  np.array(sta4)
    stats5 =  np.array(sta5)
    #stats6 =  np.array(sta6)
    stats7 =  np.array(sta7)

    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    
    stats1=np.concatenate((stats1,[stats1[0]]))
    stats2=np.concatenate((stats2,[stats2[0]]))
    stats3=np.concatenate((stats3,[stats3[0]]))
    stats4=np.concatenate((stats4,[stats4[0]]))
    stats5=np.concatenate((stats5,[stats5[0]]))
    #stats6=np.concatenate((stats6,[stats6[0]]))
    stats7=np.concatenate((stats7,[stats7[0]]))
    
    
    angles=np.concatenate((angles,[angles[0]]))
    
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111,facecolor="w", polar = True)
    for i in [2,4,6,8,10,12]:
        ax.plot(angles,[i]*(6+1), '.:r',alpha=0.5)
                         
    
    ax.plot(angles, stats1, 'o-', linewidth=2,label='紧凑车型') 
    ax.fill(angles, stats1, alpha=0.3)
    ax.plot(angles, stats2, 'o-', linewidth=2,label='紧凑型SUV') 
    ax.fill(angles, stats2, alpha=0.3)
    ax.plot(angles, stats3, 'o-', linewidth=2,label='中型车') 
    ax.fill(angles, stats3, alpha=0.3)
    ax.plot(angles, stats4, 'o-', linewidth=2,label='小型车') 
    ax.fill(angles, stats4, alpha=0.3)
    ax.plot(angles, stats5, 'o-', linewidth=2,label='小型SUV') 
    ax.fill(angles, stats5, alpha=0.3)
    #ax.plot(angles, stats6, 'o-', linewidth=2,label='中大型SUV') 
    #ax.fill(angles, stats6, alpha=0.3)
    ax.plot(angles, stats7, 'o-', linewidth=2,label='中型SUV') 
    ax.fill(angles, stats7, alpha=0.3)
    
    ax.set_thetagrids(angles * 180/np.pi, labels,fontsize=18)  # Set the label for each axis
    ax.set_title('不同级别车辆评价图',fontsize=25)
    
    ax.set_thetagrids(angles * 180 / np.pi, labels,fontsize=18)
    plt.legend(loc="upper left",bbox_to_anchor=(1,0.3),fancybox=True,shadow=True,fontsize=12)
    #plt.show()
    ax.spines['polar'].set_visible(False) # 去掉最外围的黑圈
    ax.grid(False) 
    plt.savefig('9.png', dpi=200)
Draw_9()

#%%    
#不同级别的车的平均折旧率

'''
首先看看每个级别的车子都有多少
'''
def  Draw_10():
    dataset = pd.read_csv('final_data.csv')
    plt.figure(figsize=(12,8))
    numbers = dataset.groupby(['级别']).agg('count').sort_values('id',ascending=False)
    carlist = numbers.index.values
    '''
    先用了柱状图 看不出来什么
    #for a,b in zip(carlist,numbers['id']):
    #    plt.text(a,b+0.5,'%d'%b,ha='center',va='bottom',fontsize=17)
    #plt.bar(numbers.index.values,numbers['id'])
    下面用饼图看看
    colors=['steelblue','deepskyblue','c','teal','cornflowerblue','skyblue','slategray']
    plt.pie(numbers['id'],labels=numbers.index.values,colors=colors,autopct='%1.1f%%',shadow=False,pctdistance=0.8,startangle=100,textprops={'fontsize':15,'color':'w'})
    plt.legend(loc='right')
    plt.show()
    '''
    
    '''
    现在处理折旧率
    '''
    temp = dataset[(dataset['级别']!='中大型suv') & (dataset['级别']!='跑车') & (dataset['级别']!='微面')]
    D_value = temp['新车价'].values-temp['价格'].values
    D_rats_year = D_value/temp['新车价']/temp['车龄']*100
    cars = pd.DataFrame({'级别':temp['级别'],'年均折旧率':D_rats_year})
    
    cars = cars.groupby(['级别']).mean()
    cars['级别'] = cars.index
    cars = cars.sort_values('年均折旧率',ascending=False)
    
    plt.figure(figsize=(12,8))
    plt.title('车辆级别与年均折旧率之间的关系',fontsize=21)
    plt.xlabel('车辆级别',fontsize=17)
    plt.ylabel('年均折旧率',fontsize=17)
    for a,b in zip(cars['级别'],cars['年均折旧率']):
        plt.text(a,b+0.5,'%.2f%%'%b,ha='center',va='bottom',fontsize=15)
    plt.bar(cars['级别'],cars['年均折旧率'],color='firebrick')
    plt.ylim(0,40)
    plt.savefig('10.png', dpi=200)

#Draw_10()
    
#%%
def Draw_11():
    
    plt.figure(figsize=(12,8))
    dataset = pd.read_csv('final_data.csv')
    dataset['价格'] = dataset['价格'].map(lambda x: int(x/50000)*50000)
    plt.title('车龄-价格分布',size=21)
    
    plt.grid(True, linestyle='-.',color='r',alpha=0.1)
    plt.scatter(dataset['车龄'],dataset['价格'],alpha=0.1,s=1000,color='r')
    plt.tick_params(axis='y',labelcolor='k', labelsize='large', width=2)
    plt.tick_params(axis='x',labelcolor='k', labelsize='large', width=2)
    ax=plt.subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.xlabel('车龄/年',fontsize=20)
    plt.ylabel('价格/元',fontsize=20)
    #plt.show()
    plt.savefig('11.png', dpi=200)
    '''
    plt.figure(figsize=(12,8))
    plt.title('里程-价格分布',fontproperties="SimHei",size=21)
    plt.scatter(dataset['里程'],dataset['价格'],alpha=1,s=10)
    plt.show()
    '''
    
    '''
    plt.figure(figsize=(12,8))
    plt.xlabel('里程',fontsize=20,fontproperties="SimHei")
    plt.ylabel('价格',fontsize=20,fontproperties="SimHei")
    plt.title('里程-价格-车龄分布',fontproperties="SimHei",size=21)
    plt.scatter(dataset['里程'],dataset['价格'],alpha=0.3,s=dataset['车龄']*50)
    plt.show()
    '''

Draw_11()
#%%

Draw_1()
Draw_2()
Draw_3()
Draw_4()
Draw_5()
Draw_6()
Draw_71()
Draw_72()
Draw_8()
Draw_9()
Draw_10()
Draw_11()

