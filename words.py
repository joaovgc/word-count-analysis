from collections import Counter

from tkinter import *

txt = open("ward.txt", "r")
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

f = getFrequencyList(splitTxt)[:3000]
root = Tk()
# Começo do loop.; 

Lb1 = Listbox(root, height=45, width=15, font=("", 14))

i =1
for w in f:
	Lb1.insert(i, w)
	i += 1
	
Lb1.pack()

# Fim do loop;
root.mainloop()
