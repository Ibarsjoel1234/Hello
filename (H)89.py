from collections import OrderedDict
foo =str(input())
result = "".join(OrderedDict.fromkeys(foo))
print(result[::-1])

# print all characters in strings only once in reverse order
