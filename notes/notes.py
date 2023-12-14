#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from ui import Ui_MainWindow
import json


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()
        with open("notes.json", "r") as file:
            self.notes = json.load(file)
            self.ui.listWidget.addItems(self.notes)

    def show_note(self):
        key = self.ui.listWidget.selectedItems()[0].text()
        self.ui.textEdit.setText(self.notes[key]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[key]["теги"])

    def add_note(self):
        name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки:")
        if ok:
            self.notes[name] = {"текст": "", "теги": []}
            self.ui.listWidget.addItem(name)

    def save_note(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            self.notes[key]["текст"] = self.ui.textEdit.toPlainText()
            with open("notes.json", "w") as file:
                json.dump(self.notes, file, ensure_ascii=False)

    def delete_note(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            del self.notes[key]
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.textEdit.clear()
            self.ui.listWidget.addItems(self.notes)
            with open("notes.json", "w") as file:
                json.dump(self.notes, file, ensure_ascii=False)

    def add_tag(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            tag = self.ui.lineEdit.text()
            if tag not in self.notes[key]["теги"]:
                self.notes[key]["теги"].append(tag)
                self.ui.listWidget_2.addItem(tag)
                self.ui.lineEdit.clear()
                with open("notes.json", "w") as file:
                    json.dump(self.notes, file, ensure_ascii=False)

    def connections(self):
        self.ui.listWidget.clicked.connect(self.show_note)
        self.ui.pushButton_2.clicked.connect(self.add_note)
        self.ui.pushButton_4.clicked.connect(self.save_note)
        self.ui.pushButton_3.clicked.connect(self.delete_note)
        self.ui.pushButton_6.clicked.connect(self.add_tag)


app = QApplication([])
window = Widget()
window.show()
app.exec()
