# initial inputs: a list containing parts of speech (POSs) to be replaced, and a sentence
# intermediate inputs: replacements  for POSs in the sentence one-by-one

# final output: a sentence with POSs replaced with user inputs

# pseudo code:
# split sentence into a list of words
# for each word, check if it contains a part of speech 
# if not add the word to list2
# if it does, prompt user for replacement, replace it in word, add it to list2
# convert list2 into a string

def pos_in_word(parts_of_speech, word):
	"""returns the part of speech if it is a substring in the word. otherwise, None"""
	for pos in parts_of_speech:
		if pos in word:
			return pos
	return None

def play(parts_of_speech, sentence):
	"""returns sentence with all parts_of_speech in it replaced with user input"""
	list_of_words = sentence.split()
	list_processed = []

	for word in list_of_words:
		pos_word = pos_in_word(parts_of_speech, word)
		if not pos_word:
			list_processed.append(word)
		else:
			user_input = input("give me a {}?  ".format(pos_word))
			word = word.replace(pos_word, user_input)
			list_processed.append(word)
	
	string_processed = " ".join(list_processed)
	return string_processed


# testing 
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]
sentence = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""
print (play(parts_of_speech, sentence))


# raw_input vs input:
# In Python 2, raw_input() returns a string, and input() tries to run the input as a Python expression. input() = eval(raw_input())

# Since getting a string was almost always what you wanted, Python 3 does that with input(). And if you ever want the old behaviour, eval(input()) works.
