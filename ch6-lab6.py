'''
Lab 6: Preprocessing Text
In processing raw text, it’s quite often necessary to clean and normalize the text before doing anything else. 
If you want to find the frequency of words in text, for example, you can make the job easier if,
before you start counting, you make sure that everything is lowercase (or uppercase, if you prefer) 
and that all punctuation has been removed. You can also make things easier by breaking the text into a series of words. 
In this lab, the task is to read the first part of the first chapter of Moby Dick (found in the book’s source code), 
make sure that everything is one case, remove all punctuation, and write the words one per line to a second file. 
Because I haven’t yet covered reading and writing files, here’s the code for those operations:
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
for line in infile:
# make all one case
# remove punctuation
# split into words
# write all words for line
outfile.write(cleaned_words)
'''
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
	words_list = []
	for line in infile:
# make all one case
		lower_case = line.lower()
# remove punctuation
		table = lower_case.maketrans('.,?;:!"-_][)(\'',' '*14)
		sans_punct = lower_case.translate(table)
# split into words
		line_list = sans_punct.split()		
# write all words for line
		words_list = words_list + line_list
	cleaned_words = '\n'.join(words_list)
	outfile.write(cleaned_words)

# see the outfile		
with open('moby_01_clean.txt','r') as outfile:
	for each in outfile:
		print(each)	