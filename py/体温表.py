import random


def year_judge(d):  # d为整数
    if d % 400 == 0 or (d % 4 == 0 and d % 100 != 0):
        return 'leap'  # 闰年
    else:
        return 'common'  # 平年


month = eval(input('起始月:'))
day = eval(input('起始日:'))
i = eval(input('天数:'))
l1 = [1, 3, 5, 7, 8, 10, 12]
l2 = [29, 30, 31, 32]
while i != 0:
    t = random.randint(58, 69) * 0.1 + 30
    print('%d月%d日' % (month, day) + '  ' + '%.1f℃' % t)
    i -= 1
    day += 1
    if day in l2:
        if month != 2:
            if month in l1:
                if day == 32:
                    month += 1
                    day = 1
            else:
                if day == 31:
                    month += 1
                    day = 1
        elif month == 2:
            year = eval(input('年份:'))
            if year_judge(year) == 'leap':  # 闰年
                if day == 30:
                    month += 1
                    day = 1
            else:
                if day == 29:
                    month += 1
                    day = 1
    else:
        continue
