# 输出一个随机数。

import random

def randomMaker(low,up):
    return random.uniform(low,up)


def run():
    low = int(input('Please input low:'))
    up= int(input('Please input up:'))

    if low >= up:
        print('Input Error!')
        return 
        
    print(randomMaker(low,up))



run()
    
