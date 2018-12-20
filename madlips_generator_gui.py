from tkinter import *

#### FUNCTIONS:

def switch2_design_frame():
	intro_frame.pack_forget()
	design_frame.pack()

def switch2_intro_frame():
	design_frame.pack_forget()
	intro_frame.pack()

def switch2_play_frame():
	design_frame.pack_forget()
	play_frame.pack()

def add_pos():
	# get pos from corresponding entry
	pos = add_entry.get()
	# clear the entry for better appearance
	add_entry.delete(0,END)
	# append it to the list
	pos_list.append(pos)
	# enable editing of pos_textfield
	pos_textfield.config(state="normal")
	# clear pos_textfield 
	pos_textfield.delete(1.0, END)
	# insert (update) elements of pos_list after joining to a string
	pos_textfield.insert(END, " , ".join(pos_list))
	# disable editing of pos_textfield
	pos_textfield.config(state="disabled")

def delete_pos():
	# get pos from corresponding entry
	pos = delete_entry.get()
	# clear the entry for better appearance
	delete_entry.delete(0,END)
	# append it to the list
	pos_list.remove(pos)
	# enable editing of pos_textfield
	pos_textfield.config(state="normal")
	# clear pos_textfield
	pos_textfield.delete(1.0, END)
	# insert (update) elements of pos_list after joining to a string
	pos_textfield.insert(END, " , ".join(pos_list))
	# disable editing of pos_textfield
	pos_textfield.config(state="disabled")

def pos_in_word(parts_of_speech, word):
	"""returns the part of speech if it is a substring in the word. otherwise, None"""
	for pos in parts_of_speech:
		if pos in word:
			return pos
	return None

def play_button_clicked():
	sentence = sentence_field.get(1.0, END)
	switch2_play_frame()
	list_of_words = sentence.split()
	list_of_replacements = []
	list_processed = []

	for word in list_of_words:
		pos_word = pos_in_word(pos_list, word)
		if not pos_word:
			list_processed.append(word)
		else:
			Label(play_frame, text="{}:".format(pos_word)).pack()
			Entry(play_frame).pack()
"""			
			word = word.replace(pos_word, user_input)
			list_processed.append(word)
	
	string_processed = " ".join(list_processed)
	return string_processed
"""

# initialize a window
window = Tk()

window.title("Madlips Generator")
window.geometry("600x400")

#### 1- INTRODUCTION FRAME:

intro_frame = Frame(window)
intro_frame.pack()

intro_label = Label(intro_frame, text="""
Welcome to Madlips Generator game

It takes two players to play this game: a 'game designer' and a 'game player'""")
intro_label.pack()

explain_label = Label(intro_frame, text="""
game designer: 
writes a sentence with some words encrypted as parts of speech. He can use a list of words that we already made for parts of speech, and he can modify this list to add/delete words. player2 must not see the sentence.

game player: 
After the sentence is created, it is the game player's turn to play the game. He will be asked to replace the parts of speech present in the sentence with random words. 

Finally both can see the final result.
""", wraplength=480, justify="left") # wraplength & justify
explain_label.pack()

# a button to switch to the next frame
button1 = Button(intro_frame, text="Got it", command=switch2_design_frame)
button1.pack()

#### 2- DESIGNER STAGE FRAME:

# create a new frame
design_frame = Frame(window)

# add parts of speech
pos_list = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

label1 = Label(design_frame, text="""
Designer turn

Here is the current list of parts-of-speech that you can use:
""")
label1.pack()

# add text field to display the initial list of PsOS
pos_textfield = Text(design_frame, width=200, height=2)
pos_textfield.insert(END, " , ".join(pos_list))
pos_textfield.config(state="disabled") # make the textfield for read only
pos_textfield.pack()

# frame for add/delete buttons
subframe1 = Frame(design_frame)
subframe1.pack()

# create add button that adds a POS to the list    
add_entry = Entry(subframe1)
add_entry.pack(side=LEFT)
add_button = Button(subframe1, text="Add", command=add_pos)
add_button.pack(side=LEFT)

# create delete button that deletes a POS from the list    
delete_entry = Entry(subframe1)
delete_entry.pack(side=LEFT)
delete_button = Button(subframe1, text="Delete", command=delete_pos)
delete_button.pack(side=LEFT)

# frame for add/delete instructions
subframe2 = Frame(design_frame)
subframe2.pack()

explain_label2 = Label(design_frame, text="""*to add a word: write the word in the entry field (in all caps), then press Add 
*to delete a word: copy the word from the list and paste it in the entry field, then press Delete""", wraplength=600, justify="left")
explain_label2.pack()

# make a textfield for the sentence
sentence_label = Label(design_frame, text="Enter your sentence with the parts of speech below:")
sentence_label.pack()
sentence_field = Text(design_frame, width=100, height=10)
sentence_field.pack()

# a button to recieve the sentence and play
play_button = Button(design_frame, text="Play", command=play_button_clicked)
play_button.pack()

#### 3- PLAYER STAGE FRAME:

# create a new frame
play_frame = Frame(window)
Label(play_frame, text="give me a ").pack()

# a button to switch to the previous frame
button2 = Button(design_frame, text="Back", command=switch2_intro_frame)
button2.pack(side=BOTTOM)



window.mainloop()