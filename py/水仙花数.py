beg=eval(input('起始：'))
end=eval(input('结束：'))
if beg in range(100,1000) and end in range(100,1000):
    i=0
    for n in range(beg,end+1):
        n_s=str(n)
        n1=int(n_s[0])
        n2=int(n_s[1])
        n3=int(n_s[2])
        if n1**3+n2**3+n3**3==n:
            i+=1
            print(n)
        else:
            continue
    if i==0:
        print('Not Found.')
else:
    print('输入有误。')
