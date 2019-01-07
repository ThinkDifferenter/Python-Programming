# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import re

def f():
    
    s=input('Please input a string:')

    letters=0
    space=0
    digit=0
    others=0

    for i in range(0,len(s)):
        t=s[i]
        if t.isalpha() :
            letters +=1
        elif t.isdigit() :
            digit +=1
        elif t.isspace() :
            space +=1
        else:
            others +=1
    print('letters:',letters,'space:',space,'digit',digit,'others',others)

def f2():
    s=input('Please input a string:')

    letters=0
    space=0
    digit=0
    others=0

    #正则表
    for i in range(0,len(s)):
        t=s[i]
        if re.match('\d',t) :
            digit +=1
        elif re.match('[a-zA-Z]',t) :
            letters +=1
        elif re.match('\s',t) :
            space +=1
        else:
            others +=1
            
    print('letters:',letters,'space:',space,'digit',digit,'others',others)

    
def run():
    f2()

run()
