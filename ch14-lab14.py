'''Lab 14: Custom exceptions
Think about the module you wrote in chapter 9 to count word frequencies. What errors
might reasonably occur in those functions? Refactor those functions to handle those
exception conditions appropriately.'''

class FileProcessingError(Exception):
    """Custom exception for file processing errors."""
    pass

class WordCountError(Exception):
    """Custom exception for word counting errors."""
    pass


def remove_punc(string):
    """Remove punctuation from a string."""
    try:
        table = string.maketrans('.,?;:!"-_][)(\'',' '*14)
        return string.translate(table)
    except Exception as e:
        raise FileProcessingError(f"Error removing punctuation: {e}")


def w_counter(text):
    """Count the frequency of words in a text."""
    try:
        counted = {}
        for word in text:
            counted[word] = counted.get(word, 0) + 1
        return counted
    except Exception as e:
        raise WordCountError(f"Error counting words: {e}")
 

def cleaner(text):
    """Clean the text by converting to lowercase and removing punctuation."""
    try:
        words_list = []
        for line in text:
            lower_case = line.lower()
            sans_punct = remove_punc(lower_case)
            line_list = sans_punct.split()
            words_list = words_list + line_list
        return '\n'.join(words_list)
    except Exception as e:
        raise FileProcessingError(f"Error cleaning text: {e}")


def most_finder(counted_dict):
    """Find the most common words in the counted dictionary."""
    try:
        global maxi
        maxi = max(list(counted_dict.values()))
        most = []
        for key in list(counted_dict.keys()):
            if counted_dict[key] >= maxi - 7:
                most.append(key.strip("\n"))
        return most
    except Exception as e:
        raise WordCountError(f"Error finding most common words: {e}")


def least_finder(counted_dict):
    """Find the least common words in the counted dictionary."""
    try:
        global mini
        mini = min(list(counted_dict.values()))
        least = []
        for key in list(counted_dict.keys()):
            if counted_dict[key] == mini:
                least.append(key.strip("\n"))
        return least
    except Exception as e:
        raise WordCountError(f"Error finding least common words: {e}")


#lab6 refactored
try:
    with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
        cleaned_words = cleaner(infile)
        outfile.write(cleaned_words)
except FileProcessingError as e:
    print(e)

# see the outfile		
try:
    with open('moby_01_clean.txt','r') as outfile:
        for each in outfile:
            print(each, end = "")
except FileProcessingError as e:
    print(e)	


#lab7 refactored
try:
    with open("moby_01_clean.txt") as infile:
        word_count = w_counter(infile)
    most_common = most_finder(word_count)
    least_common = least_finder(word_count)
except (FileProcessingError, WordCountError) as e:
    print(e)


print('''In the first chapter of Moby Dick\nThe most common words are
 {0} with {1} to {2} times of occorance.\n
 The least common words are {3} with only {4} times of occurance.'''.format(
		most_common, maxi - 7 , maxi , least_common, mini ))



