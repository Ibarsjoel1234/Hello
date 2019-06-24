user,val = map(str,input().split())
if user == val:
    print("D")
elif (user == "P" and val == "R") or (user == "R" and val == "P"):
    print("P")
elif (user == "P" and val == "S") or (user == "S" and val == "P"):
    print("S")
elif (user == "S" and val == "R") or (user == "R" and val == "S"):
    print("R")
