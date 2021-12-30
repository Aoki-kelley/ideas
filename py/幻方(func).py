def is_magicsquare(ls):
    element_set=set()
    n=len(ls)
    for r in range(n):
        for c in range(n):
            element_set.add(ls[r][c])
    if len(element_set)<(n*n):
        return False

    sum_set=set()
    for r in range(n):
        SUM=0
        for c in range(n):
            SUM+=ls[r][c]
        sum_set.add(SUM)
    if len(sum_set)>1:
        return False
        
    for c in range(n):
        SUM=0
        for r in range(n):
            SUM+=ls[r][c]
        sum_set.add(SUM)
    if len(sum_set)>1:
        return False
        
    SUM=0
    for r in range(n):
        SUM+=ls[r][r]
    sum_set.add(SUM)
    if len(sum_set)>1:
        return False
    
    SUM=0
    for r in range(n):
        SUM+=ls[r][n-1-r]
    if sum_set.add(SUM)>1:
        return False
    
    return True
    
if __name__=='__main__':
    n = eval(input('度数:'))
    ls = []
    for i in range(n):
        ls.append(list(eval(input('输入:'))))
    #print(ls)
    if is_magicsquare(ls)==True:
        print('Yes')
    else:
        print('No')
