# @Model   : Model
# @Author  : hak
# @Created : 10.19.2016

import pymysql

import DB.db_config as DB_Config

# Execute query in database
def db_query(sql, query_type):

    db_config = DB_Config.getDbConfig()

    results = 0
    db = pymysql.connect(db_config['host'], db_config['username'], db_config['password'], db_config['db_name'])  # Start Db connection
    cursor = db.cursor()
    try:
        cursor.execute(sql)                    # Execute the SQL command.
        if query_type is 'select':             # IF query_type is select Then get all data.
            results = cursor.fetchall()        # Fetch all the rows in a list of lists.
        else:                                  # IF query_type is not select.
            db.commit()                        # Commit your changes in the database.
    except:
        print("Error: error in query execution")
        db.rollback()                          # Rollback in case there is any error.

    db.close()                                 # Close Db connection.

    if query_type is 'select':
        return results
