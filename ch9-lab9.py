'''
Lab 9: Useful functions
Looking back at the labs in chapters 6 and 7 , refactor that code into functions for
cleaning and processing the data.
The goal should be that most of the logic is moved into functions. 
Use your own judgment as to the types of functions and parameters, but
keep in mind that functions should do just one thing, and they shouldn’t have any side
effects that carry over outside the function.
'''

# removing punctuation refactored into funtion
def remove_punc(string):
		table = string.maketrans('.,?;:!"-_][)(\'',' '*14)
		return string.translate(table)

# counting words refactored into funtion 
def w_counter(text):
	counted = {}
	for word in text:
		counted[word] = counted.get(word, 0) + 1
	return counted
 
# cleaning file refactored into funtion
def cleaner(text):
	words_list = []
	for line in text:
		lower_case = line.lower()
		sans_punct = remove_punc(lower_case)
		line_list = sans_punct.split()		
		words_list = words_list + line_list
	return '\n'.join(words_list)

# finding most common refactored into funtion
def most_finder(counted_dict):
	global maxi
	maxi = max(list(counted_dict.values()))
	most = []
	for key in list(counted_dict.keys()):
		if counted_dict[key] >= maxi - 7:
			most.append(key.strip("\n"))
	return most		

# finding least common refactored into funtion
def least_finder(counted_dict):
	global mini
	mini = min(list(counted_dict.values())) 
	least = []
	for key in list(counted_dict.keys()):	 
		if counted_dict[key] == mini:
			least.append(key.strip("\n"))
	return least


#lab6 refactored
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
	cleaned_words = cleaner(infile)
	outfile.write(cleaned_words)

# see the outfile		
with open('moby_01_clean.txt','r') as outfile:
	for each in outfile:
		print(each, end = "")	


#lab7 refactored
with open("moby_01_clean.txt") as infile:
	word_count = w_counter(infile)
most_common = most_finder(word_count)
least_common = least_finder(word_count)


print('''In the first chapter of Moby Dick\nThe most common words are
 {0} with {1} to {2} times of occorance.\n
 The least common words are {3} with only {4} times of occurance.'''.format(
		most_common, maxi - 7 , maxi , least_common, mini ))





