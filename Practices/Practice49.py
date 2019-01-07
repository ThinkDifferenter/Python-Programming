# 使用lambda来创建匿名函数。

Minmum=lambda x,y:(x>y)*y+(x<y)*x
Maxmum=lambda x,y:(x>y)*x+(x<y)*y
    
if __name__ == '__main__':
    a = 10
    b = 20
    print ('The largar one is %d' % Maxmum(a,b))
    print ('The lower one is %d' % Minmum(a,b))
