# DataProcessor Engine
from bs4 import BeautifulSoup
import pymysql
import sys

# Start point of DataProcessor
def startDataProcessor():

    link_id = 1

    url = 'http://stackoverflow.com'

    page_content = getPageContentFromRepo()

    content_links = getLinksFromPageContent(url,page_content)

    content_links = cleanLinks(url,content_links)

    saveContentLinksInDb(link_id,content_links)

# Get all page content from the Repo
def getPageContentFromRepo():
    fr = open('1.html', 'r')
    page_content = fr.read()
    fr.close()
    return page_content

# Get all links from page content
def getLinksFromPageContent(url,page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    links = []
    for link in soup.findAll('a'):
        link = str(link.get('href'))
        #if url not in link:
        links.append(link)
    return links

# Clean content links
def cleanLinks(url,content_links):
    links = []
    for link in content_links:
        if link is '#':
            content_links.remove(link)    # Remove all #
        if '//' not in link:
            links.append(url + link)      # IF link does not has // then add main url

    return links

# Save page content links in links table
def saveContentLinksInDb(link_id,content_links):

    #sys.exit()
    db = pymysql.connect("localhost", "root", "", "be_1")  # Start Db connection

    for link in content_links:
        cursor = db.cursor()
        sql = " INSERT INTO links(link) \
                VALUES ('%s')" % \
                (link)
        try:
            cursor.execute(sql)   # Execute the SQL command
            db.commit()           # Commit your changes in the database
        except:
            db.rollback()         # Rollback in case there is any error

    db.close()                    # Close Db connection

startDataProcessor()


