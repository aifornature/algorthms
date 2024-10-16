def fact(n,a,b,arr): 
    start=n//3
    for x in range(start):
        for y in range(start):
            arr[start+a+x][start+b+y]=' '
    if start != 1:
        for x in range(3):
            for y in range(3):
                arr=fact(start,a+start*x,b+start*y,arr)
        start//=3
    return arr

n=int(input())
tarr=[['*' for _ in range(n)] for _ in range(n)]
tarr=fact(n,0,0,tarr)
for x in range(n):
    print(''.join(tarr[x]))