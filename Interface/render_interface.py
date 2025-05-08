from Interface.render_user import User_Window
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont, QPixmap, QGuiApplication
from PyQt5.QtCore import Qt

def render_app():
    app = QApplication(sys.argv)
    window_user = User_Window()
    window_user.show()
    sys.exit(app.exec_())
    