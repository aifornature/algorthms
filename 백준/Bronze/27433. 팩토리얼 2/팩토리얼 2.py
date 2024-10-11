#### 내 풀이 ####
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input())))

#### 다른 사람 풀이 ####
import sys
n = int(sys.stdin.readline())
k = 1
for i in range(1, n+1):
    k *= i
print(k)

#### 회고 ####
# 차이점 : 나는 재귀함수를 정의하고 풀었다면, 다른 사람은 for문을 사용해서 풀었다.
# 느낀점 : 문제의 의도가 재귀함수였기에 내 풀이가 더 적합했다고 생각한다.
