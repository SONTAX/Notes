import os
from PyQt6.QtWidgets import (
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
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()  # Основний рядок
col1 = QVBoxLayout()  # ділиться на два стовпці
col2 = QVBoxLayout()
col1.addWidget(btn_dir)  # у першому – кнопка вибору директорії
col1.addWidget(lw_files)  # та список файлів
col2.addWidget(lb_image, 95)  # у другому - картинка
row_tools = QHBoxLayout()  # та рядок кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

workdir = ""


def chooseFolder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def filter(list_files, list_extensions):
    result = []
    for file in list_files:
        for extension in list_extensions:
            if file.endswith(extension):
                result.append(file)
                break
    return result


def show():
    chooseFolder()
    list_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    files = filter(os.listdir(workdir), list_extensions)
    lw_files.clear()
    lw_files.addItems(files)


btn_dir.clicked.connect(show)
win.show()
app.exec()
