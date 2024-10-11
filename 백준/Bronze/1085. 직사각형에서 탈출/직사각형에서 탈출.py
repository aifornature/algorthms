#### 내 풀이 ####
x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y)) # 직사각형 각 면까지의 거리 중 최소값 선택

#### 다른 사람 풀이 ####
# 입력 받기
x, y, w, h = map(int, input().split())

# 각 경계까지의 거리 계산
distance_to_left = x
distance_to_right = w - x
distance_to_bottom = y
distance_to_top = h - y

# 최소 거리 계산
min_distance = min(distance_to_left, distance_to_right, distance_to_bottom, distance_to_top)

# 결과 출력
print(min_distance)

#### 회고 ####
# 차이점 : 각 파라미터 명을 직관적으로 지정하고 단계를 거쳐 작성하여 보는 사람으로 하여금 명확하게 이해가 가능하게 하고 , 나는 파라미터 지정없이 작성하여 나만이 알아볼 수 있다는 점이 실수다.
# 배울점 : 무엇을 하고자 하는지 눈에 명확히 들어온다. 코드를 효율적으로 작성하는 것의 관점(코드 길이에 중점와 설명력 중 어느 것에 초점을 맞출지)에 대해 고민해 보는 기회였다.
