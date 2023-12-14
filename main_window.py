#!/usr/bin/python
# -*- coding: windows-1251 -*-

from PyQt5.QtWidgets import (
    QLabel, QRadioButton, 
    QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QSpinBox,
    QButtonGroup, QGroupBox
)
from PyQt5.QtCore import Qt

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Memory Card")

btn_menu = QPushButton("Меню")
btn_break = QPushButton("Відпочити")
btn_answer = QPushButton("Відповісти")
timer = QSpinBox()

lb_question = QLabel("")
lb_break = QLabel("хвилин")
lb_result = QLabel("")
lb_right = QLabel("")

rb1 = QRadioButton("")
rb2 = QRadioButton("")
rb3 = QRadioButton("")
rb4 = QRadioButton("")
rb_group = QButtonGroup()
rb_group.addButton(rb1)
rb_group.addButton(rb2)
rb_group.addButton(rb3)
rb_group.addButton(rb4)

radio_box = QGroupBox("Варіанти відповідей")
result_box = QGroupBox("Результати теста")

main_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
h4_line = QHBoxLayout()

rb_v_line1 = QVBoxLayout()
rb_v_line2 = QVBoxLayout()
rb_h_line = QHBoxLayout()

result_line = QVBoxLayout()

rb_v_line1.addWidget(rb1)
rb_v_line1.addWidget(rb2)
rb_v_line2.addWidget(rb3)
rb_v_line2.addWidget(rb4)
rb_h_line.addLayout(rb_v_line1)
rb_h_line.addLayout(rb_v_line2)

result_line.addWidget(lb_result)
result_line.addWidget(lb_right, 1, Qt.AlignHCenter)

radio_box.setLayout(rb_h_line)
result_box.setLayout(result_line)

h1_line.addWidget(btn_menu)
h1_line.addStretch(1)
h1_line.addWidget(btn_break)
h1_line.addWidget(timer)
h1_line.addWidget(lb_break)
h2_line.addWidget(lb_question, 1, Qt.AlignHCenter | Qt.AlignVCenter)
h3_line.addWidget(radio_box)
h3_line.addWidget(result_box)
result_box.hide()
h4_line.addStretch(1)
h4_line.addWidget(btn_answer, 2)
h4_line.addStretch(1)
main_line.addLayout(h1_line, 1)
main_line.addLayout(h2_line, 2)
main_line.addLayout(h3_line, 8)
main_line.addStretch(1)
main_line.addLayout(h4_line, 1)
main_line.addStretch(1)
window.setLayout(main_line)
