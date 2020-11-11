
print("hello world")

f = open("alice.txt", "r")
text = f.read()
print(text)

i=0	#this is a numerical, integer; start counting at 0	
charactersInBook=[]	#this is a list data structure with iniitial length 0
print(charactersInBook)
for character in text:
	if i<10:
		print(character)
	i=i+1	#i++; add 1 to variable i
	if character in charactersInBook:
		#disregard
		pass
	else:
		charactersInBook.append(character)

#chartersInBook=['a','b','c']
print("Total number of characters in the book",i)
print('In order of occurence in the book:',charactersInBook)
charactersInBook.sort()
print('Alphabetically sorted:',charactersInBook)

f.close()

