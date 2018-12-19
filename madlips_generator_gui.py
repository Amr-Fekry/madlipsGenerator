from tkinter import *

def switch2_design_frame():
	intro_frame.pack_forget()
	design_frame.pack()

def switch2_intro_frame():
	design_frame.pack_forget()
	intro_frame.pack()


# initialize a window
window = Tk()

window.title("Madlips Generator")
window.geometry("600x300")

#### 1- INTRODUCTION:

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

#### 2- DESIGNER STAGE:

design_frame = Frame(window)

# add parts of speech
pos_list = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

pos_label = Label(design_frame, text="""
Designer turn

Here is the current list of parts-of-speech that you can use:

""" + ", ".join(pos_list))
pos_label.pack()


button2 = Button(design_frame, text="Back", command=switch2_intro_frame)
button2.pack()



window.mainloop()