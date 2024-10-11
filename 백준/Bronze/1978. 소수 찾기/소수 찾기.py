#### 내 풀이 ####
n=int(input())
an=[x for x in map(int,input().split()) if x != 1] # 소수의 개수가 출력값이므로 1은 제외 (소수는 2 이상의 자연수 중 1과 자기자신으로 나뉘어지는 수)
q=set() # 합성수 집합
for x in an:
    for y in range(2,x+1):
        if x%y==0 and y!=x:
            q.add(x)
print(len([x for x in an if x not in q]))

#### 다른 사람 풀이 ####
a=int(input())
b=input().split()
count=0
for i in range(a):
    prime=0
    for j in range(int(b[i])):
        if int(b[i])%(j+1)==0:
            prime+=1
    if prime==2:
        count+=1
print(count)

# 차이점 : 모든 변수를 사용하며, 자신의 약수 개수를 카운트 한다는 점에서 나와 다르다. 나는 자기자신이 아닌 약수가 발견되는 즉시 for문을 중단한다.
# 배울점 : 모든 변수를 사용했다는 점.
