# replacing the words [NOUN, VERB] in a string by iterating over the string

from random import randint

# randomly generating replacements for NOUN and VERB
def random_verb():
	"""returns one of two verbs randomly"""
	random_num = randint(0, 1)
	if random_num == 0:
	    return "run"
	else:
	    return "kayak"

def random_noun():
	"""returns one of two nouns randomly"""
	random_num = randint(0,1)
	if random_num == 0:
	    return "sofa"
	else:
	    return "llama"

# different algorithm (imitating replace() method):

def word_transformer(word):
	"""returns a random noun/verb if word is NOUN/VERB. otherwise, first letter of word"""
	if word == "NOUN":
	    return random_noun()
	elif word == "VERB":
	    return random_verb()
	else:
	    return word[0]
        
def process_madlib(mad_lib):
	"""takes a string and replaces [NOUN,VERB] with 1 of 2 nouns/verbs"""

	processed = ""                                 # initialize empty string to store processed text 
	index = 0                                      # start index to iterate over passed-in string
	while index < len(mad_lib):                    # iterate over string 4-character word at a time
	    word = mad_lib[index:index+4]              # initialize word to be the first 4 characters
	    processed_word = word_transformer(word)    # transform word to a NOUN or a VERB or its first character
	    processed += processed_word                # add transformed word to processed
	    if len(processed_word) == 1:               # increment index according to transformed word length
	        index += 1
	    else:
	        index += 4
	return processed


test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
