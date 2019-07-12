matrix=[]
R=5
C=5
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(j+1) 
    
    matrix.append(a) 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
