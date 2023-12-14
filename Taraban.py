#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout,\
    QVBoxLayout, QInputDialog

app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(800, 500)
list_notes_label = QLabel('Список заміток')
list_tags_label = QLabel('Список тегів')
button_note_create = QPushButton('Створити замітку')
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')
button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_search = QPushButton('Шукати замітки за тегом')
field_tag = QLineEdit('')
field_text = QTextEdit()
list_notes = QListWidget()
list_tags = QListWidget()
main_line = QHBoxLayout()
v = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
v.addWidget(list_notes_label)
v.addWidget(list_notes)
h1.addWidget(button_note_create)
h1.addWidget(button_note_del)
h2.addWidget(button_note_save)
v.addLayout(h1)
v.addLayout(h2)
v.addWidget(list_tags_label)
v.addWidget(list_tags)
v.addWidget(field_tag)
h3.addWidget(button_tag_add)
h3.addWidget(button_tag_del)
h4.addWidget(button_tag_search)
v.addLayout(h3)
v.addLayout(h4)
main_line.addWidget(field_text, 2)
main_line.addLayout(v, 1)
notes_win.setLayout(main_line)
with open("notes.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


def show():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])


def add_note():
    name, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки:")
    if ok and name != "":
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
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False)


def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if tag not in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open("notes.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False)


def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])
        with open("notes.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False)


def search():
    tag = field_tag.text()
    if button_tag_search.text() == "Шукати замітки за тегом":
        filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                filtered[note] = notes[note]
        button_tag_search.setText("Скинути пошук")
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(filtered)
    elif button_tag_search.text() == "Скинути пошук":
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        field_tag.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Шукати замітки за тегом")


list_notes.itemClicked.connect(show)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(delete_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search)
notes_win.show()
app.exec_()
