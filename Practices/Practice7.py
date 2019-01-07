# 将一个列表的数据复制到另一个列表中
import copy

#浅拷贝
a = [1, 2, 3]
b = a[:]
print(b)

#深拷贝此时a变化c跟着变化
c=copy.deepcopy(a)
print(c)

c[0]=0;
print(a)



