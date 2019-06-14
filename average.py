aa=int(input())
l=list(map(int,input().split()))
if aa==len(l):
  s=sum(l)
  b=s//aa
print(b)
