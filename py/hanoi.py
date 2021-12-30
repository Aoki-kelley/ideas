def hanoi(n,src,tmp,dst):
    if n==1:
        print('%d:%s→%s'%(n,src,dst))
    else:
        hanoi(n-1,src,dst,tmp)
        print('%d:%s→%s'%(n,src,dst))
        hanoi(n-1,tmp,src,dst)
        
if __name__=='__main__':
    n=int(input('输入:'))
    hanoi(n,'A','B','C')
