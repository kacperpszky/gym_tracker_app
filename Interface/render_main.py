import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer, QTime
from Interface.utils import center_window, getDayWorkout

class Main_Window(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Gym Tracker")
        self.resize(1000, 800)
        center_window(self) 
        self.setFixedSize(1000, 800)
        self.setWindowIcon(QIcon("Interface//logo.jpg"))
        
        self.welcome_label = QLabel(f"Welcome - {username}", self)
        self.welcome_label.setGeometry(20, 30, 700, 40)
        self.welcome_label.setFont(QFont("Segoe UI", 20))
        self.welcome_label.setStyleSheet("padding-left: 5px;"
                                         "font-weight: bold;"
                                        #  "border: 2px solid black;"
                                            "padding-right: 5px;"
                                            "margin-left: 10px;"
                                            "margin-right: 10px;")

        self.time_label = QLabel("", self)
        self.time_label.setGeometry(800, 50, 200, 20)
        self.time_label.setFont(QFont("Segoe UI", 10))
        self.time_label.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        # "border: 2px solid black;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.update_time()
        self.start_timer()

        self.line_label = QLabel(self)
        self.line_label.setGeometry(0, 70, 1000, 10)
        line = QPixmap("Interface//line.jpg")
        self.line_label.setPixmap(line)
        self.line_label.setScaledContents(True)
        
        self.today_workout = QLabel(f"Today's Workout",self)
        self.today_workout.setGeometry(30, 110, 350, 50)
        self.today_workout.setFont(QFont("Segoe UI", 20))
        self.today_workout.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        "border: 2px solid black;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
    def update_time(self):
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.time_label.setText(f"Current time: {current_time}")
        

    def start_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        
      
    
        
        