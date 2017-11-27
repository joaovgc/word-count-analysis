from collections import Counter

txt = open("sample.txt", "r")
splitTxt = txt.read().split()
txt.close()

def replaceShit(splitTxt):
	splitTxt = [x.lower() for x in splitTxt]
	for i in range(len(splitTxt)):
		for p in [".", "“", "”", "?", ",", "-", "@", "…", ":", "–", "—", "!", ")", "(", ";", "’s"]:
			if p in splitTxt[i]:
				splitTxt[i] = splitTxt[i].replace(p, "")
			
	return splitTxt
				
def getUniqueWords(splitTxt):
	splitTxt = replaceShit(splitTxt)
	uniqueWords = set(splitTxt)
	return uniqueWords

def getFrequencyList(splitTxt):
	splitTxt = replaceShit(splitTxt)
	return (Counter(splitTxt).most_common())

def listToString(lista):
	string = ""
	for i in lista:
		string += (str(i)+ "\n")
	return string

txt = open("frequency.txt", "w")
freqString = ""
for w in getFrequencyList(splitTxt):
	freqString += str(w) + "\n"
txt.write(freqString)
txt.close()

