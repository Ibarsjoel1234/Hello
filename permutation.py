from itertools import permutations
txt=input()
var=permutations(txt)
for per in list(set(var)):
    print(''.join(per))
