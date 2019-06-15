from itertools import permutations
txt=input()
var=permutations(txt)
for per in list(var):
    print(''.join(per))
