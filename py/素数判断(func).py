'''输入若干整数（输入0结束），每个整数输入完毕后，马上输出该整数是否为素数。
   要求判断一个整数是否为素数的功能用一个函数实现。'''
def f(n):
    m=int(n**0.5)
    for i in range(2,m+1):
        if n%i == 0:
            print('No')
            break
    else:
        print('Yes')

while True:
    n=eval(input('输入:'))
    if n==0:
        break
    elif n<2:
        print('Invalid')
    else:
        f(n)
