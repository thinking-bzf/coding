import numpy as np
import matplotlib.pyplot as plt


def LoadData():
    datafile = '波士顿房价预测(神经网络)\\housing.data'
    data = np.fromfile(datafile, sep=' ')
    # 将一维的数组变为506*14的二维数组
    feature_names = [
        'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
        'PTRATIO', 'B', 'LSTAT', 'MEDV'
    ]
    feature_nums = len(feature_names)
    data = data.reshape([data.shape[0] // feature_nums, feature_nums])
    # 将数据集划分为训练集和测试集
    # 数据集中的前80%作为训练集，后20%作为测试集
    ratio = 0.8
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]  # 训练集
    test_data = data[offset:]  # 测试集

    maximums = training_data.max(axis=0)
    minimums = training_data.min(axis=0)

    # 数据归一化 将所有的数据归到（0，1）中
    for i in range(feature_nums):
        data[:, i] = (data[:, i] - minimums[i]) / (maximums[i] - minimums[i])
    return training_data, test_data


class Network(object):
    def __init__(self, num_of_weights):
        # 随机产生13个w值
        # 为保证每次结果都不一样，设置固定的随机种子
        np.random.seed(0)
        self.w = np.random.randn(num_of_weights, 1)
        self.b = 0.

    # 前向计算：得到的随机数作为特征值计算得到输出值的过程称为“前向计算”
    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        return z

    # 计算得到 预测值和实际值的损失值
    def loss(self, z, y):
        error = z - y
        cost = error * error
        cost = np.mean(cost)
        return cost

    def gradient(self, x, y):
        # 前向计算得到新的z
        z = self.forward(x)
        # 使用numpy矩阵计算每一个w的梯度，取每个w权值的平均值，并将其变为列矩阵
        gradient_w = (z - y) * x
        gradient_w = np.mean(gradient_w, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        # 使用numpy计算y的梯度
        gradient_b = (z - y)
        gradient_b = np.mean(gradient_b, axis=0)
        return gradient_w, gradient_b

    # 沿着梯度的反方向移动步长
    def update(self, gradient_w, gradient_b, eta=0.01):
        self.w = self.w - gradient_w * eta
        self.b = self.b - gradient_b * eta

    # eta为步长，或者可以被称为学习率，num_epoches为被训练的次数，batch_size为小组的个数
    def train(self, training_data, num_epoches=100, batch_size=5, eta=0.001):
        n = len(training_data)
        losses = []
        for epoch_id in range(num_epoches):
            np.random.shuffle(training_data)
            mini_batch = [
                training_data[k:k + batch_size]
                for k in range(0, n, batch_size)
            ]
            for iter_id, batch in enumerate(mini_batch):
                x = batch[:, :-1]
                y = batch[:, -1:]
                a = self.forward(x)
                loss = self.loss(a, y)
                gradient_w, gradient_b = self.gradient(x, y)
                self.update(gradient_w, gradient_b, eta)
                losses.append(loss)
                print('Epoch {:3d} / iter {:3d}, loss = {:.4f}'.format(
                    epoch_id, iter_id, loss))
        return losses


if __name__ == "__main__":
    # 获取数据 x为前13个因素 y为最后的房价
    training_data, test_data = LoadData()
    x = training_data[:, :-1]
    y = training_data[:, -1:]

    # 建立网络
    net = Network(13)
    # 开始训练
    losses = net.train(training_data, num_epoches=100, batch_size=1, eta=0.01)

    plot_x = np.arange(len(losses))
    plot_y = np.array(losses)
    # 绘画残值的迭代减小过程
    plt.plot(plot_x, plot_y)
    plt.show()
    
    trained_w = net.w
    test_x = test_data[:, :-1]
    test_y = test_data[:, -1:]
    result_y = np.dot(test_x, trained_w) + net.b
    # 绘制测试集的实际数据和预测值的拟合情况
    plt.plot(np.arange(len(test_y)), test_y, 'g--')
    plt.plot(np.arange(len(test_y)), result_y)
    plt.show()
