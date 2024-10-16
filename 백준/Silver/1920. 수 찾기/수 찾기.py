#### 내 풀이1 ####
def binary_search(target,data,start,end): #이진탐색 재귀함수
    if start>end:
        return 0
    mid=(start+end)//2
    if data[mid]<target:
        return binary_search(target,data,mid+1,end)
    elif data[mid]>target:
        return binary_search(target,data,start,mid-1)
    else:
        return 1
  
n,a=int(input()), list(map(int,input().split()))
m,b=int(input()),list(map(int,input().split()))
a.sort()
for x in b:
    print(binary_search(x,a,0,len(a)-1))

#### 내 풀이2 #### => 오답. 
n,a=int(input()), list(map(int,input().split()))
m,b=int(input()),list(map(int,input().split()))
for x in b:
    print(int(x in a))

#### 다른 사람 풀이 ####
input()
A = set(map(int, input().split()))
input()
B = list(map(int, input().split()))

for X in B:
    print(int(X in A))

#### 회고 ####
# 차이점 
### 풀이1 : 나는 이진탐색으로 문제를 풀었고, 이 사람은 boolen형의 특성을 사용해 문제를 풀었다.
### 풀이2 : a의 자료형이 list가 아닌 set여야 한다. => list : 순서가 중요하므로 시간복잡도가 평균 O(n)임. / set : 순서가 중요하지 않으므로 시간복잡도가 평균 O(1)임.
# 배울점 : 자료형에 따라 시간복잡도에 큰 차이가 있어 오답, 정답이 나뉠 수 있음을 느끼고 복잡도 분석이 중요하다는 점을 깨닫는 계기가 됨.
