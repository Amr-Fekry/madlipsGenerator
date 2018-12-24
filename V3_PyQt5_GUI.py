import sys
from PyQt5 import QtWidgets, QtGui, QtCore 

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		# initialize a QMainWindow object (will be referred to as "self")
		super(Window, self).__init__()
		# modify the Window object
		self.setGeometry(400, 100, 500, 300)
		self.setWindowTitle("Madlips Generator")
		self.setWindowIcon(QtGui.QIcon("smile.png"))


		# show Widow object
		self.show()




def main():
	# initialize the App
	app = QtWidgets.QApplication(sys.argv)
	# initialize a Window object
	window = Window()
	# keep app running
	sys.exit(app.exec_())

main()