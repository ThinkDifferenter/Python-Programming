#  按逗号分隔列表

def f():
    a=[1,2,3,4,5]
    s=','.join(str(c) for c in a)
    print(s)
    
def run():
    f()

run()
