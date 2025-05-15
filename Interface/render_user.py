from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap, QGuiApplication
from PyQt5.QtCore import Qt, pyqtSignal
from Data.db_configg import getRecordFromTable
from Interface.render_register import *
from Interface.utils import center_window, setUserID, getUserID
from Interface.render_main import Main_Window

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor) 
        self.setStyleSheet("color: black; text-decoration: underline;") 

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

class User_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 350)
        center_window(self)
        self.setWindowTitle("Gym Tracker - Select User")
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
        
        self.register_label = ClickableLabel("Create an account.", self)
        self.register_label.setGeometry(102, 270, 100, 30)
        self.register_label.clicked.connect(self.handle_register_label) 
        
    def handle_enter_button(self):
        entered_username = str(self.enter_label.text().strip())
        if not entered_username:
            QMessageBox.warning(self, "Error", "Enter your username.")
            return
        else:
            result = getRecordFromTable(f"SELECT id FROM users WHERE username = '{entered_username}'")
            if result == "None":
                QMessageBox.information(self, "No account", "User not found. Try again or create an account!")
            elif result != "None":
                setUserID(int(result))
                self.main_window = Main_Window(entered_username)
                self.main_window.show()
                self.close()

                
    def handle_register_label(self):
        self.register_window = Register_Window()
        self.register_window.show()
        