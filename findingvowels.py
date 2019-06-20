values=input()
vow={'a','e','i','o','u'}
for i in range(0,len(values)):
    if values[i] in vow:
        print("yes")
        break
else:
    print("no")
