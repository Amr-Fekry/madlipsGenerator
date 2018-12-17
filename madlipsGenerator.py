# replacing the words [NOUN, VERB] in a string using replace() method

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

# using replace() method:

def process_madlib(mad_lib):
	"""takes a string and replaces [NOUN,VERB] with 1 of 2 nouns/verbs"""
	return mad_lib.replace("NOUN",random_noun()).replace("VERB",random_verb())


test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
