import re
def findHackerrank(text):
	flag = 0
	check1 = r"^hackerrank"
	check2 = r"hackerrank$"
	if re.search(check1,text) and re.search(check2,text):
		flag = 0
	elif re.search(check1,text):
		flag = 1
	elif re.search(check2,text):
		flag = 2
	else:
		flag = -1
	return flag				 
line = "hackerrank"
print(findHackerrank(line))