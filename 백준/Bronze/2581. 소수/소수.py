m,n=int(input()),int(input())
q=set()
for x in range(m,n+1):
    for y in range(2,x+1):
        if x%y==0 and y!=x:
            q.add(x)
clear=[x for x in range(m,n+1) if x not in q if x != 1]  
if len(clear)==0:
    print(-1)
else:
    print(sum(clear),min(clear))