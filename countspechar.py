strings=input()
counts=0
for j in strings:
    if(j.isalpha()!=True and j.isdigit()!=True):
        counts=counts+1
print(counts)
