from itertools import permutations
txt=str(input())
var=permutations(txt)
for per in list(var):
    print(''.join(per))
