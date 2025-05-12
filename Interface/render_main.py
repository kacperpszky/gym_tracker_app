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
        
        self.today_workout = QLabel("Today's Workout",self)
        self.today_workout.setGeometry(30, 90, 350, 50)
        self.today_workout.setFont(QFont("Segoe UI", 20))
        self.today_workout.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.today_workout1 = QLabel(f"{getDayWorkout()}",self)
        self.today_workout1.setGeometry(50, 130, 350, 40)
        self.today_workout1.setFont(QFont("Segoe UI", 12))
        self.today_workout1.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.recent_progress = QLabel("Recent Progress",self)
        self.recent_progress.setGeometry(620, 90, 350, 50) 
        self.recent_progress.setFont(QFont("Segoe UI", 20))
        self.recent_progress.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.recent_progress1 = QLabel(f"💥 Recent Progress - #TODO",self)
        self.recent_progress1.setGeometry(640, 130, 350, 40)
        self.recent_progress1.setFont(QFont("Segoe UI", 12))
        self.recent_progress1.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.weight = QLabel(f"⚖️ Weight - #TODO",self)
        self.weight.setGeometry(640, 160, 350, 40)
        self.weight.setFont(QFont("Segoe UI", 12))
        self.weight.setStyleSheet("padding-left: 5px;"
                                        "font-weight: bold;"
                                        "padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.new_workout = QLabel("New Workout", self)
        self.new_workout.setGeometry(0, 230, 250, 50) 
        self.new_workout.setFont(QFont("Segoe UI", 15))
        self.new_workout.setStyleSheet(#"padding-left: 5px;"
                                       "qproperty-alignment: 'AlignCenter';"
                                       "color: black;"
                                        "border: 1px solid black;"
                                        "border-radius: 5px;"
                                        "font-weight: bold;"
                                        #"padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.measurements = QLabel("Measurements", self)
        self.measurements.setGeometry(250, 230, 250, 50) 
        self.measurements.setFont(QFont("Segoe UI", 15))
        self.measurements.setStyleSheet(#"padding-left: 5px;"
                                        "color: black;"
                                        "qproperty-alignment: 'AlignCenter';"
                                        "border: 1px solid black;"
                                        "border-radius: 5px;"
                                        "font-weight: bold;"
                                        #"padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.history = QLabel("History", self)
        self.history.setGeometry(500, 230, 250, 50) 
        self.history.setFont(QFont("Segoe UI", 15))
        self.history.setStyleSheet(#"padding-left: 5px;"
                                        "color: black;"
                                        "qproperty-alignment: 'AlignCenter';"
                                        "border: 1px solid black;"
                                        "border-radius: 5px;"
                                        "font-weight: bold;"
                                        #"padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        self.goals = QLabel("Goals", self)
        self.goals.setGeometry(750, 230, 250, 50) 
        self.goals.setFont(QFont("Segoe UI", 15))
        self.goals.setStyleSheet(#"padding-left: 5px;"
                                        "color: black;"
                                        "qproperty-alignment: 'AlignCenter';"
                                        "border: 1px solid black;"
                                        "border-radius: 5px;"
                                        "font-weight: bold;"
                                        #"padding-right: 5px;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        
        
        
    def update_time(self):
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.time_label.setText(f"Current time: {current_time}")
        
    def start_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        
      
    
        
        