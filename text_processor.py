'''the module for cleaning a text file, counting the words, and reporting frequent words'''


def remove_punc(string):
	'''removing punctuations from any given string'''
	table = string.maketrans('.,?;:!"-_][)(\'',' '*14)
	return string.translate(table)

 

def cleaner(text):
	'''cleaning a file and making it standard to proccess'''
	words_list = []
	for line in text:
		lower_case = line.lower()
		sans_punct = remove_punc(lower_case)
		line_list = sans_punct.split()		
		words_list = words_list + line_list
	return '\n'.join(words_list)


def w_counter(text):
	'''counting words in any given text'''
	counted = {}
	for word in text:
		counted[word] = counted.get(word, 0) + 1
	return counted


def most_finder(counted_dict):
	'''inding most common words in a dictionary'''
	global maxi
	maxi = max(list(counted_dict.values()))
	most = []
	for key in list(counted_dict.keys()):
		if counted_dict[key] >= maxi - 7:
			most.append(key.strip("\n"))
	return most		


def least_finder(counted_dict):
	'''finding least common words in a dictionary'''
	global mini
	mini = min(list(counted_dict.values())) 
	least = []
	for key in list(counted_dict.keys()):	 
		if counted_dict[key] == mini:
			least.append(key.strip("\n"))
	return least