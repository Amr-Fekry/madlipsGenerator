# replacing the words [NOUN, VERB] in a string using string slicing and concatenation

sentence = "A NOUN went on a walk. It can VERB really fast."

# slice sentence around NOUN and VERB
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

# replacements for NOUN and VERB
noun_replacement = "book" 
verb_replacement = "read" 

# concatenate substrings with replacements
new_sentence = ""
new_sentence += substring1
new_sentence += noun_replacement
new_sentence += substring2
new_sentence += verb_replacement
new_sentence += substring3

print new_sentence

#or
#new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
