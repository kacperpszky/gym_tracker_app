from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from Data.db_configg import getRecordFromTable, addValuesIntoUsers
from datetime import datetime

LOGIN_SESSION_END = False

class User_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gym Tracker - Select User")
        # self.setStyleSheet("background-color: #194a05;")
        self.setGeometry(600, 250, 300, 350)
        self.setFixedSize(300,350)
        self.setWindowIcon(QIcon("Interface//logo.jpg"))
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 0, 200, 200)
        pixmap = QPixmap("Interface//user.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        
        
        self.enter_label = QLineEdit(self)
        self.enter_label.setPlaceholderText("Enter Username...")
        self.enter_label.setStyleSheet("""
                                       color: black;
                                       border: 2px solid black;
                                       """)
        self.enter_label.setFont(QFont("Helvetica [Cronyx]", 12))
        self.enter_label.setGeometry(20,200,250,30)
        
        self.enter_button = QPushButton("Enter", self)
        self.enter_button.setStyleSheet("""                                        
                                        color: black;
                                        border: 2px solid black;
                                        border-radius: 5px;                                         
                                        """)
        self.enter_button.setGeometry(105,240, 85, 25)
        self.enter_button.clicked.connect(self.handle_enter_button)
        
    def handle_enter_button(self):
        entered_username = str(self.enter_label.text().strip())
        if not entered_username:
            QMessageBox.warning(self, "Error", "Enter your username.")
            return
        else:
            result = getRecordFromTable(f"SELECT id FROM users WHERE username = '{entered_username}'")
            #print("Rezultat : " + result)
            if result == "None":
                QMessageBox.information(self, "No account", "User not found. Account has just been created.")
                addValuesIntoUsers(entered_username, " ", str(datetime.today().strftime('%Y-%m-%d')))
                LOGIN_SESSION_END = True
                # Przekierowywanie do kolejnego okna
            elif result != "None":
                QMessageBox.information(self, "Success", f"Logged as {entered_username}")
                LOGIN_SESSION_END = True
                # Przekierowywanie do kolejnego okna
        