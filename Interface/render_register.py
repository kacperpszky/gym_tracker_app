from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from Data.db_configg import addValuesIntoUsers
from datetime import datetime

class Register_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gym Tracker - Register User")
        self.setGeometry(600, 250, 300, 350)
        self.setFixedSize(300,350)
        self.setWindowIcon(QIcon("Interface//logo.jpg"))
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 0, 200, 200)
        pixmap = QPixmap("Interface//register.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

        self.user_label = QLineEdit(self)
        self.user_label.setPlaceholderText("Enter Username...")
        self.user_label.setStyleSheet("""
                                       color: black;
                                       border: 2px solid black;
                                       """)
        self.user_label.setFont(QFont("Helvetica [Cronyx]", 12))
        self.user_label.setGeometry(20,200,250,30)
        
        self.email_label = QLineEdit(self)
        self.email_label.setPlaceholderText("Enter E-mail...")
        self.email_label.setStyleSheet("""
                                       color: black;
                                       border: 2px solid black;
                                       """)
        self.email_label.setFont(QFont("Helvetica [Cronyx]", 12))
        self.email_label.setGeometry(20,240,250,30)
        
        self.enter_button = QPushButton("Register", self)
        self.enter_button.setStyleSheet("""                                        
                                        color: black;
                                        border: 2px solid black;
                                        border-radius: 5px;                                         
                                        """)
        self.enter_button.setGeometry(105,280, 85, 25)
        self.enter_button.clicked.connect(self.handle_enter_button)
                
    def handle_enter_button(self):
        entered_username = str(self.user_label.text().strip())
        entered_email = str(self.email_label.text().strip())
        if (not entered_username) or (not entered_email) :
            QMessageBox.warning(self, "Error", "Enter information!.")
            return
        else:
            addValuesIntoUsers(entered_username, entered_email, str(datetime.today().strftime('%Y-%m-%d')))
            QMessageBox.information(self, "Account created!", "Success! Account has just been created.")
            self.close()
        