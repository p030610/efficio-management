from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

from ui.stacks import Stacks
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Stacks()
    sys.exit(app.exec())