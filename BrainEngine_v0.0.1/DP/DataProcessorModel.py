# DataProcessorModel

import pymysql
import sys

''' DataBase Variables '''
db_host = 'localhost'
db_username = 'root'
db_pass = ''
db_name = 'be_1'

# Execute query in database
def db_query(sql, query_type):
    results = 0
    db = pymysql.connect(db_host, db_username, db_pass, db_name)  # Start Db connection
    cursor = db.cursor()
    try:
        cursor.execute(sql)                    # Execute the SQL command.

        if query_type is 'select':             # IF query_type is select Then get all data.
            results = cursor.fetchall()        # Fetch all the rows in a list of lists.
            print(sql)
            print(results)
            sys.exit()
        else:                                  # IF query_type is not select.
            db.commit()                        # Commit your changes in the database.
    except:
        db.rollback()                          # Rollback in case there is any error.

    db.close()                                 # Close Db connection.

    if query_type is 'select':
        return results

# Get page doc from page_docs Table
def getPageDoc(page_doc):
    page_doc = 'hasan'
    sql = " SELECT * FROM page_docs \
            WHERE page_doc == '%s' " % (page_doc)
    query_type = 'select'
    print(sql)
    sys.exit()
    db_query(sql,query_type)


