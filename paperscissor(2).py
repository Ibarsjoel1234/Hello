def cll_val():
    user,val = map(str,input().split())
    if user == val:
        print("D")
    elif (user == "Paper" and val == "Rock"):
        print("User is winner")
    elif (user == "Paper" and val == "Scissor"):
        print("val is the winner")
    elif (user == "Rock" and val == "Paper"):
        print("Val is the winner")
    elif (user == "Scissor" and val=="Paper"):
        print("User is winner")
    elif (user =="Rock" and val =="Scissor"):
        print("User if the winner")
    elif (user == "Scissor" and val =="Rock"):
        print("Val is the winner")
print("Start Play")
cll_val()
print("Play again")
cll_val()
