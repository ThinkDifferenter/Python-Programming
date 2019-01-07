import re

def f():
    text = '.525heart.com\n'   #在系统中表示为   .525heart.com换行
    patternstr = '\.525heart.com\n'
    #  代码里的书写为   \.525heart.com\n
    #  系统识别为   \.525heart.com换行     字符串转义能识别\n，但是无法识别\.就原样保存
    #  正则识别为  .525heart任意字符com换行    正则转义能识别\.和.

    patternstr = r'\.525heart.com\n'
    #  代码里的书写为   \.525heart.com\n
    #  系统识别的字符串为   \.525heart.com\n   原样保存
    #  正则识别为  .525heart任意字符com换行   正则转义能识别\.和.和\n

    print(patternstr)
    pattern = re.compile(patternstr)

    result = re.search(pattern,text)
    print(result.group())


def f2():
    # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
    pattern = re.compile(r'hello')

    # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
    result1 = re.match(pattern, 'hello')
    result2 = re.match(pattern, 'helloo world!')
    result3 = re.match(pattern, 'helo world!')
    result4 = re.match(pattern, 'hello world!')

    # 如果1if result1:
        # 使用Match获得分组信息
        print(result1.group())
    else:
        print('1匹配失败！')

    # 如果2匹配成功
    if result2:
        # 使用Match获得分组信息
        print(result2.group())
    else:
        print('2匹配失败！')

    # 如果3匹配成功
    if result3:
        # 使用Match获得分组信息
        print(result3.group())
    else:
        print('3匹配失败！')

    # 如果4匹配成功
    if result4:
        # 使用Match获得分组信息
        print(result4.group())
    else:
        print('4匹配失败！')





if __name__=='__main__':
    f2()
