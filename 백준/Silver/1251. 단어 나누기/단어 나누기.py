word =list(input())
li = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a,b,c= word[:i], word[i:j],word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        li.append(''.join(a+b+c))
        li.sort()
print(li[0])