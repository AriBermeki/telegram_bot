import psycopg2
import psycopg2.extras
import os

username = os.environ['USERNAME']
pwd = os.environ['EMAIL_USER_PASSWORD']
hostname = os.environ['HOSTNAME']
port_id = os.environ['PORT_ID']
database = os.environ['DATABASE']
db = None
date = None

try:
    db = psycopg2.connect(
        host = hostname, 
        dbname = database, 
        user = username, 
        password = pwd, 
        port = port_id)
    date = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print("Connected to Postgresql")
    create_table = ''' CREATE TABLE IF NOT EXISTS telegram_ari (
                        user_id serial PRIMARY KEY,
	                    ID VARCHAR (50) UNIQUE NOT NULL,
	                    email VARCHAR (50) NOT NULL) '''

    date.execute(create_table)

    sqlite_select_query = """SELECT * from telegram_ari"""
    date.execute(sqlite_select_query)
    postgresql_date = date.fetchall()
    print("Total rows are:  ", len(postgresql_date))
    print("Printing each row")
        
    for row in postgresql_date:
        Identificationnumber = row['ID']
        email = row['email']
        
           
    db.commit() 


except Exception as error:
    print(print("Failed to read data from table", error))
finally:
    if date is not None: 
        date.close()
    if db is not None:
        db.close()
        print("The Sqlite connection is closed")


    
    




