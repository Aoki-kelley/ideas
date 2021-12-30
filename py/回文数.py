def judge(s):  #s为字符串
    l=len(s)//2
    a,b=0,-1
    i=0
    while a<l:
        if s[a]==s[b]:
            i+=1
            a+=1
            b-=1
        else:
            a+=1
            b-=1
            continue
    if i==l:
        return True

x=eval(input('从:'))
y=eval(input('至:'))
i=0
for n in range(x,y+1):
    n_s=str(n)
    if judge(n_s):
        print(n,end=' ')
        i+=1
    else :
        continue
print('\n'+'共%d个'%i)
    
