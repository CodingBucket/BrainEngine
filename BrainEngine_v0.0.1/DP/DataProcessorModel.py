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
        else:                                  # IF query_type is not select.
            db.commit()                        # Commit your changes in the database.
    except:
        print("Error: error in query execution")
        db.rollback()                          # Rollback in case there is any error.

    db.close()                                 # Close Db connection.

    if query_type is 'select':
        return results

# Get page doc from page_docs Table
def getPageDoc(page_doc):
    sql = " SELECT * FROM page_docs \
            WHERE doc_index = '%s' " % (page_doc)
    query_type = 'select'
    result = db_query(sql,query_type)
    return result

def insertPageDocIndex(page_doc,doc_page_ids):
    sql = "INSERT INTO page_docs(doc_index,page_doc_count) \
           VALUES ('%s','%s')" % \
           (page_doc,doc_page_ids)
    query_type = 'insert'
    result = db_query(sql,query_type)
    return result


