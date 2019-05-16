from decimal import *
a=str(input())
b=str(input())
#if a.isalpha() and b.isalpha():
 # print("Both a and b are alphabet")
  #exit()
c=input("Enter the operation\t")
if c=="1":
    if a.isalpha and b.isalpha():
      print("Both a and b are expection")
      exit()
    elif a.isalpha():
        print("Throw exception: a")
    elif b.isalpha():
        print("Throw exception: b")
    elif a.isalpha() and b.isalpha():
        print("Both a and b is alphabet")
    else:
        a=Decimal(a)
        b=Decimal(b)
        c=a+b
        print(c)
elif c=="2":
  if a.isalpha() and b.isalpha():
    print("Both a and b are alphabet")
    exit()
  elif a.isalpha():
    print("Throw expection : a")
  elif b.isalpha():
    print("Thow expection: b")
  else:
    a=Decimal(a)
    b=Decimal(b)
    c=a-b
    print(c)
elif c=="3":
  if a.isalpha() and b.isalpha():
    print("Both a and b are alphabet")
  elif a.isalpha():
      print("Throw exception: a")
  elif b.isalpha():
      print("Throw expection: b")
  elif b == "0":
      print("Infinite")
  else:
      a=Decimal(a)
      b=Decimal(b)
      c=a/b
      print(c)
else:
    print("No operation is found")
