class PosPIDClass:
    """位置式PID类"""

    def __init__(self, kp=0.1, ki=0, kd=0):
        """初始化"""
        self.__Kp = kp  # P参数
        self.__Ki = ki  # I参数
        self.__Kd = kd  # D参数

        self.__Iterm_max = None  # Iterm最大值,用于积分限幅,非int或float表示不限制
        self.__mistake_enableIterm = None  # 启用I调节的误差最大值,用于积分分离,非int或float表示不限制
        self.__Dterm_forward = False  # 微分先行,False表示不启用
        self.__mistake_deadband = None  # 误差死区

        self.__Pterm = 0  # P调节数值
        self.__Iterm = 0  # I调节数值
        self.__Dterm = 0  # D调节数值
        self.__output = 0  # 输出量

        self.__measurement = 0  # 测量量
        self.__last_mistake = 0  # 上一次的误差
        self.__last_measurement = 0  # 上一次的测量值
        self.__target = 0  # 目标值

    def __str__(self):
        return "Positional PIDClass"

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

    def setLimitForIterm(self, max_value, mistake_enable_value):
        """设置I计算的限制参数"""
        self.__Iterm_max = max_value
        self.__mistake_enableIterm = mistake_enable_value

    def setDtermForward(self, state):
        """微分先行设置"""
        if isinstance(state, bool):
            self.__Dterm_forward = state

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
        在不考虑积分限幅、积分分离和微分先行时,公式为:
        $$U_n = K_P{\times}E_n + K_I{\times}{\sum_{i=1}^{n}E_i} + K_D{\times}(E_n-E_{n-1})$$
        """
        mistake = self.__target - feedback
        if isinstance(self.__mistake_deadband, int) or isinstance(self.__mistake_deadband, float):
            if abs(mistake) < self.__mistake_deadband:  # 误差在死区,则认为无误差
                mistake = 0
        self.__last_measurement = self.__measurement
        self.__measurement = feedback

        # P计算
        self.__Pterm = mistake

        # I计算
        if isinstance(self.__mistake_enableIterm, int) or isinstance(self.__mistake_enableIterm, float):  # 启用积分分离
            if mistake <= self.__mistake_enableIterm:  # 误差不大于限制值
                self.__Iterm += mistake
        else:
            self.__Iterm += mistake
        if isinstance(self.__Iterm_max, int) or isinstance(self.__Iterm_max, float):  # 启用积分限幅
            self.__Iterm = min(self.__Iterm_max, self.__Iterm)

        # D计算
        if self.__Dterm_forward:  # 启用微分先行
            self.__Dterm = self.__measurement - self.__last_measurement
        else:
            self.__Dterm = mistake - self.__last_mistake

        self.__last_mistake = mistake

        self.__output = self.__Pterm * self.__Kp + self.__Iterm * self.__Ki + self.__Dterm * self.__Kd

    def output(self):
        """获取最终结果"""
        return self.__output


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    Show_SubImage = True

    target_point = 100
    current_point = 0
    set_times = 100

    PID_Controller = PosPIDClass()
    PID_Controller.setTarget(target_point)
    PID_Controller.setKp(0.2)
    PID_Controller.setKi(0)
    PID_Controller.setKd(0)
    PID_Controller.setLimitForIterm(None, None)
    PID_Controller.setDtermForward(False)
    PID_Controller.setMistakeDeadband(0)

    data_point = [[0, ], [current_point, ]]
    data_Pterm = [[0, ], [0, ]]
    data_Iterm = [[0, ], [0, ]]
    data_Dterm = [[0, ], [0, ]]

    times = 0
    while set_times > times:
        PID_Controller.update(current_point)
        current_point += PID_Controller.output()

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
