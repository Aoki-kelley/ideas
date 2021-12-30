n=int(input('个数:'))
ls=[]
for i in range(n):
    ls.append(input('输入:'))
ls.sort(reverse=False)
for i in range(n-1):
    if ls[i+1].find(ls[i])==0:
        print('invalid')
        break
else:
    print('valid')
