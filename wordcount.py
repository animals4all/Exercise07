from sys import argv

#script, filename = argv
filename = open("twain.txt")
contents = filename.read()

# Remove newline characters
wordStr = contents.replace("\n", " ")
# Turn from string into list of words
wordList = wordStr.split(" ")

wordDict = {}
for word in wordList:
	if word in wordDict:
		wordDict[word] += 1
	else:
		wordDict[word] = 1

for key, value in wordDict.iteritems():
	print key + " " + str(value)
