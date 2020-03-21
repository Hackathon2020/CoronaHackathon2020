import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon
from functools import partial
import json

global dict_state
language = None

Form, Window = uic.loadUiType("test_gui.ui")


def safeDialog():
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setNameFilter("Json files (*.json)")

    if dlg.exec_():
        filenames = dlg.selectedFiles()
        with open(filenames[0], 'w') as fp:
            global dict_state
            json.dump(dict_state, fp, indent=4, separators=(',', ': '),
                      ensure_ascii=False)


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
    form.tableWidget.setRowCount(300)
    form.tableWidget.setColumnCount(len(dict_state['language_map']))

    row_count = 0
    for element in dict_state['question_map']:
        id = element['question_id']
        col_count = 0
        for key, value in dict_state['language_map'].items():
            if id in value:
                form.tableWidget.setItem(row_count, col_count,
                                        QTableWidgetItem(value[id]))
            col_count += 1
        row_count += 1
    form.tableWidget.resizeColumnsToContents()
    form.tableWidget.resizeRowsToContents()


def handleTableClick(row, column):
    writeInputToDict(row)


def writeInputToDict(idx):
    if idx in dict_state["language_map"][language].keys():
        if "options" in dict_state["question_map"][idx].keys():
            pass
        else:
            c_ans = dict_state["language_map"][language][idx]
    else:
        c_ans = ""
    form.left_window.setCurrectIndex(0)
    form.textEdit.setText(c_ans)


def dump_json():
    #  load question mask
    answer_text = form.textEdit.toPlainText()
    answer_type = form.comboBox.currentIndex()

    if answer_text == "":
        # fixme infobox
        pass
    else:
        if answer_type == 0 or answer_type == 5:
            dict_state["question_map"].append()
        else:
            pass


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.load_dict.clicked.connect(openDialog)
form.save_dict.clicked.connect(safeDialog)
form.new_dict.clicked.connect(newDictDialog)
form.tableWidget.cellClicked.connect(handleTableClick)

window.show()
app.exec_()








# def safeDialog():
#     dlg = QFileDialog()
#     dlg.setFileMode(QFileDialog.AnyFile)
#     dlg.setNameFilter("Json files (*.json)")
#
#     if dlg.exec_():
#       filenames = dlg.selectedFiles()
#       with open(filenames[0], 'w') as fp:
#         global dict_state
#         json.dump(dict_state, fp, indent=4, separators=(',', ': '), ensure_ascii=False)
#
# def openDialog():
#     dlg = QFileDialog()
#     dlg.setFileMode(QFileDialog.AnyFile)
#     dlg.setNameFilter("Json files (*.json)")
# =======
#
#     def safeDialog(self):
#         pass
#
# <<<<<<< Updated upstream
#       with f:
#          data = f.read()
#          d = json.loads(data)
#          global dict_state
#          if 'language_map' in d:
#             dict_state = d
#
#     updatedTable()
# =======
#     def openDialog(self):
#         dlg = QFileDialog()
#         dlg.setFileMode(QFileDialog.AnyFile)
#         dlg.setNameFilter("Json files (*.json)")
#         # filenames = QStringList()
#
#         if dlg.exec_():
#           filenames = dlg.selectedFiles()
#           f = open(filenames[0], 'r')
#
#           with f:
#              data = f.read()
#              d = json.loads(data)
#              global dict_state
#              dict_state = d
#
#     def newDictDialog(self):
#         pass
#
#     def updatedTable(self):
#         pass
#
#     def loadDataFromJson(self,idx):
#
#
#
#
#     def writeInputToDict(self,):
#         #  load question mask
#         answer_text = self.form.textEdit.toPlainText()
#         answer_type = self.form.comboBox.currentIndex()
#
#
#         if answer_text== "":
#             # fixme infobox
#             pass
#         else:
#             if answer_type == 0 or answer_type == 5:
#                 self.state_dict["question_map"].append()
#             else:
#                 pass
#
#
#     def setLanguage(self):
#         self.language = "german"
# >>>>>>> Stashed changes
#
#
# <<<<<<< Updated upstream
# def updatedTable():
#
#     global dict_state
#     form.tableWidget.setRowCount(300)
#     form.tableWidget.setColumnCount(len(dict_state['language_map']))
#
#
#     row_count = 0
#     for element in dict_state['question_map']:
#         id = element['question_id']
#         col_count = 0
#         for key, value in dict_state['language_map'].items():
#             if id in value:
#                 form.tableWidget.setItem(row_count, col_count, QTableWidgetItem(value[id]))
#             col_count += 1
#         row_count += 1
#     form.tableWidget.resizeColumnsToContents()
#     form.tableWidget.resizeRowsToContents()
#
# def handleTableClick(row, column):
#     writeInputToDict(row)
# =======
# >>>>>>> Stashed changes
#
#
# app = QApplication([])
# mw = MainWindow()
#
# mw.form.setupUi(mw.window)
#
# mw.form.load_dict.clicked.connect(mw.openDialog)
# mw.form.save_dict.clicked.connect(mw.safeDialog)
# mw.form.button_box.clicked.connect(mw.writeInputToDict)
# mw.form.new_dict.clicked.connect(partial(mw.loadDataFromJson,idx=0))
#
# <<<<<<< Updated upstream
# form.load_dict.clicked.connect(openDialog)
# form.save_dict.clicked.connect(safeDialog)
# form.new_dict.clicked.connect(newDictDialog)
# form.tableWidget.cellClicked.connect(handleTableClick)
# form.
#
# mw.window.show()
# app.exec_()
#
