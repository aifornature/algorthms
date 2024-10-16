def binary_search(target,data,start,end):
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