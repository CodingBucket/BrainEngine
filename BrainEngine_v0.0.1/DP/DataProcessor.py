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
        links.append(url + str(link.get('href')))
    return links

# Save page content links in links table
def saveContentLinksInDb(link_id,content_links):

    print(content_links)
    sys.exit()

    db = pymysql.connect("localhost", "root", "", "test")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME CHAR(20) NOT NULL,
             LAST_NAME CHAR(20),
             AGE INT,
              SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)

    # disconnect from server
    db.close()

startDataProcessor()


