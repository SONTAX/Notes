#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, \
    QVBoxLayout, QInputDialog

app = QApplication([])
notes_win = QWidget()
notes_win.resize(700, 500)
lb_notes = QLabel('Список заміток')
lb_tegs = QLabel('Список тегів')
btn_note_create = QPushButton('Створити замітку')
btn_note_delete = QPushButton('Видалити замітку')
btn_note_save = QPushButton('Зберегти замітку')
btn_teg_add = QPushButton('Додати до замітки')
btn_teg_delete = QPushButton('Відкріпити від замітки')
btn_teg_search = QPushButton('Шукати замітки за тегом')
field_teg = QLineEdit('')
field_text = QTextEdit()
list_tegs = QListWidget()
list_notes = QListWidget()
h1 = QHBoxLayout()
left_loyaut = QVBoxLayout()
left_loyaut.addWidget(field_text)
right_loyaut = QVBoxLayout()
right_loyaut.addWidget(lb_notes)
right_loyaut.addWidget(list_notes)
right_loyaut.addWidget(btn_note_create)
right_loyaut.addWidget(btn_note_delete)
right_loyaut.addWidget(btn_note_save)
right_loyaut.addWidget(lb_tegs)
right_loyaut.addWidget(list_tegs)
right_loyaut.addWidget(field_teg)
right_loyaut.addWidget(btn_teg_add)
right_loyaut.addWidget(btn_teg_delete)
right_loyaut.addWidget(btn_teg_search)
h1.addLayout(left_loyaut, 2)
h1.addLayout(right_loyaut, 1)
notes_win.setLayout(h1)
with open("notes.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


def show():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])
    list_tegs.clear()
    list_tegs.addItems(notes[key]["теги"])


def add_note():
    name, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки:")
    if ok:
        notes[name] = {"текст": "", "теги": []}
        list_notes.addItem(name)


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open("notes.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False)


def delete_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tegs.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False)


def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        teg = field_teg.text()
        if teg not in notes[key]["теги"]:
            notes[key]["теги"].append(teg)
            list_tegs.addItem(teg)
            field_teg.clear()
            with open("notes.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False)


def delete_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        note = list_tegs.selectedItems()[0].text()
        notes[key]["теги"].remove(note)
        list_tegs.clear()
        list_tegs.addItems(notes[key]["теги"])
        with open("notes.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False)


def search():
    teg = field_teg.text()
    if btn_teg_search.text() == "Шукати замітки за тегом":
        filter = {}
        for note in notes:
            if teg in notes[note]["теги"]:
                filter[note] = notes[note]
        btn_teg_search.setText("Скинути пошук")
        list_notes.clear()
        list_tegs.clear()
        field_text.clear()
        list_notes.addItems(filter)
    elif btn_teg_search.text() == "Скинути пошук":
        list_notes.clear()
        list_tegs.clear()
        field_text.clear()
        field_teg.clear()
        list_notes.addItems(notes)
        btn_teg_search.setText("Шукати замітки за тегом")


list_notes.clicked.connect(show)
btn_note_create.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)
btn_note_delete.clicked.connect(delete_note)
btn_teg_add.clicked.connect(add_tag)
btn_teg_delete.clicked.connect(delete_tag)
btn_teg_search.clicked.connect(search)
notes_win.show()
app.exec_()
