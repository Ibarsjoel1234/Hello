arm,num=map(int,input().split())
for i in range(arm,num):
  result=0
  temp=i
  n=len(str(i))
  while temp>0:
    digit=temp%10
    result=result+digit**n
    temp=temp//10
  if i==result:
    print(i,end=" ")
