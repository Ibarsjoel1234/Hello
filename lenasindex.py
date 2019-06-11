aa=input()
aa2=list(map(int,input().split()))
c=d=0
for i in range(0,len(aa2)+1):
    if(i==aa2[i]):
        c=c+1
    else:
        d=d+1
        break
if(d>=1):
    print(d)
