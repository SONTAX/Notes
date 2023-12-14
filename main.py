#!/usr/bin/python
# -*- coding: windows-1251 -*-

from PyQt5.QtWidgets import QApplication
from random import shuffle, choice
from time import sleep

app = QApplication([])

from main_window import *
from menu_window import *   


class Question:
    def __init__(self, question, answer, wrong1, wrong2, wrong3):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.attempts = 0
        self.points = 0


questions = []
q = Question("1 + 1", "0", "3", "4", "5")
questions.append(q)
q = Question("2 + 1", "0", "3", "4", "5")
questions.append(q)
q = Question("3 + 1", "0", "3", "4", "5")
questions.append(q)
q = Question("4 + 1", "0", "3", "4", "5")
questions.append(q)

rb_list = [rb1, rb2, rb3, rb4]


def new_question():
    global question, rb_list
    rb_group.setExclusive(False)
    rb_list[0].setChecked(False)
    rb_list[1].setChecked(False)
    rb_list[2].setChecked(False)
    rb_list[3].setChecked(False)
    rb_group.setExclusive(True)
    question = choice(questions)
    shuffle(rb_list)
    rb_list[0].setText(question.answer)
    rb_list[1].setText(question.wrong1)
    rb_list[2].setText(question.wrong2)
    rb_list[3].setText(question.wrong3)
    lb_question.setText(question.question)



def check():
    if rb_list[0].isChecked():
        lb_result.setText("Правильно")
        question.points += 1
    else:
        lb_result.setText("Не правильно")
    lb_right.setText(question.answer)
    question.attempts += 1


def click_ok():
    if btn_answer.text() == "Відповісти":
        btn_answer.setText("Наступне питання")
        check()
        radio_box.hide()
        result_box.show()
    else:
        btn_answer.setText("Відповісти")
        radio_box.show()
        result_box.hide()
        new_question()


def show_menu():
    lb_7.setText("Кількість відповідей: " +
                 str(question.attempts) + "\nВідсоток правильних відповідей: " +
                 str(question.points / question.attempts * 100) + "%")
    window.hide()
    menu_window.show()


def show_test():
    menu_window.hide()
    window.show()
    new_question()


def rest():
    menu_window.hide()
    window.hide()
    sleep(timer.value() * 60)
    window.show()


def add_question():
    q = Question(le_1.text(), le_2.text(), le_3.text(), le_4.text(), le_5.text())
    questions.append(q)
    clear()


def clear():
    le_1.clear()
    le_2.clear()
    le_3.clear()
    le_4.clear()
    le_5.clear()


new_question()
btn_answer.clicked.connect(click_ok)
btn_menu.clicked.connect(show_menu)
btn_back.clicked.connect(show_test)
btn_break.clicked.connect(rest)
btn_add.clicked.connect(add_question)
btn_clear.clicked.connect(clear)

window.show()
app.exec()
