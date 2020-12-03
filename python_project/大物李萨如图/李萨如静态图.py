from math import pi, cos
import matplotlib.pyplot as plt
import numpy as np

ts = np.linspace(-50, 50, 1000)


def TheSameDirection(A1=5, A2=5, w1=1.2, w2=1.2, theta1=pi, theta2=3 * pi):

    y1, y2 = [], []
    for t in ts:
        y1.append(A1 * cos(w1 * t + theta1))
        y2.append(A2 * cos(w2 * t + theta2))
    plt.figure()
    plt.plot(ts, y1, alpha=0.5, c='deeppink')
    plt.plot(ts, y2, alpha=0.5, c='orange')
    y = []
    for i in range(len(y1)):
        y.append(y1[i] + y2[i])
    plt.plot(ts, y, c='red', alpha=5)
    plt.show()


def TheDifferentDirection(A1=5,
                          A2=8,
                          w1=1.2,
                          w2=1.2,
                          theta1=pi,
                          theta2=3 * pi):
    #解决中文乱码问题
    plt.rcParams["font.sans-serif"] = "SimHei"
    #解决负号无法正常显示的问题
    plt.rcParams['axes.unicode_minus'] = False
    x, y = [], []
    for t in ts:
        x.append(A1 * cos(w1 * t + theta1))
        y.append(A2 * cos(w2 * t + theta2))
    plt.figure()
    plt.plot(x, y)
    plt.title(f'频率比 {w1}:{w2} 相位差 {(theta2-theta1)/pi}pi')
    plt.savefig(f'频率比{w2}_相位差{(theta2-theta1)/pi}pi.jpg')
    # plt.show()


if __name__ == '__main__':
    '''
	ts在-10~10之间：

	TheSameDirection()
	TheSameDirection(theta2=2*pi)
	TheSameDirection(theta2=0.6*pi)
	'''
    '''
	ts在-50~50之间：

	TheSameDirection(w1=4,w2=4.1)
	'''
    '''
	TheDifferentDirection()
	TheDifferentDirection(theta2=2*pi)
	TheDifferentDirection(theta2=0.6*pi)
	TheDifferentDirection(theta2=3.6*pi)
	'''

    for w in range(1, 5):
        for theta in range(0, 5):
            TheDifferentDirection(w1=1,
                                  w2=w,
                                  theta1=0,
                                  theta2=theta * 0.25 * pi)

    # TheDifferentDirection(w1=3, w2=7)
    # TheDifferentDirection(w1=2, w2=11)
    # TheDifferentDirection(w1=7, w2=3)
