# 一维卡尔曼滤波 系统简单取样
import matplotlib.pyplot as plt
import numpy as np


class KalmanFilterOneDimension:
    def __init__(self):
        self.X = 0  # 最优估计值
        self.A = 1  # 状态转移系数
        self.H = 1  # 测量系数
        self.R = 1  # 测量噪声方差
        self.Q = 1  # 预测噪声方差
        self.W = 0  # 测量噪声均值
        self.B = 0  # 控制系数
        self.U = 0  # 控制量
        self.P = 0  # 估计值协方差
        self.K = 0  # kalman增益系数

    def generate(self, _z):
        # 迭代 z为测量值
        _x = self.A * self.X + self.B * self.U + self.W  # 估计值
        _p = self.A * self.P * self.A + self.Q  # 估计值协方差
        x_n = _x + self.K * (_z - self.H * _x)  # 最优估计值
        self.X = x_n  # 记录最优估计值
        self.K = _p * self.H / (self.H * _p * self.H + self.R)  # kalman增益
        self.P = (1 - self.K * self.H) * _p  # 最优估计值协方差

        return x_n


if __name__ == "__main__":
    import random

    generate_times = 200
    KM_Filter = KalmanFilterOneDimension()

    x = 0
    # x_noise_l = np.array(x + np.random.randn(generate_times))
    x_noise_l = [x + random.uniform(-0.5, 0.5) for _ in range(generate_times)]
    x_filter_l = np.array([])
    for i in range(generate_times):
        x_filter_l = np.append(x_filter_l, KM_Filter.generate(float(x_noise_l[i])))

    plt.title("Kalman", fontproperties="SimHei", fontsize=18)
    plt.xlabel("Times", fontsize=16)
    plt.ylabel("X Filter", fontsize=16)
    plt.axhline(x, color="salmon", linewidth=1.2)
    plt.plot(np.arange(generate_times), x_noise_l, color="cornflowerblue", linewidth=1.2)
    plt.plot(np.arange(generate_times), x_filter_l, color="lightgreen", linewidth=1.2)
    plt.show()
