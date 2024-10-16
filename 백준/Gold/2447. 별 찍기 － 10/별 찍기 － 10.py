#### 내 풀이 ####
def fact(n,a,b,arr): # 재귀함수 정의 
    start=n//3
    for x in range(start): # 가장 큰 공백의 정사각형 
        for y in range(start):
            arr[start+a+x][start+b+y]='  '
    if start != 1: # 주위를 둘러싸는 공백의 정사각형 
        for x in range(3):
            for y in range(3):
                arr=fact(start,a+start*x,b+start*y,arr)
        start//=3
    return arr

n=int(input())
tarr=[['*' for _ in range(n)] for _ in range(n)] # 전체 리스트
tarr=fact(n,0,0,tarr)
for x in range(n): #출력
    print(''.join(tarr[x]))

#### 다른 사람 풀이 ####
n,s,i=int(input()),'*',1
while i<n:k=[c*3 for c in s];s=k+[c+' '*i+c for c in s]+k;i*=3
print(*s)

#### 회고 ####
# 차이점 : 나는 리스트와 재귀함수를 정의하고 풀었다면, 이 풀이는 while문과 문자를 이용해 3의 배수라는 점을 정확하게 이용해서 풀었다. 또한, 이 풀이는 한줄로 출력되는 반면, 내 풀이는 출력 예시 그대로 출력된다.
# 배울점 : n과 i의 크기 차이를 조건으로 이용해 불필요한 재귀함수 사용없이 간단히 정답을 도출함.
