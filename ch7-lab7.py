'''
Lab 7: Word Counting
In the previous lab, you took the text of the first chapter of Moby Dick, normalized the case, 
removed punctuation, and wrote the separated words to a file. 
In this lab, you read that file, use a dictionary to count the number of times each word occurs, 
and then report the most common and least common words.
'''

with open("moby_01_clean.txt") as infile:
	word_count = {}
	for word in infile:
		word_count[word] = word_count.get(word, 0) + 1

maxi = max(list(word_count.values()))
mini = min(list(word_count.values())) 

most_common = []
least_common = []

for key in list(word_count.keys()):
	if word_count[key] >= maxi - 7:
		most_common.append(key.strip("\n"))
	 
	if word_count[key] == mini:
		least_common.append(key.strip("\n"))


print('''In the first chapter of Moby Dick\nThe most common words are {0} with {1} to {2} times of occorance.\n
	The least common words are {3} with only {4} times of occurance.'''.format(
		most_common, maxi - 7 , maxi , least_common, mini ))
