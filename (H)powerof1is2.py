no, pow =  list(map(int,input().split()))
while no>1:
    no = no/pow
if no ==1:
    print("yes")
else:
    print("no")
