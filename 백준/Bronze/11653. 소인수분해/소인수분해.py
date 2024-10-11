#### 내 풀이 ####
m=int(input())
for x in range(2,m+1):
    if m%x==0: # 약수라면
        while m%x==0: #소인수분해
            m//=x
            print(x)

#### 다른 사람 풀이 ####
n=int(input())
i=2
while n>1:
    if n%i==0:
        n=n//i
        print(i)
    else:
        i+=1

# 차이점 : 나는 for문을 사용해 약수 안에서 while문을 실행한 데 반해, 2부터 1씩 증가해가며 소인수분해를 실행했다. 즉, while문 실행 조건의 최댓값을 지정했는지 유무가 다르다.
# 배울점 : 처음부터 while문을 사용해 불필요한 for문을 실행시키기지 않아 메모리 성능을 약 100KB 절약했다. (그러나 실행 시간은 약 388ms 늦다.)
