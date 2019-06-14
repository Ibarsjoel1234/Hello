no=int(input())
num=list(map(int,input().split()))
num.sort()
print(min(num),max(num),end=" ")
