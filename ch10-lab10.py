'''Lab 10: Create a module
Package the functions created at the end of chapter 9 as a standalone module. Although
you can include code to run the module as the main program, the goal should be for the
functions to be completely usable from another script.'''

#importing everything from the module
import text_processor

#What was done in lab 6
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
	cleaned_words = text_processor.cleaner(infile)
	outfile.write(cleaned_words)

# see the outfile		
with open('moby_01_clean.txt','r') as outfile:
	for each in outfile:
		print(each, end = "")	


#What was done in lab 7
with open("moby_01_clean.txt") as infile:
	word_count = text_processor.w_counter(infile)
most_common = text_processor.most_finder(word_count)
least_common = text_processor.least_finder(word_count)


print('''In the first chapter of Moby Dick\nThe most common words are
 {0} with {1} to {2} times of occorance.\n
 The least common words are {3} with only {4} times of occurance.
 '''.format(most_common, text_processor.maxi - 7 , text_processor.maxi , least_common, text_processor.mini ))





