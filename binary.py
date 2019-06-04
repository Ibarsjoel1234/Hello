def check_str(s):
	pp = set(s)
	s = {'0','1'}
	if s==pp or pp=={'0'} or pp=={'1'}:
		print("yes")
	else:
		print("no")
s = input()
check_str(s)
