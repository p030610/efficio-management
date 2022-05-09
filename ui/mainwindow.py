from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QFileDialog, QInputDialog, QLabel, QWidget, QPushButton, QTableWidget
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
import PyQt6.QtWidgets

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()