import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from win_menu import WinMenu
from stat_win import StatMenu


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_menu = StatMenu()
    win_menu.show()
    sys.exit(app.exec())
