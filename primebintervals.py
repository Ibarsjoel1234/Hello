to,the=list(map(int,input().split()))
for prime in range(to,the):
  if prime>1:
    for n in range(2,prime):
      if(prime%n)==0:
        break
    else:
      print(prime,end=" ")
