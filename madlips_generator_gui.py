from tkinter import *

#### FUNCTIONS:

def frame1_Gotit_btn():
	intro_frame.pack_forget()
	design_frame.pack()

def frame2_Add_btn():
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

def frame2_Delete_btn():
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

def frame2_Back_btn():
	design_frame.pack_forget()
	intro_frame.pack()

def switch_frame3():
	design_frame.pack_forget()
	play_frame.pack()

def pos_in_word(parts_of_speech, word):
	"""returns the part of speech if it is a substring in the word. otherwise, None"""
	for pos in parts_of_speech:
		if pos in word:
			return pos
	return None

def frame2_Play_btn():
	# get sentence from sentence_field
	sentence = sentence_field.get(1.0, END)
	# list of separate words of the sentence
	global list_of_words
	list_of_words = sentence.split()
	# make a subframe to contain widgets to be created
	global play_subframe 
	play_subframe = Frame(play_frame)
	play_subframe.pack()

	global list_of_widgets
	list_of_widgets = []

	# iterate over list_of_word and entry widgets for each pos detected
	for word in list_of_words:
		pos_word = pos_in_word(pos_list, word)
		if pos_word:
			# create a label and an entry field on subframe and add them to a list
			list_of_widgets.append(Label(play_subframe, text="{}:".format(pos_word)))
			list_of_widgets.append(Entry(play_subframe))

	# pack all widgets in the list
	for widget in list_of_widgets:
		widget.pack()

	switch_frame3()

def frame3_Back_btn():
	# clear sentence_field
	sentence_field.delete(1.0, END)
	# destroy subframe and all widgets in it to prepare for a new one
	play_subframe.destroy()
	play_frame.pack_forget()
	design_frame.pack()

def frame3_Done_btn():
	# get user inputs from entries
	list_of_inputs = []
	for entry in list_of_widgets[1::2]: # get odd positions only list[start:end:step]
		list_of_inputs.append(entry.get())
	# words of the sentence after processing 
	list_processed = []

	for index, word in enumerate(list_of_words):
		pos_word = pos_in_word(pos_list, word)
		if pos_word:
			word = word.replace(pos_word, list_of_inputs[0])
			list_of_words[index] = word
			del list_of_inputs[0]

	string_processed = " ".join(list_of_words)
	print(string_processed)


# initialize a window
window = Tk()

window.title("Madlips Generator")
window.geometry("600x450")

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
button1 = Button(intro_frame, text="Got it", command=frame1_Gotit_btn)
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
add_button = Button(subframe1, text="Add", command=frame2_Add_btn)
add_button.pack(side=LEFT)

# create delete button that deletes a POS from the list    
delete_entry = Entry(subframe1)
delete_entry.pack(side=LEFT)
delete_button = Button(subframe1, text="Delete", command=frame2_Delete_btn)
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

# a button to switch to the previous frame
button2 = Button(design_frame, text="Back", command=frame2_Back_btn)
button2.pack(side=BOTTOM)

# a button to recieve the sentence and play
play_button = Button(design_frame, text="Play", command=frame2_Play_btn)
play_button.pack()

#### 3- PLAYER STAGE FRAME:

# create a new frame
play_frame = Frame(window)
Label(play_frame, text="""
Player turn

give an example for each part of speech below:
""").pack()

# a button to switch to the previous frame
button3 = Button(play_frame, text="Back", command=frame3_Back_btn)
button3.pack(side=BOTTOM)

# switch to next frame, show final sentence 
button4 = Button(play_frame, text="Done", command=frame3_Done_btn)
button4.pack(side=BOTTOM)



window.mainloop()