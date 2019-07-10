import re
def likeStrip(*arg):
	temp = list(arg)
	
	regx2 = re.compile(r"^\s*|\s*$")
	if len(temp)>1:
		regx1 = re.compile(temp[1])
		for i in regx1.finditer(temp[0]):
			temp[0] = re.sub(i.group(),"",temp[0])
	else:
		for i in regx2.finditer(temp[0]):
			temp[0] = re.sub(i.group(),"",temp[0])
	return temp[0]					

def isValidPass(text):
	regx = re.compile(r"^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{4,})$")
	if regx.fullmatch(text):
		return True
	else:
		return False	

def removeExtraWhiteSpace(text):
	regx = r"\s+"
	
	#temp = re.sub(regx," ", text)
	text = re.sub(regx," ",text)
	return text
def doReplace(text):
	regx = r"the" #write the regex here to match the portion to be replaced.
	text = re.sub(regx,"",text)
	return text
#this function counts any characters
def countCharacters(text):
	regx = r"."
	units = re.findall(regx,text)
	return len(units)
def countWords(text):
	regx = r"\W+"
	units = re.split(regx,text)
	return len(units)
test = "I fluck you"
print(likeStrip(test,"u"))
print(likeStrip("                        hi there			"))