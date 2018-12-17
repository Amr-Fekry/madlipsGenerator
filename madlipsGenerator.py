# replacing the words [NOUN, VERB] in a string using string slicing and concatenation

sentence = "A NOUN went on a walk. It can VERB really fast."

# slice sentence around NOUN and VERB
noun_position = sentence.find("NOUN")
verb_position = sentence.find("VERB")

substring1 = sentence[:noun_position]
substring2 = sentence[noun_position+4 : verb_position]
substring3 = sentence[verb_position+4 :]

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
