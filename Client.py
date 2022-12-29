from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
import sys
import socket


#install PyQt5

# Essais d'interface

# class MyGUI(QMainWindow):
#
#     def __init__(self):
#         super(MyGUI, self).__init__()
#         uic.loadUi("untitled.ui", self)
#         self.show()
#
#         self.pushButton.clicked.connect(self.login)
#         self.pushButton_2.clicked.connect(lambda: self.sayit(self.textEdit.toPlainText()))
#         self.actionClose.triggered.connect(exit)
#
#
#     def login(self):
#         if self.lineEdit.text() == "momo" and self.lineEdit_2.text() == "momo":
#             self.textEdit.setEnabled(True)
#             self.pushButton_2.setEnabled(True)
#         else:
#             message = QMessageBox()
#             message.setText("Invalid login")
#             message.exec_()
#
#     def  sayit(self, msg):
#         message = QMessageBox()
#         message.setText(msg)
#         message.exec_()
#
# def main():
#     app = QApplication([])
#     window = MyGUI()
#     app.exec_()

host = "127.0.0.1"  # The server's hostname or IP address
port = 65432  # The port used by the server

message = 'Client'

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

while message != 'disconnect':
    message = input("\nCommande Server : ")
    client_socket.send(message.encode())
    message = client_socket.recv(1024).decode()
    print(f"Message du serveur : \n{message}\n")

# Fermeture de la socket du client
client_socket.close()
print("Connexion arrêter : Server")

