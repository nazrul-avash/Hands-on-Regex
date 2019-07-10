import re
def isValid(text):
	pattern = r"^[A-Z]{5}\d{4}[A-Z]$"
	result = re.match(pattern,text)
	if result:
		return "YES"
	else:
		return "NO"	
case = int(input())
for x in range(case):
	testStr = input()
	print(isValid(testStr))
