val=int(input())
var,var1=list(map(int,input().split()))
for valu in range(var,var1):
    if(valu==val):
        print("yes")
        break
else:
    print("no")
