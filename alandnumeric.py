pp=input()
a=0
bb=0
for i in  pp:
    if i.isnumeric():
        a=1
    if i.isalpha():
        b=1
if a==1 and b==1:
    print("yes")
else:
    print("no")
