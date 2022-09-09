from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from windows.main_window import MainWindow
import sys

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.userCount = 0
        self.users = self.initUsers()
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def initUsers(self):
        userDict = {"username":[],"password":[]}
        file = open("db.json")
        data = json.load(file)
        for user in data['users']:
            userDict["username"].append(user["username"])
            userDict["password"].append(user["password"])
        file.close()
        self.userCount = len(userDict)
        return userDict
            

    def handleLogin(self):
        for i in range(self.userCount):
            if (self.textName.text() == self.users["username"][i] and
                self.textPass.text() == self.users["password"][i]):
                self.accept()
                break
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Bad user or password')
                break

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow.Ui()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        print()
        window = Test()
        window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
