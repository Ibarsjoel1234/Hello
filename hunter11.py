txt=str(input())
var=txt.split()
for letter in var:
    print(letter[::-1],end=" ")

