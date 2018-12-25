import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		# initialize a QMainWindow object (will be referred to as "self")
		super(Window, self).__init__()
		# modify the Window object
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Madlips Generator")
		self.setWindowIcon(QtGui.QIcon("smile.png"))

		self.page_one()


	# ________________________________________PAGES_________________________________________

	def page_one(self):

		self.page1 = QtWidgets.QWidget()
		self.layout = QtWidgets.QGridLayout()
		self.layout.setAlignment(QtCore.Qt.AlignCenter) # alignment of cells inside the layout. Center = (HCenter + VCenter)
		self.page1.setLayout(self.layout)

		# ------ make label1
		self.intro_label1 = QtWidgets.QLabel("""Welcome to Madlips Generator game

		It takes two players to play this game: a 'game designer' and a 'game player'
		""")
		self.intro_label1.setAlignment(QtCore.Qt.AlignCenter) # alignment of text inside the label

		# ------ make label2
		self.intro_label2 = QtWidgets.QLabel("""
game designer: 
writes a sentence with some words encrypted as parts of speech. He can use a list of words that we already made for parts of speech, and he can modify this list to add/delete words. player2 must not see the sentence.

game player: 
After the sentence is created, it is the game player's turn to play the game. He will be asked to replace the parts of speech present in the sentence with random words. 

Finally both can see the final result.

		""")
		#self.intro_label2.setMaximumWidth(800)
		#self.intro_label2.setMinimumWidth(800)
		self.intro_label2.setMinimumHeight(160)
		self.intro_label2.setWordWrap(True)

		# ------ make button
		self.gotit_btn = QtWidgets.QPushButton("Got it")
		#self.gotit_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

		# add widgets to layout
		self.layout.addWidget(self.intro_label1, 0, 0, QtCore.Qt.AlignCenter) 
		self.layout.addWidget(self.intro_label2, 1, 0, QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.gotit_btn, 2, 0, QtCore.Qt.AlignCenter) # for grid layout: (widget, row, column, alignment in cell)
		
		# show page1 as centralwidget
		self.setCentralWidget(self.page1)


	# ________________________________________METHODS_________________________________________


def main():
	# initialize the App
	app = QtWidgets.QApplication(sys.argv)
	# initialize a Window object
	window = Window()
	# show window
	window.show()
	# keep app running
	sys.exit(app.exec_())

main()