import re
import pyperclip
emailRegx= re.compile(r'''[A-Za-z0-9._%+-]+
						  @
						  [a-zA-Z0-9.-]+
						  (\.[a-zA-Z]{2,4})'''
						  ,re.VERBOSE)
text =pyperclip.paste()
match = []
temp= ""
for i in emailRegx.finditer(text):
	match.append(i.group())
for i in match:
	temp += i+"\n"
pyperclip.copy(temp)	