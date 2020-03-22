from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QTableWidgetItem,
    QTableWidget,
    QAbstractItemView,
)
import json
import uuid

global dict_state
dict_state = {}
# fixme remove, only dummy for debugging
language = "german"

Form, Window = uic.loadUiType("test_gui.ui")


def safeDialog():
    dlg = QFileDialog()
    dlg.setAcceptMode(QFileDialog.AcceptSave)
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setNameFilter("Json files (*.json)")

    if dlg.exec_():
        filenames = dlg.selectedFiles()
        with open(filenames[0], "w") as fp:
            json.dump(
                dict_state,
                fp,
                indent=4,
                separators=(",", ": "),
                ensure_ascii=False,
            )


def openDialog(to_fill):
    global dict_state
    dlg = QFileDialog()
    dlg.setAcceptMode(QFileDialog.AcceptOpen)
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setNameFilter("Json files (*.json)")

    if dlg.exec_():
        filenames = dlg.selectedFiles()
        f = open(filenames[0], "r")

        with f:
            data = f.read()
            d = json.loads(data)
            if "language_map" in d:
                dict_state = d

    updatedTable()


def addLangDialog():
    form.left_window.setCurrentIndex(2)
    for key, value in dict_state["language_map"].items():
        form.new_language_com_box.addItem(key)


def newDictDialog():
    form.dict_table.clear()
    form.dict_table.setRowCount(300)
    form.dict_table.setColumnCount(2)
    form.dict_table.setEditTriggers(QTableWidget.NoEditTriggers)
    form.left_window.setCurrentIndex(0)
    form.textEdit.setText("")
    form.comboBox.setCurrentText("")


def createTable():
    form.dict_table.clear()
    form.dict_table.setRowCount(300)
    form.dict_table.setColumnCount(len(dict_state["language_map"]))
    form.dict_table.setEditTriggers(QTableWidget.NoEditTriggers)

    horHeaders = []
    for key, _ in dict_state["language_map"].items():
        horHeaders.append(key)
    form.dict_table.setHorizontalHeaderLabels(horHeaders)


def updatedTable():
    createTable()

    row_count = 0
    for element in dict_state["question_map"]:
        id = element["question_id"]
        col_count = 0
        for key, value in dict_state["language_map"].items():
            if id in value:
                form.dict_table.setItem(
                    row_count, col_count, QTableWidgetItem(value[id])
                )
            col_count += 1
        row_count += 1
    form.dict_table.resizeColumnsToContents()
    form.dict_table.resizeRowsToContents()


def fillNewLanguage():
    if form.new_language_field.toPlainText():
        form.left_window.setCurrentIndex(3)
        global new_language_counter

        dict_state["language_map"][
            form.new_language_field.toPlainText()
        ] = dict()
        new_language_counter = 1
        form.add_translation_ref_text_field.setText(
            dict_state["language_map"][form.new_language_com_box.currentText()][
                str(new_language_counter)
            ]
        )
        form.add_translation_translation_field.clear()
    updatedTable()


def prevNewLanguage():
    global new_language_counter
    dict_state["language_map"][form.new_language_field.toPlainText()][
        str(new_language_counter)
    ] = form.add_translation_translation_field.toPlainText()
    if new_language_counter > 1:
        new_language_counter -= 1
        form.add_translation_ref_text_field.setText(
            dict_state["language_map"][form.new_language_com_box.currentText()][
                str(new_language_counter)
            ]
        )
        form.add_translation_translation_field.clear()

    updatedTable()


def nextNewLanguage():
    global new_language_counter
    global dict_state
    dict_state["language_map"][form.new_language_field.toPlainText()][
        str(new_language_counter)
    ] = form.add_translation_translation_field.toPlainText()
    if new_language_counter < len(
        dict_state["language_map"][form.new_language_com_box.currentText()]
    ):
        new_language_counter += 1
        form.add_translation_ref_text_field.setText(
            dict_state["language_map"][form.new_language_com_box.currentText()][
                str(new_language_counter)
            ]
        )
        form.add_translation_translation_field.clear()
    updatedTable()


def finishNewLanguage():
    dict_state["language_map"][form.new_language_field.toPlainText()][
        str(new_language_counter)
    ] = form.add_translation_translation_field.toPlainText()
    form.add_translation_translation_field.clear()
    form.left_window.setCurrentIndex(0)
    updatedTable()


def handleTableClick(row, column):
    SetLeftWindow(row)


