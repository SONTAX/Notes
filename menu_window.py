#!/usr/bin/python
# -*- coding: windows-1251 -*-

from PyQt5.QtWidgets import (
    QLabel, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit
)

menu_window = QWidget()

btn_add = QPushButton("������ ���������")
btn_clear = QPushButton("��������")
btn_back = QPushButton("�����")

lb_1 = QLabel("������ ���������")
lb_2 = QLabel("������ ��������� �������")
lb_3 = QLabel("������ ����� ����������� �������")
lb_4 = QLabel("������ ����� ����������� �������")
lb_5 = QLabel("������ ����� ����������� �������")
lb_6 = QLabel("����������")
lb_7 = QLabel("")

le_1 = QLineEdit()
le_2 = QLineEdit()
le_3 = QLineEdit()
le_4 = QLineEdit()
le_5 = QLineEdit()

main_line = QVBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

v1.addWidget(lb_1)
v1.addWidget(lb_2)
v1.addWidget(lb_3)
v1.addWidget(lb_4)
v1.addWidget(lb_5)
v2.addWidget(le_1)
v2.addWidget(le_2)
v2.addWidget(le_3)
v2.addWidget(le_4)
v2.addWidget(le_5)
h1.addLayout(v1)
h1.addLayout(v2)
h2.addWidget(btn_add)
h2.addWidget(btn_clear)
main_line.addLayout(h1)
main_line.addLayout(h2)
main_line.addWidget(lb_6)
main_line.addWidget(lb_7)
main_line.addWidget(btn_back)

menu_window.setLayout(main_line)
