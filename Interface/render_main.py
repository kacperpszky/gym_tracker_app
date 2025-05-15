import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QStackedWidget, QComboBox, QTextEdit, QListWidget
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer, QTime
from Interface.utils import center_window, getDayWorkout, getUserID
from Data.db_configg import getRecordsFromTable

class NewWorkout(QWidget):
    def __init__(self):
        super().__init__()
        self.add_workout = QLabel("Add new exercise", self)
        self.add_workout.setGeometry(10,-10,450,75)
        self.add_workout.setFont(QFont("Segoe UI", 20))
        self.add_workout.setStyleSheet(""" 
                                       font-weight: bold;
                                        """)
        
        self.current_exercises = QLabel("Current exercises", self)
        self.current_exercises.setGeometry(465,-10,500,75)
        self.current_exercises.setFont(QFont("Segoe UI", 20))
        self.current_exercises.setStyleSheet(""" 
                                            font-weight: bold;
                                            """)
        
        self.current_exercises_data = QListWidget(self)
        self.current_exercises_data.setGeometry(480, 50, 485, 350)
        self.current_exercises_data.setFont(QFont("Segoe UI", 13))
        

        self.exercise = QLabel("Exercise: ", self)
        self.exercise.setGeometry(20, 50, 150, 60)
        self.exercise.setFont(QFont("Segoe UI", 13))
        
        self.exercise_data = QComboBox(self)
        self.exercise_data.addItems(getRecordsFromTable("SELECT name FROM exercises WHERE category='Push – Chest & Triceps'"))
        self.exercise_data.setGeometry(200, 50, 275, 50)
        self.exercise_data.setFont(QFont("Segoe UI", 10))
        
        self.series = QLabel("Series: ", self)
        self.series.setGeometry(20, 100, 150, 60)
        self.series.setFont(QFont("Segoe UI", 13))
        
        self.series_data = QComboBox(self)
        self.series_data.addItems(['1','2','3','4'])
        self.series_data.setGeometry(200, 100, 150, 50)
        self.series_data.setFont(QFont("Segoe UI", 10))
      
        self.repetitions = QLabel("Repetitions: ", self)
        self.repetitions.setGeometry(20, 150, 150, 60)
        self.repetitions.setFont(QFont("Segoe UI", 13))
        
        self.repetitions_data = QLineEdit(self)
        self.repetitions_data.setGeometry(200, 150, 150, 50)
        self.repetitions_data.setFont(QFont("Segoe UI", 10))
        
        self.weight = QLabel("Weight: ", self)
        self.weight.setGeometry(20, 200, 150, 60)
        self.weight.setFont(QFont("Segoe UI", 13))  
        
        self.weight_data = QLineEdit(self)
        self.weight_data.setGeometry(200, 200, 275, 50)
        self.weight_data.setFont(QFont("Segoe UI", 10))
        
        self.notes = QLabel("Notes: ", self)
        self.notes.setGeometry(20, 250, 150, 60)
        self.notes.setFont(QFont("Segoe UI", 13))  
        
        self.notes_data = QTextEdit(self)
        self.notes_data.setGeometry(200, 250, 275, 150)
        self.notes_data.setFont(QFont("Segoe UI", 10))
        
        self.button_save_exercise = QPushButton("+ Add exercise", self)
        self.button_save_exercise.setGeometry(20, 400, 230, 50)
        self.button_save_exercise.setFont(QFont("Segoe UI", 13))
        self.button_save_exercise.clicked.connect(self.handle_save_exercise_button)
        
        self.button_save_workout = QPushButton("+ Add workout", self)
        self.button_save_workout.setGeometry(250, 400, 230, 50)
        self.button_save_workout.setFont(QFont("Segoe UI", 13))
        
        
    def handle_save_exercise_button(self):
        user_id = int(getUserID())
        exercise = str(self.exercise_data.currentText())
        series = str(self.series_data.currentText())    
        repetitions = str(self.repetitions_data.text().strip())
        weight = str(self.weight_data.text().strip())
        notes = str(self.notes_data.toPlainText().strip())
        
        # mozna dodac pozniej error handling dla null data
        
        self.current_exercises_data.addItem(f"{exercise} - {series} x {repetitions} @ {weight} <...>")
    
class Measurements(QWidget):
     def __init__(self):
        super().__init__()
        
class History(QWidget):
     def __init__(self):
        super().__init__()
        
class Goals(QWidget):
     def __init__(self):
        super().__init__()
    


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
                                         #"border: 2px solid black;"
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
        
        self.new_workout = QPushButton("New Workout", self)
        self.new_workout.setGeometry(0, 230, 250, 50) 
        self.new_workout.setFont(QFont("Segoe UI", 15))
        self.new_workout.setStyleSheet("qproperty-alignment: 'AlignCenter';"
                                       "color: black;"
                                       "border: 1px solid black;"
                                       "border-radius: 5px;"
                                       "font-weight: bold;"
                                       "margin-left: 10px;"
                                       "margin-right: 10px;")
        self.new_workout.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        
        self.measurements = QPushButton("Measurements", self)
        self.measurements.setGeometry(250, 230, 250, 50) 
        self.measurements.setFont(QFont("Segoe UI", 15))
        self.measurements.setStyleSheet("color: black;"
                                        "qproperty-alignment: 'AlignCenter';"
                                        "border: 1px solid black;"
                                        "border-radius: 5px;"
                                        "font-weight: bold;"
                                        "margin-left: 10px;"
                                        "margin-right: 10px;")
        self.measurements.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        
        self.history = QPushButton("History", self)
        self.history.setGeometry(500, 230, 250, 50) 
        self.history.setFont(QFont("Segoe UI", 15))
        self.history.setStyleSheet("color: black;"
                                   "qproperty-alignment: 'AlignCenter';"
                                   "border: 1px solid black;"
                                   "border-radius: 5px;"
                                   "font-weight: bold;"
                                   "margin-left: 10px;"
                                   "margin-right: 10px;")
        self.history.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        
        self.goals = QPushButton("Goals", self)
        self.goals.setGeometry(750, 230, 250, 50) 
        self.goals.setFont(QFont("Segoe UI", 15))
        self.goals.setStyleSheet("color: black;"
                                 "qproperty-alignment: 'AlignCenter';"
                                 "border: 1px solid black;"
                                 "border-radius: 5px;"
                                 "font-weight: bold;"
                                 "margin-left: 10px;"
                                 "margin-right: 10px;")
        self.goals.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        
        self.central_widget = QWidget(self)
        self.central_widget.setGeometry(0, 300, 1000, 500)
        self.central_widget.setStyleSheet("""
                                            margin-left: 10px;
                                            margin-right: 10px;
                                            margin-bottom: 10px;
                                            padding: 10px;
                                          """)
        
        self.stack = QStackedWidget(self.central_widget)
        self.stack.setGeometry(0, 0, 1000, 500)
        self.workout_view = NewWorkout()
        self.measurements_view = Measurements()
        self.history_view = History()
        self.goals_view = Goals()
        
        self.stack.addWidget(self.workout_view)       
        self.stack.addWidget(self.measurements_view)  
        self.stack.addWidget(self.history_view)       
        self.stack.addWidget(self.goals_view) 
        
    def update_time(self):
        current_time = QTime.currentTime().toString('HH:mm:ss')
        self.time_label.setText(f"Current time: {current_time}")
        
    def start_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        
      
    
        
        