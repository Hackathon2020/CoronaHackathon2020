import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

Form, Window = uic.loadUiType("test_gui.ui")

global dict_state

def safeDialog():
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setNameFilter("Json files (*.json)")
      
    if dlg.exec_():
      filenames = dlg.selectedFiles()
      with open(filenames[0], 'w') as fp:
        global dict_state
        json.dump(dict_state, fp, indent=4, separators=(',', ': '), ensure_ascii=False)

def openDialog():
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setNameFilter("Json files (*.json)")

    if dlg.exec_():
      filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         d = json.loads(data)
         global dict_state
         dict_state = d

def newDictDialog():
    pass

def updatedTable():
    pass

def writeInputToDict(idx):
    pass

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.load_dict.clicked.connect(openDialog)
form.save_dict.clicked.connect(safeDialog)
form.new_dict.clicked.connect(newDictDialog)


window.show()
app.exec_()

