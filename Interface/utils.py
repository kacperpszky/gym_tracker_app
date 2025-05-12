from PyQt5.QtGui import QGuiApplication
import datetime

def center_window(window):
    screen = QGuiApplication.primaryScreen() 
    screen_geometry = screen.availableGeometry()
    center_point = screen_geometry.center()

    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(center_point)
    window.move(frame_geometry.topLeft())
    
    
WORKOUT_PLAN = {
    'Monday': 'Push Day',
    'Tuesday':'Pull Day',
    'Wednesday':'Legs Day',
    'Thursday':'Cardio',
    'Friday':'Upper Body',
    'Saturday':'Legs + Core',
    'Sunday':'Rest Day'
}

def getDayWorkout():
    day = datetime.datetime.now()
    day = str(day.strftime("%A"))
    
    return str(WORKOUT_PLAN[day])