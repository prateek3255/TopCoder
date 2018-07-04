n=int(input())
l=list(map(int,input().split()))
# print(n,l)
m=[]
for i in l:
    if i<0:
        m.append(i)
for i in m:
    l.remove(i)
print(sum(l),len(l))

