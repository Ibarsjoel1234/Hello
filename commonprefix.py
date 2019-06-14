bb=int(input())
m=[]
for i in range(0,bb):  
    dd=input()
    m.append(dd)
list=[]
for i in zip(*m):
    if (i.count(i[0])==len(i)): 
        list.append(i[0])
    else:
        break
print(''.join(list))
