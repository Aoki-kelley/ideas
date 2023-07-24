# 匀速运动模型
import matplotlib.pyplot as plt
import numpy as np

DELTA_T = 1  # 取样时间间隔
V_X = 0  # x方向加速度均值
V_Y = 0  # y 方向加速度均值
DELTA_X = 1  # x 方向位置方差
DELTA_Y = 1  # y 方向位置方差
DELTA_V_X = 1  # x 方向速度方差
DELTA_V_Y = 1  # y 方向速度方差

I_MATRIX = np.eye(4)


class KalmanFilterCV:
    def __init__(self):
        self.X = np.mat([[0],
                         [0],
                         [0],
                         [0]])  # 最优估计值
        self.A = np.mat([[1, 0, DELTA_T, 0],
                         [0, 1, 0, DELTA_T],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])  # 状态转移矩阵
        self.H = np.mat([[0, 0, 1, 0],
                         [0, 0, 0, 1]])  # 测量矩阵
        self.R = np.mat([[DELTA_V_X ** 2, 0],
                         [0, DELTA_V_Y ** 2]])  # 测量噪声方差
        self.Q = np.mat([[0.25 * DELTA_T ** 4 * DELTA_V_X ** 2, 0, 0.5 * DELTA_T ** 3 * DELTA_V_X ** 2, 0],
                         [0, 0.25 * DELTA_T ** 4 * DELTA_V_Y ** 2, 0, 0.5 * DELTA_T ** 3 * DELTA_V_Y ** 2],
                         [0.5 * DELTA_T ** 3 * DELTA_V_X ** 2, 0, 1 * DELTA_T ** 2 * DELTA_V_X ** 2, 0],
                         [0, 0.5 * DELTA_T ** 3 * DELTA_V_Y ** 2, 0, 1 * DELTA_T ** 2 * DELTA_V_Y ** 2]])  # 预测噪声方差
        self.W = np.mat([[0.5 * V_X * DELTA_T ** 2],
                         [0.5 * V_Y * DELTA_T ** 2],
                         [V_X * DELTA_T],
                         [V_Y * DELTA_T]])  # 测量噪声均值
        self.B = 0  # 控制系数
        self.U = np.mat([[0], [0], [0], [0]])  # 控制量
        self.P = np.mat([[DELTA_X ** 2, 0, 0, 0],
                         [0, DELTA_Y ** 2, 0, 0],
                         [0, 0, DELTA_V_X ** 2, 0],
                         [0, 0, 0, DELTA_V_Y ** 2]])  # 估计值协方差
        self.K = np.mat([[1, 0],
                         [1, 0],
                         [1, 0],
                         [1, 0]])

    def generate(self, _z):
        # 迭代 z为测量值矩阵
        _x = self.A * self.X + self.B * self.U + self.W  # 估计值
        _p = self.A * self.P * self.A.T + self.Q  # 估计值协方差
        x_n = _x + self.K * (_z - self.H * _x)  # 最优估计值
        self.X = x_n  # 记录最优估计值
        self.K = (_p * self.H.T) * np.linalg.pinv(self.H * _p * self.H.T + self.R)  # kalman增益
        self.P = (I_MATRIX - self.K * self.H) * _p  # 最优估计值协方差

        return x_n


if __name__ == "__main__":
    vx = 20  # x 方向速度
    vy = 16  # y 方向速度
    generate_times = 200
    mvx = np.array(vx + np.random.randn(generate_times))  # vx 测量值
    mvy = np.array(vy + np.random.randn(generate_times))  # vy 测量值
    # import random
    #
    # noise_abs = 0.5
    # mvx = np.array([vx + random.uniform(-noise_abs, noise_abs) for _ in range(generate_times)])  # vx 测量值
    # mvy = np.array([vy + random.uniform(-noise_abs, noise_abs) for _ in range(generate_times)])  # vy 测量值
    km_vx = np.array([])
    km_vy = np.array([])

    KM_Filter = KalmanFilterCV()

    for i in range(generate_times):
        tmp = KM_Filter.generate(np.mat([[mvx[i]], [mvy[i]]]))
        km_vx = np.append(km_vx, float(tmp[2, 0]))
        km_vy = np.append(km_vy, float(tmp[3, 0]))

    fig = plt.figure(figsize=(8, 5))
    ax1 = plt.subplot(211)
    plt.axhline(vx, color="salmon", label=r"real value", linewidth=1.2)
    plt.plot(range(generate_times), mvx, color="cornflowerblue", label=r"measurement", linewidth=1.2)
    plt.plot(range(generate_times), km_vx, color="lightgreen", label=r"filter value", linewidth=1.2)
    plt.ylabel(r'X Velocity')
    plt.xlabel(r'Times')
    plt.title('KM Filter')
    plt.legend(loc='best', prop={'size': 10})

    ax2 = plt.subplot(212)
    plt.axhline(vy, color="salmon", label=r"real value", linewidth=1.2)
    plt.plot(range(generate_times), mvy, color="cornflowerblue", label=r"measurement", linewidth=1.2)
    plt.plot(range(generate_times), km_vy, color="lightgreen", label=r"filter value", linewidth=1.2)
    plt.xlabel(r'Times')
    plt.ylabel(r'Y Velocity')
    plt.title('KM Filter')
    plt.legend(loc='best', prop={'size': 10})

    plt.tight_layout()
    plt.show()
