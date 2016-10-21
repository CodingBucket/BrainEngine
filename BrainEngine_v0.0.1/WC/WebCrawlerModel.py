# @Model   : WebCrawlerModel
# @Author  : hak
# @Created : 10.19.2016

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
        else:                                  # IF query_type is not select.
            db.commit()                        # Commit your changes in the database.
    except:
        print("Error: error in query execution")
        db.rollback()                          # Rollback in case there is any error.

    db.close()                                 # Close Db connection.

    if query_type is 'select':
        return results

# Get links
def getLinks(search_query):
    sql = " SELECT page_id, page_link, page_title FROM pages WHERE page_title LIKE '%s' " % ("%"+search_query+"%")
    query_type = 'select'
    result = db_query(sql,query_type)
    return result


