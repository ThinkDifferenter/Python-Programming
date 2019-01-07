# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.
# 编程找出1000以内的所有完数。

def f(n):
      l=[]
      while n>1:
          for i in range(2,n+1):
              if n%i==0:
                   n=int(n/i)
                   l.append(i)
                   break
      return l


def run():
    for i in range(1,1001):
        t=sum(f(i))
        if t==i:
            print(i)

run()
