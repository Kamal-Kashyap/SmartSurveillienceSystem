import sqlite3
connection = sqlite3.connect('Detailss.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (fname,dat,time,street,colony,city,Nearest_Police_Station,Mobile_number,Email,Description_of_incident )''')
connection.commit()
connection.close()
