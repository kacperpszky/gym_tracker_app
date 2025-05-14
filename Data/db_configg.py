import psycopg2
from urllib import request

INTERNET_CONNECTION = False
DATABASE_CONNECTION = False

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1998" # tutaj wklej własny pass do swojego postgresa.
DB_HOST = "localhost"
DB_PORT = "5432" # jesli dzialasz na innym porcie to zmien go tutaj.

CONN = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
CUR = CONN.cursor()

def check_internet():
    try:
        request.urlopen('https://www.google.com/', timeout=1)
        return True
    except request.URLError as err: 
        return False
    
def connect_db():
    try:
        psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
        return True
    except:
        return False
    
def createTables():
    # w tabeli body_metrics w chest/arms/waist obwody. 
    CUR.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                
                CREATE TABLE IF NOT EXISTS workouts (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                date DATE NOT NULL,
                notes TEXT
                );
                
                CREATE TABLE IF NOT EXISTS exercises (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(100),
                description TEXT
                );
                
                CREATE TABLE IF NOT EXISTS workout_entries (
                    id SERIAL PRIMARY KEY,
                    workout_id INTEGER REFERENCES workouts(id) ON DELETE CASCADE,
                    exercise_id INTEGER REFERENCES exercises(id) ON DELETE CASCADE,
                    sets INTEGER NOT NULL,
                    reps INTEGER NOT NULL, 
                    weight NUMERIC(5,2),
                    notes TEXT
                );
                
                CREATE TABLE IF NOT EXISTS body_metrics (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    date DATE NOT NULL,
                    weight NUMERIC(5,2),
                    chest NUMERIC(5,2), 
                    arms NUMERIC(5,2),
                    waist NUMERIC(5,2)
                );              
                """)
    CONN.commit()
    print("Utworzono tabele.")
    
def getRecordFromTable(request_db):
    CUR.execute(request_db)
    CONN.commit()
    
    result = str(CUR.fetchone())
    
    result = result.replace('(','')
    result = result.replace(')','')
    result = result.replace(',','')
    
    return result

def getRecordsFromTable(request_db):
    CUR.execute(request_db)
    CONN.commit()
    
    results = CUR.fetchall()

    cleaned_results = []
    for row in results:
        cleaned_row = ''.join(str(val) for val in row)
        cleaned_results.append(cleaned_row)
    
    return cleaned_results

def addValuesIntoUsers(username, email, created_at):
    CUR.execute(f"""
                INSERT INTO users (username, email, created_at) 
                VALUES (%s, %s, %s)
                """, (username, email, created_at))
    CONN.commit()
    
def addValuesIntoWorkouts(user_id, date, notes):
    CUR.execute(f"""
                INSERT INTO workouts (user_id, date, notes) 
                VALUES (%s, %s, %s)
                """, (user_id, date, notes))
    CONN.commit()

def addValuesIntoExercises(name, category, description):
    CUR.execute(f"""
                INSERT INTO exercises (name, category, description) 
                VALUES (%s, %s, %s)
                """, (name, category, description))
    CONN.commit()

def addValuesIntoWorkout_entries(workout_id, exercise_id, sets, reps, weight, notes):
    CUR.execute(f"""
                INSERT INTO workout_entries (workout_id, exercise_id, sets, reps, weight, notes) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (workout_id, exercise_id, sets, reps, weight, notes))
    CONN.commit()
    
def addValuesIntoBody_metrics (user_id, date, weight, chest, arms, waist):
    CUR.execute(f"""
                INSERT INTO body_metrics (user_id, date, weight, chest, arms, waist) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (user_id, date, weight, chest, arms, waist))
    CONN.commit()
    