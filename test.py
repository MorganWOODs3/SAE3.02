from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)

        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Add message")
        self.btnPress2 = QPushButton("Clear")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.append(f"Nouveau texte {self.i}")
        self.i += 1
#        self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("")
#        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
# # from PyQt5 import QtWidgets
# # from PyQt5.QtWidgets import QApplication, QMainWindow
# # import sys
# #
# #
# # class MyWindow(QMainWindow):
# #     def __init__(self):
# #         super(MyWindow, self).__init__()
# #         self.setGeometry(200, 200, 300, 300)
# #         self.setWindowTitle("Tech With ME!")
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.label = QtWidgets.QLabel(self)
# #         self.label.setText("my fist label !")
# #         self.label.move(50, 50)
# #         self.b1 = QtWidgets.QPushButton(self)
# #         self.b1.setText("Click me")
# #         self.b1.clicked.connect(self.clicked)
# #
# #     def clicked(self):
# #         self.label.setText("you pressed the boutton")
# #         self.update()
# #
# #     def update(self):
# #         self.label.adjustSize()
# #
# #
# # def clicked():
# #     print("clicked")
# #
# # def windows():
# #     app = QApplication(sys.argv)
# #     win = MyWindow()
# #     win.show()
# #     sys.exit(app.exec_())
# #
# # windows()
# from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
# import sys
#
#
#
# class TextEditDemo(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.i = 0
#         self.setWindowTitle("QTextEdit")
#         self.resize(300, 270)
#
#         self.textEdit = QTextEdit()
#         self.textEdit.setEnabled(False)
#         self.btnPress1 = QPushButton("Add message")
#         self.btnPress2 = QPushButton("Clear")
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.textEdit)
#         layout.addWidget(self.btnPress1)
#         layout.addWidget(self.btnPress2)
#         self.setLayout(layout)
#
#         self.btnPress1.clicked.connect(self.btnPress1_Clicked)
#         self.btnPress2.clicked.connect(self.btnPress2_Clicked)
#
#     def btnPress1_Clicked(self):
#         self.textEdit.append(f"Nouveau texte {self.i}")
#         self.i += 1
# #        self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")
#
#     def btnPress2_Clicked(self):
#         self.textEdit.setPlainText("")
# #        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = TextEditDemo()
#     win.show()
#     sys.exit(app.exec_())
#
# from __future__ import with_statement #for python 2.5
# with open('C:/Thread/numbers.txt', 'r') as f:
#     lines = f.readlines()
#
#
# print(lines)
#