def SetLeftWindow(idx):
    form.left_window.setCurrentIndex(1)
    form.tableWidget.clear()
    # default view
    form.stackedWidget_2.setCurrentIndex(1)

    key = str(idx + 1)
    exists = len(dict_state) != 0 and idx < len(dict_state["question_map"])
    if exists:
        c_quest = dict_state["language_map"][language][key]
        c_ans = dict_state["question_map"][idx]["answer_type"]
    else:
        c_ans = ""
        c_quest = ""

    form.textEdit.setText(c_quest)
    form.comboBox.setCurrentText(c_ans)

    form.tableWidget.clear()
    form.tableWidget.setRowCount(10)
    form.tableWidget.setColumnCount(1)
    form.tableWidget.setHorizontalHeaderLabels(["Options"])

    if exists and "options" in dict_state["question_map"][idx].keys():
        form.stackedWidget_2.setCurrentIndex(1)
        options = dict_state["question_map"][idx]["options"]
        for row, option in enumerate(options):
            form.tableWidget.setItem(
                row,
                0,
                QTableWidgetItem(dict_state["language_map"][language][option]),
            )
        form.tableWidget.resizeColumnsToContents()
        form.tableWidget.resizeRowsToContents()
    else:
        form.stackedWidget_2.setCurrentIndex(0)


def createNewDict():
    hash = str(uuid.uuid4())
    dict_state.update(
        {
            "global_questionaire_id": hash,
            "language_map": {language: {}},
            "question_map": [],
        }
    )


def changeOption():
    if form.comboBox.currentIndex() == 0 or form.comboBox.currentIndex() == 5:
        form.stackedWidget_2.setCurrentIndex(1)
    else:
        form.stackedWidget_2.setCurrentIndex(0)


def writeToDict():
    #  load question mask
    quest_text = form.textEdit.toPlainText()
    answer_type = form.comboBox.currentIndex()
    answer_desc = form.comboBox.currentText()

    if quest_text == "":
        # fixme infobox
        pass
    elif answer_desc == "":
        # fixme infobox
        pass
    else:
        if len(dict_state) == 0:
            createNewDict()
            createTable()
        field_id = (
            max(
                map(
                    lambda x: int(x),
                    dict_state["language_map"][language].keys(),
                )
            )
            + 1
            if len(dict_state["language_map"][language]) > 0
            else 1
        )

        col_id = 0
        for idx, lang in enumerate(dict_state["language_map"]):
            if form.dict_table.horizontalHeaderItem(idx).text() == lang:
                col_id = idx
                break

        row_id = 0
        for idx, _ in enumerate(dict_state["question_map"]):
            if form.dict_table.item(idx, col_id) is not None:
                row_id += 1
            else:
                break

        # write to dict
        # question = form.textEdit.plainText()
        dict_state["language_map"][language][str(field_id)] = quest_text

        # add to overview table
        form.dict_table.setItem(row_id, col_id, QTableWidgetItem(quest_text))

        if answer_type == 0 or answer_type == 5:
            options = []
            for row in range(form.tableWidget.rowCount()):
                curr_item = form.tableWidget.item(row, 0)
                if curr_item is None:
                    break
                options.append(str(field_id + row + 1))
                dict_state["language_map"][language].update(
                    {options[-1]: curr_item.text()}
                )

            dict_state["question_map"].append(
                {
                    "question_id": str(field_id),
                    "answer_type": answer_desc,
                    "options": options,
                }
            )
        else:
            dict_state["question_map"].append(
                {"question_id": str(field_id), "answer_type": answer_desc}
            )

        form.dict_table.resizeColumnsToContents()
        form.dict_table.resizeRowsToContents()

        # reset lefthand side
        form.left_window.setCurrentIndex(0)


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.load_dict.clicked.connect(openDialog)
form.save_dict.clicked.connect(safeDialog)
form.new_dict.clicked.connect(newDictDialog)
form.add_language.clicked.connect(addLangDialog)
form.new_language_button.clicked.connect(fillNewLanguage)
form.add_translation_next.clicked.connect(nextNewLanguage)
form.add_translation_back.clicked.connect(prevNewLanguage)
form.add_translation_finish.clicked.connect(finishNewLanguage)
form.dict_table.cellClicked.connect(handleTableClick)
form.buttonBox.clicked.connect(writeToDict)
form.comboBox.currentIndexChanged.connect(changeOption)


window.show()
app.exec_()
