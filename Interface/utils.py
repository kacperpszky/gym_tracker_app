from PyQt5.QtGui import QGuiApplication

def center_window(window):
    screen = QGuiApplication.primaryScreen() 
    screen_geometry = screen.availableGeometry()
    center_point = screen_geometry.center()

    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(center_point)
    window.move(frame_geometry.topLeft())
    