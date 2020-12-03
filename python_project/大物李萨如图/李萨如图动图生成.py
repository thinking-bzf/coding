import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)


# 初始化函数
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,


# 用于存储x轴和y轴的数据点
xdata, ydata = [], []


# 模拟x,y轴坐标的累加，当长度大于60时删除
def ghostImage(x, y):
    xdata.append(x)
    ydata.append(y)
    if len(xdata) > 60:
        del xdata[0]
        del ydata[0]
    return xdata, ydata


# 动画函数
def animate(i):
    # 时间计数器
    t = i / 100.0
    # x,y要绘画的点
    x = 40 * np.cos(1 * np.pi * t + 0.75 * np.pi)
    y = 40 * np.cos(5 * np.pi * t)
    # 在x, y轴上追加新的点
    line.set_data(ghostImage(x, y))
    return line,


# 设置标题
plt.title('频率 1:5，相位差 3/4 pi')
plt.axis('off')

# 调用动图绘画函数
anim = animation.FuncAnimation(fig,
                               animate,
                               init_func=init,
                               frames=400,
                               interval=20,
                               blit=True)


#解决中文乱码问题
plt.rcParams["font.sans-serif"] = "SimHei"
#解决负号无法正常显示的问题
plt.rcParams['axes.unicode_minus'] = False

plt.show()
anim.save('1-5-3.gif', writer='imagemagick')
