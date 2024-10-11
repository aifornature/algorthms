n=int(input())
if n!=1:
    x,y=set(),set()
    for _ in range(n):
        a,b=map(int,input().split())
        x.add(a)
        y.add(b)
    print((max(x)-min(x))*(max(y)-min(y)))
else:
    print(0)