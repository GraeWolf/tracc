from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QLabel, QPushButton,
    QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap


class StatMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "TCC Stat Generation"
        # self.setGeometry(200, 200, 400, 300)
        # self.roll_label_width = 20
        self.setFixedSize(400, 300)
        self.roll_label_height = 20
        self.font_size = 18

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Labels to list the rolled numbers

        self.roll1 = QLabel()
        self.grid.addWidget(self.roll1, 0, 3)
        self.roll1.setStyleSheet("""
            background: grey;
            font-size: (self.font_size)px;
        """)
        #self.roll1.setFixedWidth(self.roll_label_width)
        self.roll1.setFixedHeight(self.roll_label_height)
        self.roll1.setText("10")
        self.roll1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.roll2 = QLabel()
        self.grid.addWidget(self.roll2, 0, 4)
        self.roll2.setStyleSheet("""
            background: grey;
            font-size: (self.font_size)px;
        """)
        #self.roll2.setFixedWidth(self.roll_label_width)
        self.roll2.setFixedHeight(self.roll_label_height)

        self.roll3 = QLabel()
        self.grid.addWidget(self.roll3, 0, 5)
        self.roll3.setStyleSheet("""
            background: grey;
            font-size: (self.font_size)px;
        """)
        #self.roll3.setFixedWidth(self.roll_label_width)
        self.roll3.setFixedHeight(self.roll_label_height)

        self.roll4 = QLabel()
        self.grid.addWidget(self.roll4, 0, 6)
        self.roll4.setStyleSheet("""
            background: grey;
            font-size: (self.font_size)px;
        """)
        #self.roll4.setFixedWidth(self.roll_label_width)
        self.roll4.setFixedHeight(self.roll_label_height)

        self.roll5 = QLabel()
        self.grid.addWidget(self.roll5, 0, 7)
        self.roll5.setStyleSheet("""
            background: grey;
            font-size: (self.font_size)px;
        """)
        #self.roll5.setFixedWidth(self.roll_label_width)
        self.roll5.setFixedHeight(self.roll_label_height)

        self.roll6 = QLabel()
        self.grid.addWidget(self.roll6, 0, 8)
        self.roll6.setStyleSheet("""
            background: grey;
            font-size: (self.font_size)px;
        """)
        #self.roll6.setFixedWidth(self.roll_label_width)
        self.roll6.setFixedHeight(self.roll_label_height)

        # spacer label
        self.col_spacer = QLabel()
        self.grid.addWidget(self.col_spacer, 0, 2)
        self.col_spacer.setFixedHeight(20)

        # combo boxes to assign stat numbers
        self.str_box = QComboBox()
        self.grid.addWidget(self.str_box, 1, 0)
        self.str_label = QLabel("Strength")
        self.grid.addWidget(self.str_label, 1, 1)

        self.dex_box = QComboBox()
        self.grid.addWidget(self.dex_box, 2, 0)
        self.dex_label = QLabel("Strength")
        self.grid.addWidget(self.dex_label, 2, 1)

        self.end_box = QComboBox()
        self.grid.addWidget(self.end_box, 3, 0)
        self.end_label = QLabel("Endurance")
        self.grid.addWidget(self.end_label, 3, 1)

        self.int_box = QComboBox()
        self.grid.addWidget(self.int_box, 4, 0)
        self.int_label = QLabel("Intelect")
        self.grid.addWidget(self.int_label, 4, 1)

        self.edu_box = QComboBox()
        self.grid.addWidget(self.edu_box, 5, 0)
        self.edu_label = QLabel("Education")
        self.grid.addWidget(self.edu_label, 5, 1)

        self.soc_box = QComboBox()
        self.grid.addWidget(self.soc_box, 6, 0)
        self.soc_label = QLabel("Social")
        self.grid.addWidget(self.soc_label, 6, 1)

        # Roll and continue buttons
        self.roll_button = QPushButton("Roll")
        self.grid.addWidget(self.roll_button, 7, 3, 1, 3)

        self.continue_button = QPushButton("Continue")
        self.grid.addWidget(self.continue_button, 7, 6, 1, 3)