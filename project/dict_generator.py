import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QIcon

Form, Window = uic.loadUiType("test_gui.ui")

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
    form.stackedWidget.setCurrentIndex(1)
    global dict_state
    for key, value in dict_state['language_map'].items():
        form.new_language_com_box.addItem(key)


def updatedTable():

    global dict_state
    form.dict_table.clear()
    form.dict_table.setRowCount(300)
    form.dict_table.setColumnCount(len(dict_state['language_map']))
    form.dict_table.setEditTriggers(QTableWidget.NoEditTriggers)

    horHeaders = []
    for key, _ in dict_state['language_map'].items():
        horHeaders.append(key)
    form.dict_table.setHorizontalHeaderLabels(horHeaders)

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

def fillNewLanguage():
    if form.new_language_field.toPlainText():
        form.stackedWidget.setCurrentIndex(2)
        global new_language_counter
        new_language_counter = 0

def nextNewLanguage():
    global new_language_counter
    if new_language_counter > 0:
        new_language_counter -= 0


def prevNewLanguage():
    global new_language_counter
    new_language_counter += 0

def finishNewLanguage():
    pass

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
form.add_language.clicked.connect(newDictDialog)
form.new_language_button.clicked.connect(fillNewLanguage)
form.add_translation_next.clicked.connect(nextNewLanguage)
form.add_translation_back.clicked.connect(prevNewLanguage)
form.add_translation_finish.clicked.connect(finishNewLanguage)

window.show()
app.exec_()

