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
