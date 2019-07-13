a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = sorted(c)
if b == d:
    print("yes")
else:
    print("no")
