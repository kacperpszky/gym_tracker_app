import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from Interface.utils import center_window

class Main_Window(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Gym Tracker")
        self.resize(1000, 800)
        center_window(self) 
        self.setFixedSize(1000, 800)
        self.setWindowIcon(QIcon("Interface//logo.jpg"))
        
        self.welcome_label = QLabel(f"Welcome {username}", self)
        self.welcome_label.setGeometry(20, 20, 600, 30)
        self.welcome_label.setFont(QFont("Segoe UI", 10))
        self.welcome_label.setStyleSheet("padding-left: 5px;"
                                            "padding-right: 5px;"
                                            "margin-left: 10px;"
                                            "margin-right: 10px;")
        
        
      
        
        
        