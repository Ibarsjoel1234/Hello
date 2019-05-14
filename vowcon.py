num = str(input())
if num == "a" or num == "e"  or num == "i" or num =="o" or num == "u":
	print("Vowels")
elif num.isalpha():
	print("Consonant")
else:
	print("Invalid")
