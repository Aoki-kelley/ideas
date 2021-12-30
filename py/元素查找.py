def find(x,l):
    a=-1
    count=l.count(x)
    l_p=[]
    while count!=0:
        a=l.index(x,a+1)
        l_p.append(a)
        count-=1
    else:
        print(l_p)

if __name__=='__main__':
    x=eval(input('查找:'))
    n=eval(input('元素个数:'))
    i=1
    l=[]
    while i<=n:
        y=eval(input('输入:'))
        l.append(y)
        i+=1
    find(x,l)
