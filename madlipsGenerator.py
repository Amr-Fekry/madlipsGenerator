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
