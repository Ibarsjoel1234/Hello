# integer to roman values (IBM Online Qns)

romanvalues = {'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX','10':'X','150':'L'}
str = input("Enter the Integer Value: ")
if(str in romanvalues):
    if(str == '1'):
        print(romanvalues['1'])
    elif(str=='2'):
        print(romanvalues['2'])
    elif(str =='3'):
        print(romanvalues['3'])
    elif (str == '4'):
        print(romanvalues['4'])
    elif (str == '5'):
        print(romanvalues['5'])
    elif (str == '6'):
        print(romanvalues['6'])
    elif (str == '7'):
        print(romanvalues['7'])
    elif (str == '8'):
        print(romanvalues['8'])
    elif (str == '9'):
        print(romanvalues['9'])
    elif (str == '10'):
        print(romanvalues['10'])
    elif (str == '150'):
        print(romanvalues['150'])
else:
    print("Beyond limits")
