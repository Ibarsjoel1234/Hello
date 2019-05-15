a=int(input())

b=int(input())

c=input("Enter the operation")

if c=="1":
    
	c=a+b
    
	print(c)

elif c=="2":
    
	c=a-b
    
	print(c)

elif c=="3":
    
	if b == 0:
        
		print("Infinite")
    
	else:
        
		c=a/b
        
		print(c)

else:
    
	print("No operation is found")