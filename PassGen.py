# This Python file uses the following encoding: utf-8
import sys
import os
import smtplib, random, string

from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox
from PySide2.QtCore import QFile
from PySide2 import QtGui
from PySide2.QtUiTools import QUiLoader


class PassGen(QWidget):
    def __init__(self):
        super(PassGen, self).__init__()
        self.load_ui()
        self.setFixedSize(217, 108)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setWindowTitle('PassGen')

        self.passGen = self.findChild(QPushButton, "passGen")
        self.passGen.clicked.connect(self.Generate)


    def Generate(self):
        passOut = self.findChild(QLabel, "passOut")
        Char = self.findChild(QLineEdit, "Char")
        Char = int(Char.text())
        if Char >= 6 and Char <= 20:
            password_length = (Char)
            password_characters = string.ascii_letters + string.digits + string.punctuation
            password = []
            for x in range(password_length):
                password.append(random.choice(password_characters))
            p_out = (''.join(password))
            passOut.setText(p_out)
        else:
            QMessageBox.critical(
                None,
                "Invalid Character Length",
                '''The character length must be between 6 and 20 characters.''')
            return



    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    widget = PassGen()
    widget.show()
    sys.exit(app.exec_())
