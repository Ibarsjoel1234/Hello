a=input()
if len(a)%2!=0:
    s=int(len(a)/2)
    s1=a[:s]
    s2=a[s+1:len(a)]
    print(s1+'*'+s2)
else:
    s=int(len(a)/2)
    s1=a[:s-1]
    s2=a[s+1:len(a)]
    print(s1+'**'+s2)
