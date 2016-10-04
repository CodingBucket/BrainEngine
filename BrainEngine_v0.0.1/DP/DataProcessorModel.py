# DataProcessorModel

import pymysql

''' DataBase Variables '''
db_host = 'localhost'
db_username = 'root'
db_pass = ''
db_name = 'be_1'

def db_query(sql):
    db = pymysql.connect(db_host, db_username, db_pass, db_name)  # Start Db connection
    cursor = db.cursor()
    try:
        cursor.execute(sql)   # Execute the SQL command
        db.commit()           # Commit your changes in the database
    except:
        db.rollback()         # Rollback in case there is any error

    db.close()                # Close Db connection