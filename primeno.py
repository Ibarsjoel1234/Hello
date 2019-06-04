nn=int(input())
if nn > 1:  
   for i in range(2, nn): 
       if (nn % i) == 0: 
           print("no") 
           break
   else: 
       print("yes") 
  
else: 
   print("no") 
