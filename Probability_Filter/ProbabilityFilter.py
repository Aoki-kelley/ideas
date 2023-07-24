# 概率滤波
import numpy as np


class ProbabilityFilterClass:
    def __init__(self, probable_max_val, probable_min_val, scale):
        """
        :param probable_max_val: 预计最大值
        :param probable_min_val: 预计最小值
        :param scale: 最大值到最小值区间的分度值
        """
        self.probable_max_val = probable_max_val
        self.probable_min_val = probable_min_val
        self.scale = scale
        self.range_num = int((probable_max_val - probable_min_val) / scale)  # 区间数量

        self.range_list = [[probable_min_val + i * scale, probable_min_val + (i + 1) * scale] for i in
                           range(self.range_num)]  # 数值区间表,左小右大,左闭右开
        self.range_element_count = [0 for _ in range(self.range_num)]  # 落入区间内的数值数,小标与数值区间表对应
        self.real_val_probability_preference_list = [0.5 for _ in range(self.range_num)]  # 实际值值概率偏向(偏向左边)

    def calculate(self, _val):
        """根据输入数值计算估计值"""
        for i in range(self.range_num):
            tmp_range = self.range_list[i]
            if _val in np.arange(tmp_range[0], tmp_range[1]):  # 在区间范围内
                self.range_element_count[i] += 1  # 区间元素个数加一
                self.real_val_probability_preference_list[i] = 1 - (_val - tmp_range[0]) / self.scale  # 概率偏向更新

        max_count_index_list = [i for i, x in enumerate(self.range_element_count) if x == max(self.range_element_count)]
        probable_real_val_list = []
        for i in range(len(max_count_index_list)):
            val_range = self.range_list[max_count_index_list[i]]
            probability_preference = self.real_val_probability_preference_list[max_count_index_list[i]]
            probable_real_val_list.append(
                val_range[0] * probability_preference + val_range[1] * (1 - probability_preference))

        if probable_real_val_list:
            return sum(probable_real_val_list) / len(probable_real_val_list)
        else:
            return 0


def sample_simulator() -> list:
    # 取样模拟
    # import random
    #
    # generate_times = 200
    # max_val = 300
    # min_val = 200
    # period = 20
    # direction_flag = 1
    # ret = [max_val]
    #
    # for i in range(generate_times):
    #     if i % int(period / 2) == 0:
    #         direction_flag = -direction_flag
    #
    #     ret.append(ret[-1] + (max_val - min_val) / int(period / 2) * direction_flag + random.randint(-2, 2))
    #     # ret.append(ret[-1] + (max_val - min_val) / int(period / 2) * direction_flag)

    # import numpy as np
    # generate_times = 200
    # max_val = 1.8
    # min_val = 0.2
    # sigma = 0.04
    # ret = np.random.normal(loc=(max_val + min_val) / 2, scale=sigma, size=generate_times)  # 均值,标准差,尺寸

    import random
    mean_val = 1
    generate_times = 200
    ret = [mean_val + random.uniform(-0.4, 0.4) for _ in range(generate_times)]

    return ret


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    sample_list = sample_simulator()
    probability_filter = ProbabilityFilterClass(1.5, 0.5, 0.02)

    result_record = []
    for j in range(len(sample_list)):
        result = probability_filter.calculate(sample_list[j])
        result_record.append(result)

    plt.plot(sample_list, color="dodgerblue")
    plt.plot(result_record, color="orangered")
    plt.show()
