#### 내 풀이 ####
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

#### 다른 사람 풀이 ####
M = int(input())
N = int(input())
a = []

for i in range(M, N+1):
    count = 0
    for j in range(i+1):
        if(i % (j+1) == 0):
            count += 1
    if(count == 2):
        a.append(i)
if(len(a) == 0):
    print(-1)   
else:
    print(sum(a))
    print(a[0])

# 차이점 : 소수찾기 1978문제와 같다. 
# 배울점 : X
