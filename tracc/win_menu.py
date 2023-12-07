from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap


class WinMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Traveller Character Creator"
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 500
        self.icon = "images/icon.png"
        self.create_ui()

    def create_ui(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setStyleSheet("""
        background: 'white';
        """)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.draw_items()

    def draw_items(self):
        # Adding title image
        # self.image_logo = QPixmap("images/image_goes_here.png")
        # self.logo = QLabel()
        # self.logo.setPixmap(self.image_logo)
        # self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.grid.addWidget(self.logo, 0, 0)

        # Adding text
        self.menu_text = QLabel("Traveller Character Creator")
        self.menu_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_text.setStyleSheet("""
        font-size: 20px;
        """)
        self.grid.addWidget(self.menu_text, 0, 0)

        # Buttons
        self.button1 = QPushButton("Button One")
        self.button1.setStyleSheet("""
        *{
        border: 2px solid '#000000';
        border-radius: 10px;
        background: '#0e7190';
        font-size: 20px;
        color: 'white';
        }
        *:hover{
        background: '#000000';
        color: 'white';
        }
        """)
        self.button1.clicked.connect(self.button_click)
        self.grid.addWidget(self.button1, 1, 0)

    def button_click(self):
        pass
