a= int(input())
b = int(input())
for row in range(0,a):
    for col in range(0,b):
        if(row==0 and col%3!=0) or(row ==1 and col%3 ==0) or (row-col == 2) or (row+col == 8):
            print("*",end="")
        else:
            print(end=" ")
    print()
# if a=6 and b=7 the heart shape star will displayed
