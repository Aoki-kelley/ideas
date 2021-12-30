n=eval(input('输入：'))
count=0
for ten in range(n//10+1):
        for five in range((n-ten*10)//5+1):
            count+=1
            one=n-ten*10-five*5
            print('%d,%d,%d'%(ten,five,one))
print(count)
