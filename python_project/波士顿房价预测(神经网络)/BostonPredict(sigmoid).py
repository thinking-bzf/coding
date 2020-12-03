import numpy as np
import math
import random
import matplotlib.pyplot as plt


# 生成区间[a,b]内的随机数
def random_number(a, b):
    return (b - a) * random.random() + a


# sigmoid函数-激活函数
def sigmoid(x):
    # our activation function: f(x) = 1 / (1 * e^(-x))
    return 1 / (1 + np.exp(-x))


# 获取sigmoid函数的求导
def deriver_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)


class BPNet(object):
    def __init__(self, count_in, count_hidden, count_out):
        # 输入层，中间层，输出层的节点数
        self.count_in = count_in + 1  # 增加一个偏置节点
        self.count_hidden = count_hidden + 1  #增加一个偏置节点
        self.count_out = count_out

        # 创建权重矩阵
                                  
        