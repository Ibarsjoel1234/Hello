nn= int(input(""))
ss= 0
t= nn
while t > 0:
   d = t % 10
   ss += d ** 3
   t //= 10
if n == ss:
   print("yes")
else:
   print("no")
