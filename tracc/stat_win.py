from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap


class StatMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "TCC Stat Generation"
        self.width = 600
        self.height = 500

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Labels to list the rolled numbers
        
        self.roll1 =  QLabel()
        self.grid.addWidget(self.roll1, 0, 0,)
        self.roll1.setStyleSheet("""
            background: grey;
        """)
        self.roll1.setFixedWidth(10)

        self.roll2 = QLabel()
        self.grid.addWidget(self.roll2, 0, 1)
        self.roll2.setStyleSheet("""
            background: grey;
        """)
        self.roll2.setFixedWidth(10)

        self.roll3 = QLabel()
        self.grid.addWidget(self.roll3, 0, 2)
        self.roll3.setStyleSheet("""
            background: grey;
        """)
        self.roll3.setFixedWidth(10)

        self.roll4= QLabel()
        self.grid.addWidget(self.roll4, 0, 3)
        self.roll4.setStyleSheet("""
            background: grey;
        """)
        self.roll4.setFixedWidth(10)

        self.roll5 = QLabel()
        self.grid.addWidget(self.roll5, 0, 4)
        self.roll5.setStyleSheet("""
            background: grey;
        """)
        self.roll5.setFixedWidth(10)

        self.roll6 = QLabel()
        self.grid.addWidget(self.roll6, 0, 5)
        self.roll6.setStyleSheet("""
            background: grey;
        """)
        self.roll6.setFixedWidth(10)

        
