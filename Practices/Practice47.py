# 两个变量值互换。

def exchange(a,b):
    a,b = b,a
    return a,b
    
def run():
    print(exchange(2,3))


run()
