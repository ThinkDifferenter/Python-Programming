# 对10个数进行排序。

# 冒泡排序
def bubbleSort(l):
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l
    

# 选择排序
def selectSort(l):
    for i in range(len(l)-1):
        min = i     #记录最小元素下标
        for j in range(i+1,len(l)):
            if l[min]>l[j]: #寻找最小元素下标
                min = j
            if min != i:
                l[i],l[min] = l[min],l[i]   #交换最小元素位置
    return l


# 插入排序
def insertSort(l):
    for i in range(0,len(l)):
        if l[i]<l[i-1]:
            index=i
            tmp=l[i]
            while index>0 and l[index-1]>tmp:
                l[index] = l[index-1]
                index -= 1
            if index != i:
                l[index] = tmp
    return l

def shellSort(list1):
    # 设定步长
    step = len(list1)//2
    while step > 0:
        for i in range(step, len(list1)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and list1[i-step] > list1[i]:
                list1[i], list1[i-step] = list1[i-step], list1[i]
                i -= step
        step = step//2   #步长值改为之前的二分之一

# 更多排序算法：https://blog.csdn.net/lm_is_dc/article/details/80048449


def f():
    l=[]
    for i in range(3):
        t=input('请输入%d个数:'%(i+1))
        l.append(t)
    #l.sort()
    #bubbleSort(l)
    #selectSort(l)
    #insertSort(l)
    
    return l
    
def run():
    print(f())

run()
    
