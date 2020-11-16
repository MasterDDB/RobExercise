
print("hello world")

f = open("alice.txt", "r")
#text = f.read()
#print(text)

#read in all lines from book and iterate through each line to print each word
lines = f.readlines()
lineNumber = 0
for line in lines:
    words = line.split()
    if lineNumber<500 and lineNumber>=490:
        for word in words:
            print("line:",lineNumber, "word:", word)
    lineNumber = lineNumber + 1

print("#lines in book is:",lineNumber)

f.close()

