#### 내 풀이 ####
x,y=set(),set()
for _ in range(int(input())):
    a,b=map(int,input().split())
    x.add(a)
    y.add(b)
print((max(x)-min(x))*(max(y)-min(y)))

#### 다른 사람 풀이 ####
X,Y=[],[]
for _ in range(int(input())):
  x,y=map(int,input().split()) 
  X.append(x)
  Y.append(y)
print((max(X)-min(X))*(max(Y)-min(Y)))

#### 회고 ####
# 차이점 : 자료형이 집합이나 리스트냐의 차이점이 있다. 리스트 풀이의 메모리 / 시간 = 35060/1264, 집합 풀이의 메모리 / 시간 = 33684/1276
# 배울점 : 집합 자료형일 경우 리스트에 비해 메모리를 약 14kb덜 차지하고 시간은 12ms 늦게 실행된다. 즉, 시간 대비 메모리 효율이 27.7, 26.3으로 집합 자료형이 더 효율적이다. 
