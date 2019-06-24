name1,name2 = list(map(str,input().split()))
a = set(name1)
b = set(name2)
if a == b:
    print("true")
else:
    print("false")
