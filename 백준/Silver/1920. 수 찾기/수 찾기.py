input()
A = set(map(int, input().split()))
input()
B = list(map(int, input().split()))

for X in B:
    print(int(X in A))