import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
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
         if 'language_map' in d:
            dict_state = d

    updatedTable()

def newDictDialog():
    pass

def updatedTable():

    global dict_state
    form.dict_table.setRowCount(300)
    form.dict_table.setColumnCount(len(dict_state['language_map']))


    row_count = 0
    for element in dict_state['question_map']:
        id = element['question_id']
        col_count = 0
        for key, value in dict_state['language_map'].items():
            if id in value:
                form.dict_table.setItem(row_count, col_count, QTableWidgetItem(value[id]))
            col_count += 1
        row_count += 1
    form.dict_table.resizeColumnsToContents()
    form.dict_table.resizeRowsToContents()

def handleTableClick(row, column):
    writeInputToDict(row)

def writeInputToDict(idx):
    pass

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.load_dict.clicked.connect(openDialog)
form.save_dict.clicked.connect(safeDialog)
form.new_dict.clicked.connect(newDictDialog)
form.dict_table.cellClicked.connect(handleTableClick)

window.show()
app.exec_()

