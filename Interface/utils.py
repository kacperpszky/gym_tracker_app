from PyQt5.QtGui import QGuiApplication
import datetime

def center_window(window):
    screen = QGuiApplication.primaryScreen() 
    screen_geometry = screen.availableGeometry()
    center_point = screen_geometry.center()

    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(center_point)
    window.move(frame_geometry.topLeft())

USER_ID = 0
   
WORKOUT_PLAN = {
    'Monday': '🔥 Push Day – Bench & Triceps',
    'Tuesday':'🧲 Pull Day – Back & Biceps',
    'Wednesday':'🦵 Legs Day - Squats Incoming',
    'Thursday':'💨 Cardio – Move & Chill',
    'Friday':'💪 Upper Body – Pump Day',
    'Saturday':'🏋️ Legs + Core - Stabilize & Strengthen',
    'Sunday':'🛌 Rest Day – Recharge Mode'
}

def getDayWorkout():
    day = datetime.datetime.now()
    day = str(day.strftime("%A"))
    
    return str(WORKOUT_PLAN[day])

def setUserID(id):
    USER_ID = id
    
def getUserID():
    return USER_ID