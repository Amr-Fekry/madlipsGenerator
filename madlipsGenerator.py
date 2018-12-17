# replacing the words [NOUN, VERB] in a string using string slicing and concatenation
from random import randint

sentence = "A NOUN went on a walk. It can VERB really fast."

# slice sentence around NOUN and VERB
noun_position = sentence.find("NOUN")
verb_position = sentence.find("VERB")

substring1 = sentence[:noun_position]
substring2 = sentence[noun_position+4 : verb_position]
substring3 = sentence[verb_position+4 :]

# randomly generating replacements for NOUN and VERB
def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

# concatenate substrings with replacements
new_sentence = ""
new_sentence += substring1
new_sentence += random_noun()
new_sentence += substring2
new_sentence += random_verb()
new_sentence += substring3

print new_sentence
