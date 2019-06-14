no,no1=list(map(int,input().split()))
no2,no3=list(map(int,input().split()))
no4,no5=list(map(int,input().split()))
no6,no7=list(map(int,input().split()))
a=no3-no1
b=no5-no7
c=no4-no2
d=no6-no
if(a==b==c==d):
    print("yes")
else:
    print("no")
    
