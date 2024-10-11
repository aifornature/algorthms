m=int(input())
for x in range(2,m+1):
    if m%x==0:
        while m%x==0:
            m//=x
            print(x)