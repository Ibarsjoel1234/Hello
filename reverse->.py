no=input()
n=map(int,input().split())
at=[]
for rev in n:
    at.append(rev)
at.reverse()
print(*at,sep="->")
