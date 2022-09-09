from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *   

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QFontDatabase.addApplicationFont("Resources/OpenSans-Regular.ttf")
        QFontDatabase.addApplicationFont("Resources/OpenSans-Bold.ttf")
        QFontDatabase.addApplicationFont("Resources/OpenSans-BoldItalic.ttf")
        self.font_OSRegular = QFont("OpenSans-Regular")
        self.font_OSBold = QFont("OpenSans-Bold")
        self.font_OSBoldItalic = QFont("OpenSans-BoldItalic")
        self.window = QWindow()