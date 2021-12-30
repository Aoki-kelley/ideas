while True:
    n=eval(input('输入一个大于一的整数：'))
    if n > 0 and type(n) != float:
        m=int(n**0.5)
        if n > 1:
            for i in range(2,m+1):
                if n%i == 0:
                    print('%d不是素数'%n)
                    break
            else:
                print('%d是素数'%n)
        else:
            print('结束')
            break
    else:
        print('结束')
        break
