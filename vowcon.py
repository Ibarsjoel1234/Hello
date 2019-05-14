num = str(input())
if num == "a" or num == "e"  or num == "i" or num =="o" or num == "u":
	print("Vowel")
elif num.isalpha():
	print("Consonant")
else:
	print("Invalid")
