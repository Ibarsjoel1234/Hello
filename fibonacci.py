x=int(input(""))
aa=0
bb=1
for i  in range(x):
    c=aa+bb
    aa=bb
    print(bb,end=' ')
    bb=c
