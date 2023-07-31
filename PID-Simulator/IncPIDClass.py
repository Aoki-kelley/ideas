class IncPIDClass:
    """增量式PID类"""

    def __init__(self, kp=0.1, ki=0, kd=0):
        """初始化"""
        self.__Kp = kp  # P参数
        self.__Ki = ki  # I参数
        self.__Kd = kd  # D参数

        self.__mistake_enableIterm = None  # 启用I调节的误差最大值,用于积分分离,非int或float表示不限制
        self.__mistake_deadband = None  # 误差死区

        self.__Pterm = 0  # P调节数值
        self.__Iterm = 0  # I调节数值
        self.__Dterm = 0  # D调节数值
        self.__output = 0  # 输出量

        self.__mistake = 0  # 误差
        self.__last_mistake = 0  # 上一次的误差
        self.__double_last_mistake = 0  # 上上次的测量值
        self.__target = 0  # 目标值

    def __str__(self):
        return "Increasing PIDClass"

    def setKp(self, kp):
        """设置P参数"""
        self.__Kp = kp

    def setKi(self, ki):
        """设置I参数"""
        self.__Ki = ki

    def setKd(self, kd):
        """设置D参数"""
        self.__Kd = kd

    def setTarget(self, target):
        """设置目标值"""
        self.__target = target

    def setMistakeDeadband(self, daedband):
        """误差死区设置"""
        self.__mistake_deadband = daedband

    def getPterm(self):
        """获取P计算值"""
        return self.__Pterm

    def getIterm(self):
        """获取I计算值"""
        return self.__Iterm

    def getDterm(self):
        """获取D计算值"""
        return self.__Dterm

    def update(self, feedback):
        """
        迭代计算
        $$\Delta u_k = u_k - u_{k-1} =
        K_p \times (e_k-e_{k-1}) + K_i \times e_k + K_d \times (e_k - 2e_{k-1} + e_{k-2})$$
        """
        mistake = self.__target - feedback

        self.__double_last_mistake = self.__last_mistake  # 误差记录更新
        self.__last_mistake = self.__mistake
        self.__mistake = mistake

        self.__Pterm = self.__mistake - self.__last_mistake  # P计算

        if isinstance(self.__mistake_enableIterm, int) or isinstance(self.__mistake_enableIterm, float):  # 启用积分分离
            if mistake <= self.__mistake_enableIterm:  # 误差不大于限制值
                self.__Iterm = mistake  # I计算
        else:
            self.__Iterm = mistake

        self.__Dterm = self.__mistake - 2 * self.__last_mistake + self.__double_last_mistake  # D计算

        self.__output = self.__Kp * self.__Pterm + self.__Ki * self.__Iterm + self.__Kd * self.__Dterm  # 计算输出值

    def output(self):
        """获取最终结果"""
        return self.__output


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    Show_SubImage = True

    target_point = 10
    current_speed = 0
    current_point = 0
    set_times = 100

    PID_Controller = IncPIDClass()
    PID_Controller.setTarget(target_point)
    PID_Controller.setKp(0.2)
    PID_Controller.setKi(0)
    PID_Controller.setKd(0)
    PID_Controller.setMistakeDeadband(0)

    data_point = [[0, ], [current_point, ]]
    data_Pterm = [[0, ], [0, ]]
    data_Iterm = [[0, ], [0, ]]
    data_Dterm = [[0, ], [0, ]]

    times = 0
    while set_times > times:
        PID_Controller.update(current_point)
        current_speed += PID_Controller.output()
        current_point += current_speed * 1

        times += 1
        # print(times, current_point)
        data_point[0].append(times)
        data_point[1].append(current_point)

        data_Pterm[0].append(times)
        data_Pterm[1].append(PID_Controller.getPterm())

        data_Iterm[0].append(times)
        data_Iterm[1].append(PID_Controller.getIterm())

        data_Dterm[0].append(times)
        data_Dterm[1].append(PID_Controller.getDterm())

    if Show_SubImage:
        plt.figure(figsize=(10, 7.5))
        ax1 = plt.subplot(221)
        plt.title("Point", fontproperties="SimHei", fontsize=14)
        plt.axhline(target_point, color="salmon")
        plt.plot(data_point[0], data_point[1], color="cornflowerblue", linewidth=0.8)

        ax2 = plt.subplot(222)
        plt.title("Pterm", fontproperties="SimHei", fontsize=14)
        plt.plot(data_Pterm[0], data_Pterm[1], color="cornflowerblue", linewidth=0.8)

        ax3 = plt.subplot(223)
        plt.title("Iterm", fontproperties="SimHei", fontsize=14, y=-0.28)
        plt.plot(data_Iterm[0], data_Iterm[1], color="cornflowerblue", linewidth=0.8)

        ax4 = plt.subplot(224)
        plt.title("Dterm", fontproperties="SimHei", fontsize=14, y=-0.28)
        plt.plot(data_Dterm[0], data_Dterm[1], color="cornflowerblue", linewidth=0.8)
    else:
        plt.title("Point", fontproperties="SimHei", fontsize=18)
        plt.xlabel("times", fontsize=16)
        plt.ylabel("point", fontsize=16)
        plt.axhline(target_point, color="salmon")
        plt.plot(data_point[0], data_point[1], color="cornflowerblue", linewidth=1.2)

    plt.tight_layout()
    plt.show()
