#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Відзеркалити")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()  # Головна лінія
col1 = QVBoxLayout()  # ділиться на два стовпці
col2 = QVBoxLayout()
col1.addWidget(btn_dir)  # в першому - кнопка вибору каталогу
col1.addWidget(lw_files)  # 1 список файлів
col2.addWidget(lb_image, 95)  # в другому - картинка
row_tools = QHBoxLayout()  # 1 ряд кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

workdir = ''


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = os.listdir(workdir)
    lw_files.clear()
    for file in filenames:
        for ext in extensions:
            if file.endswith(ext):
                lw_files.addItem(file)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None

    def loadImage(self, filename):
        self.filename = filename
        self.image = Image.open(os.path.join(workdir, filename))

    def showImage(self, path):
        lb_image.hide()
        image = QPixmap(path).scaled(lb_image.width(), lb_image.height(), Qt.KeepAspectRatio)
        lb_image.setPixmap(image)
        lb_image.show()

    def saveImage(self):
        path = os.path.join(workdir, "Modified")
        if not os.path.exists(path) and not os.path.isdir(path):
            os.mkdir(path)
        self.image.save(os.path.join(workdir, "Modified", self.filename))

    def bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        self.showImage(os.path.join(workdir, "Modified", self.filename))

workimage = ImageProcessor()


def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage(os.path.join(workdir, filename))


lw_files.clicked.connect(showChosenImage)
btn_dir.clicked.connect(showFilenamesList)
btn_bw.clicked.connect(workimage.bw)

win.show()
app.exec_()
