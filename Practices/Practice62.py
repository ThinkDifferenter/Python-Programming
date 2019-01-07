# 查找字符串。　

def searchString():
    baseStr = input('输入基本字符串:')
    patternStr = input('输入要查找的字符串:')

    t=baseStr.find(patternStr)

    if t>=0:
        print('找到了子串位于:',t+1)
    else:
        print('没有找到子串')



if __name__=='__main__':
    searchString()

    
