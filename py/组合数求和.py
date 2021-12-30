#计算C(1,n)+C(2,n)+...+C(m,n)的值
def fac(a):  #阶乘factoria
    SUM=1
    for i in range(1,a+1):
        SUM*=i
    return SUM

def com(m,n):   #组合combination
    s=0
    if m<=n and m>0:
        return int(fac(n)/(fac(m)*fac(n-m)))
    else:
        return 'invalid'

a=eval(input('输入:'))   #a<=b
b=eval(input('输入:'))
SUM=0
if a<=b and a>0:
    for i in range(1,a+1):
        SUM+=com(i,b)
    print(SUM)
else:
    print('invalid')
