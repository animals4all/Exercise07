from string import punctuation
from sys import argv

# Create a list of all punctuation minus the hyphen
punctuationList = list(punctuation.replace("-", ""))

def main():
	# Get the name of the script and the name of the file from the command line
	script, filename = argv

	text = open(filename)
	contents = text.read()
	text.close()

	# Remove newline characters and seperator hypens from the file contents, and split the
	# contents into a list of all the words in it
	wordList = contents.replace("\n", " ").replace(" - ", " ").replace("--", " ").split(" ")

	# Create a dictionary with each of the words and the number of times that word occurs
	wordDict = {}
	for word in wordList:
		# Remove any punctuation from the file contents that doesn't act as a seperator for
		# two different words
		for char in punctuationList:
			word = word.replace(char, "")

		# Don't count words that are blank strings, such as empty lines in a file
		if word != "":
			word = word.lower()

			if word in wordDict:
				wordDict[word] += 1
			else:
				wordDict[word] = 1

	# Create a dictionary with the numbers of word occurences as the keys and the words that
	# occur that many times as the values
	arrangedItems = {}
	for key, value in wordDict.iteritems():
		if value in arrangedItems:
			arrangedItems[value].append(key)
		else:
			arrangedItems[value] = [key]

	# Print the words and their occurences in order of frequency, with words having the same
	# frequency being sorted alphabetically
	for num in sorted(arrangedItems):
		words = arrangedItems[num]
		words.sort()
		for word in words:
			print word + " " + str(num)

if __name__ == "__main__":
	main()
