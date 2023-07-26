from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout 
app= QApplication([])
main_win=QWidget()
main_win.setWindowTitle('My frist app')
main_win.move(900,70)
main_win.resize(400,200)
main_win.show()
v_line=QVBoxLayout()
title=QLabel('HELLO WORLD')
v_line.addWidget(title,alignment=Qt.AlignCenter)
main_win.setLayout(v_line)



app.exec_()