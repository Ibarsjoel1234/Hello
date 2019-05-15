from decimal import *
a=str(input())
b=str(input())
c=input("Enter the operation")
if c=="1":
    if a.isalpha():
        print("Throw exception: a")
    elif b.isalpha():
        print("Throw exception: b")
    else:
        a=Decimal(a)
        b=Decimal(b)
        c=a+b
        print(c)
elif c=="2":
  if a.isalpha():
    print("Throw expection : a")
  elif b.isalpha():
    print("Thow expection: b")
  else:
    a=Decimal(a)
    b=Decimal(b)
    c=a-b
    print(c)
elif c=="3":
  if a.isalpha():
      print("Throw exception: a")
  elif b.isalpha():
      print("Throw expection: b")
  if b == 0:
      print("Infinite")
  else:
      a=Decimal(a)
      b=Decimal(b)
      c=a/b
      print(c)
else:
    print("No operation is found")
