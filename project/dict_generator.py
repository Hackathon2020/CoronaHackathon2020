from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QTableWidgetItem,
    QTableWidget,
    QAbstractItemView,
    QMenuBar,
    QAction,
)
import json
import uuid

# Contains JSON file which will be exported or has been imported and will be manipulated by the user's actions.
dict_state = {}

# fixme remove, only dummy for debugging
language = "german"

Form, Window = uic.loadUiType("test_gui.ui")


def save_dialog():
    """Open a file dialog to save json dict to file."""
    dlg = QFileDialog()
    dlg.setAcceptMode(QFileDialog.AcceptSave)
    dlg.setFileMode(QFileDialog.AnyFile)
    dlg.setNameFilter("Json files (*.json)")

    if dlg.exec_():
        filenames = dlg.selectedFiles()
        with open(filenames[0], "w") as fp:
            json.dump(
                dict_state, fp, indent=4, separators=(",", ": "), ensure_ascii=False,
            )


def open_dialog():
    """Open a file dialog to read json dict from file."""
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

    updated_table()


def add_lang_dialog():
    """Add language dialog to left window."""
    form.left_window.setCurrentIndex(2)
    for key, value in dict_state["language_map"].items():
        form.new_language_com_box.addItem(key)


def new_dict_dialog():
    """Switch to new dict dialog window."""
    form.left_window.setCurrentIndex(4)

    # form.dict_table.clear()
    # form.dict_table.setRowCount(300)
    # form.dict_table.setColumnCount(2)
    # form.dict_table.setEditTriggers(QTableWidget.NoEditTriggers)
    # form.left_window.setCurrentIndex(0)
    # form.textEdit.setText("")
    # form.comboBox.setCurrentText("")


def new_dict_begin_dialog():
    """Open dialog to add a new dictionary and start with entering a new language."""
    if form.new_language_field_2.toPlainText():

        form.dict_table.clear()
        form.dict_table.setRowCount(300)
        form.dict_table.setColumnCount(1)
        form.dict_table.setEditTriggers(QTableWidget.NoEditTriggers)

        horHeaders = [form.new_language_field_2.toPlainText()]
        form.dict_table.setHorizontalHeaderLabels(horHeaders)
        form.dict_table.resizeColumnsToContents()
        form.dict_table.resizeRowsToContents()

        global language
        language = form.new_language_field_2.toPlainText()

        form.left_window.setCurrentIndex(0)
        form.textEdit.setText("")
        form.comboBox.setCurrentText("")


def create_table():
    """Create a new table."""
    form.dict_table.clear()
    form.dict_table.setRowCount(300)
    form.dict_table.setColumnCount(len(dict_state["language_map"]))
    form.dict_table.setEditTriggers(QTableWidget.NoEditTriggers)

    horHeaders = dict_state["language_map"].keys()

    form.dict_table.setHorizontalHeaderLabels(horHeaders)


def updated_table():
    """Updated table."""
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


def fill_new_language():
    """Fill new language adding it to the dict_state."""
    if form.new_language_field.toPlainText():
        form.left_window.setCurrentIndex(3)
        global new_language_counter

        dict_state["language_map"][form.new_language_field.toPlainText()] = dict()
        new_language_counter = 1
        form.add_translation_ref_text_field.setText(
            dict_state["language_map"][form.new_language_com_box.currentText()][
                str(new_language_counter)
            ]
        )
        form.add_translation_translation_field.clear()
    updated_table()


def prev_new_language():
    """Back button when adding new language."""
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

    updated_table()


def next_new_language():
    """Forward button when adding new language."""
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
    updated_table()


def finish_new_language():
    """Forward button when adding new language."""
    dict_state["language_map"][form.new_language_field.toPlainText()][
        str(new_language_counter)
    ] = form.add_translation_translation_field.toPlainText()
    form.add_translation_translation_field.clear()
    form.left_window.setCurrentIndex(0)
    updated_table()


def handle_table_click(row, column):
    set_left_window(row)


def set_left_window(idx):
    """Go into inspection mode."""
    global global_idx
    global_idx = idx

    update_lang_inspect_table()

    form.left_window.setCurrentIndex(1)
    form.tableWidget.clear()
    # default view
    form.stackedWidget_2.setCurrentIndex(1)

    key = str(idx + 1)
    exists = len(dict_state) != 0 and idx < len(dict_state["question_map"])
    if exists:
        question_id = dict_state["question_map"][idx]["question_id"]
        if question_id in dict_state["language_map"][language]:
            c_quest = dict_state["language_map"][language][question_id]
            c_ans = dict_state["question_map"][idx]["answer_type"]
        else:
            c_quest = ""
            if dict_state["question_map"][idx]:
                c_ans = dict_state["question_map"][idx]["answer_type"]
            else:
                c_ans = ""
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
            try:
                form.tableWidget.setItem(
                    row,
                    0,
                    QTableWidgetItem(dict_state["language_map"][language][option]),
                )
            except:
                pass
        form.tableWidget.resizeColumnsToContents()
        form.tableWidget.resizeRowsToContents()
    else:
        form.stackedWidget_2.setCurrentIndex(0)


def create_new_dict():
    """Initialize a new dict."""
    hash = str(uuid.uuid4())
    global dict_state
    dict_state = dict()
    dict_state.update(
        {
            "global_questionaire_id": hash,
            "language_map": {language: {}},
            "question_map": [],
        }
    )


def change_option():
    """Change view."""
    if form.comboBox.currentIndex() == 0 or form.comboBox.currentIndex() == 5:
        form.stackedWidget_2.setCurrentIndex(1)
    else:
        form.stackedWidget_2.setCurrentIndex(0)


