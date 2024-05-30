'''
Lab 8: Refactor word_count
Rewrite the word_count program from section 8.7 to make it shorter. 
You may want to look at the string and list operations already discussed, as well as think about different
ways to organize the code. You may also want to make the program smarter so that only
alphabetic strings (not symbols or punctuation) count as words.
'''

line_count = 0
word_count = 0
char_count = 0

with open('word_count.txt') as infile:
	for line in infile:
		line_count += 1
		char_count += len(line)
		words = line.split()
		word_count += len(words)

print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))