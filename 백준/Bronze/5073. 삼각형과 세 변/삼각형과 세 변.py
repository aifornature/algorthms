    #### 내 풀이 ####
    while True:
    ans=sorted(list(map(int,input().split())),reverse=False)
    answer=''
    if ans[0]!=0 and (ans[0]+ans[1])<=ans[2]:
        answer='Invalid'
    elif ans.count(ans[0])==3:
        if ans[0]==0:
            break
        else:
            answer='Equilateral'
    else:
        for t in range(len(ans)):  
            if ans.count(ans[t])==2:
                answer='Isosceles'
                break
            answer='Scalene'
    print(answer)
    #### 다른 사람 풀이 ####
    while True :
      a, b, c = map(int, input().split())
      if a == b == c == 0 :
        break
      if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)) :
        print("Invalid")
      elif a == b == c :
        print('Equilateral')
      elif a == b or b == c or a == c :
        print("Isosceles")
      else :
        print("Scalene")
    #### 회고 ####
    # 차이점 : -
    # 배울점 : -
