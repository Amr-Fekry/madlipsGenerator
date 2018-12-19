from tkinter import *

# initialize a window
window = Tk()

window.title("Madlips Generator")
window.geometry("600x300")

intro_frame = Frame(window)
intro_frame.pack()

intro_label = Label(intro_frame, text="""
	Welcome to Madlips Generator game \n
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

window.mainloop()