def change_lang_inspect_mode(row, colum):
    """Go into inspection mode."""
    global language
    language = form.tableWidget_2.item(row, colum).text()
    global global_idx
    set_left_window(global_idx)


def update_lang_inspect_table():
    """Update language table."""
    try:
        form.tableWidget_2.clear()
        form.tableWidget_2.setColumnCount(1)
        form.tableWidget_2.setRowCount(len(dict_state["language_map"]))
        form.tableWidget_2.setHorizontalHeaderLabels(["Languages"])
        form.tableWidget_2.setEditTriggers(QTableWidget.NoEditTriggers)

        row_count = 0
        for key, value in dict_state["language_map"].items():
            form.tableWidget_2.setItem(row_count, 0, QTableWidgetItem(key))
            row_count += 1

        form.tableWidget_2.resizeColumnsToContents()
        form.tableWidget_2.resizeRowsToContents()
    except:
        pass


def cancel_inspect_mode():
    form.left_window.setCurrentIndex(0)


def write_to_dict():
    """Write """

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
        #        __import__('pudb').set_trace()
        if len(dict_state) == 0:
            create_new_dict()
            createTable()
        if quest_text in dict_state["language_map"][language].values():
            keys = [
                key
                for key, value in dict_state["language_map"][language].items()
                if value == quest_text
            ]
            field_id = int(keys[0])
        else:
            field_id = (
                max(map(lambda x: int(x), dict_state["language_map"][language].keys(),))
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
        # form.dict_table.setItem(row_id, col_id, QTableWidgetItem(quest_text))
        updatedTable()

        if answer_type == 0 or answer_type == 5:
            options = []

            for row in range(form.tableWidget.rowCount()):
                curr_item = form.tableWidget.item(row, 0)
                if curr_item is None:
                    break
                next_field = field_id + row + 1
                if next_field > max(
                    map(
                        lambda x: int(x),
                        dict_state["question_map"][global_idx]["options"],
                    )
                ):
                    next_free_field = (
                        max(
                            map(
                                lambda x: int(x),
                                dict_state["language_map"][language].keys(),
                            )
                        )
                        + 1
                    )
                    nentry = str(next_free_field)
                    dict_state["language_map"][language].update(
                        {nentry: curr_item.text()}
                    )
                    options.append((nentry))
                    pass
                else:
                    options.append(str(next_field))
                    dict_state["language_map"][language].update(
                        {options[-1]: curr_item.text()}
                    )

            if global_idx > len(dict_state["question_map"]):
                dict_state["question_map"].append(
                    {
                        "question_id": str(field_id),
                        "answer_type": answer_desc,
                        "options": options,
                    }
                )
            else:
                dict_state["question_map"][global_idx]["question_id"] = str(field_id)
                dict_state["question_map"][global_idx]["answer_type"] = answer_desc
                dict_state["question_map"][global_idx]["options"] = options
        else:
            if global_idx > len(dict_state["question_map"]):
                dict_state["question_map"].append(
                    {"question_id": str(field_id), "answer_type": answer_desc}
                )
            else:
                dict_state["question_map"][global_idx]["question_id"] = str(field_id)
                dict_state["question_map"][global_idx]["answer_type"] = answer_desc

        form.dict_table.resizeColumnsToContents()
        form.dict_table.resizeRowsToContents()

        # reset lefthand side
        form.left_window.setCurrentIndex(0)
        updatedTable()


def close_application():
    exit()


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.load_dict.clicked.connect(open_dialog)
form.save_dict.clicked.connect(save_dialog)
form.new_dict.clicked.connect(new_dict_dialog)
form.add_language.clicked.connect(add_lang_dialog)
form.new_language_button.clicked.connect(fill_new_language)
form.new_language_button_2.clicked.connect(new_dict_begin_dialog)
form.add_translation_next.clicked.connect(next_new_language)
form.add_translation_back.clicked.connect(prev_new_language)
form.add_translation_finish.clicked.connect(finish_new_language)
form.dict_table.cellClicked.connect(handle_table_click)
form.ok_button.clicked.connect(write_to_dict)
form.cancel_button.clicked.connect(cancel_inspect_mode)
form.comboBox.currentIndexChanged.connect(change_option)
form.tableWidget_2.cellClicked.connect(change_lang_inspect_mode)

# create menu
# menubar = QMenuBar()
menubar = QMenuBar()
window.setMenuBar(menubar)

extractActionNew = QAction("&New")
extractActionNew.setShortcut("Ctrl+N")
extractActionNew.setStatusTip("Create-Dictonary")
extractActionNew.triggered.connect(newDictDialog)
menubar.addAction(extractActionNew)

extractActionLoad = QAction("&Load-File")
extractActionLoad.setShortcut("Ctrl+L")
extractActionLoad.setStatusTip("Leave The App")
extractActionLoad.triggered.connect(open_dialog)
menubar.addAction(extractActionLoad)

extractActionSave = QAction("&Save-File")
extractActionSave.setShortcut("Ctrl+S")
extractActionSave.setStatusTip("Leave The App")
extractActionSave.triggered.connect(save_dialog)
menubar.addAction(extractActionSave)

extractActionAddLan = QAction("&Add-Language")
extractActionAddLan.setShortcut("Ctrl+Q")
extractActionAddLan.setStatusTip("Leave The App")
extractActionAddLan.triggered.connect(add_lang_dialog)
menubar.addAction(extractActionAddLan)
menubar.addSeparator()

extractActionClose = QAction("&Close")
extractActionClose.setShortcut("Ctrl+Q")
extractActionClose.setStatusTip("Leave The App")
extractActionClose.triggered.connect(close_application)
menubar.addAction(extractActionClose)

window.show()
app.exec_()
