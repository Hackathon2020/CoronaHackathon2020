from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QStringList
from PyQt5.QtGui import QIcon

Form, Window = uic.loadUiType("test_gui.ui")

global dict_state

def safeDialog(self):
    pass

def openDialog(self):
    pass

def newDictDialog(self):
    pass

def updatedTable(self):
    pass

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.loadDict.clicked.connect(openDialog)
form.saveDict.clicked.connect(safeDialog)
form.newDict.clicked.connect(newDictDialog)

window.show()
app.exec_()


