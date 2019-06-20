var,var1=map(int,input().split())
mul=var*var1
for i in range(0,mul+1):
    if(i**2)== mul:
        print("yes")
        break
else:
    print("no")
