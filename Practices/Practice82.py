# 八进制转换为十进制

def eight2ten():
    n = input("请输入一个八进制数:")
    n = reversed(n)
    s = 0
    for idx,i in enumerate(n):
        s += int(i) * pow(8, idx)
    print (s)


if __name__=='__main__':
    eight2ten()

    
