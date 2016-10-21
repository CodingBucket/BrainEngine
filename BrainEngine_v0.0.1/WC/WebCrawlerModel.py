# @Model   : WebCrawlerModel
# @Author  : hak
# @Created : 10.19.2016

import DB.Model as Model

# Get links
def getLinks(search_query):
    sql = " SELECT page_id, page_link, page_title FROM pages WHERE page_title LIKE '%s' " % ("%"+search_query+"%")
    query_type = 'select'
    result = Model.db_query(sql,query_type)
    return result


