import sqlite3
def createTable():
    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()
    print("Successfully Connected to SQLite")
    try: cursor.execute('''CREATE TABLE USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT)''')
    except: pass
    cursor.execute('''INSERT INTO USERS (USERNAME,EMAIL,PASSWORD) VALUES ('Daepyonim','ahsnyn@gmail.com','400Lux!!')''')
    connection.commit()
    result = cursor.execute('''SELECT * FROM USERS''')
    for data in result: print (data)
    cursor.close()
createTable()