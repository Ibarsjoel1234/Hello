from collections import OrderedDict
foo =str(input())
result = "".join(OrderedDict.fromkeys(foo))
print(result)
