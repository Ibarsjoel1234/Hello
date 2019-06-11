starts,ends=input().split()

starts=int(starts)+1

ends=int(ends)

for num in range(starts,ends): 
    if(num%2 != 0): 
        print(num, ends=" ")
