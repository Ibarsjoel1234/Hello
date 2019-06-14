no=int(input())
num=list(map(int,input().split()))
at=0
while len(num)!=0:
    if len(num)!=1:
        at.append(max(num))
        at.append(min(num))
        num.remove(max(num))
        num.remove(min(num))
    else:
        at.append(max(num))
        num.remove(min(num))
print(*at,end=" ")
