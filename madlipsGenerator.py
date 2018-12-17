# initial inputs: a list containing parts of speech (POSs) to be replaced, and a sentence
# intermediate inputs: replacements  for POSs in the sentence one-by-one

# final output: a sentence with POSs replaced with user inputs

# hard-codes inputs for testing 
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]
sentence = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

# pseudo code:
# split sentence into a list of words
# for each word, check if it contains a part of speech 
# if it does, prompt user for replacement then add it to list2
# if not add the word to list2
# convert list2 into a string

def pos_in_word(parts_of_speech, word):
	"""returns the part of speech if it is a substring in the word. otherwise, None"""
	for pos in parts_of_speech:
		if pos in word:
			return pos
	return None


test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech2 = ["PERSON", "PLURALNOUN", "NOUN"]

print pos_in_word(parts_of_speech2, test_cases[0])
print pos_in_word(parts_of_speech2, test_cases[1])
print pos_in_word(parts_of_speech2, test_cases[2])
print pos_in_word(parts_of_speech2, test_cases[3])
