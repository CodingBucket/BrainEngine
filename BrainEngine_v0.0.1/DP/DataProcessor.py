# DataProcessor Engine
import DP.RemoveWords as RemoveWords

from bs4 import BeautifulSoup
import pymysql
import sys

''' DataBase Variables '''
db_host = 'localhost'
db_username = 'root'
db_pass = ''
db_name = 'be_1'

''' @Task: Start point of DataProcessor '''
def startDataProcessor():

   link_id = 1

   page_link = 'http://stackoverflow.com'

   page_content = getPageContentFromRepo()

   #content_links = getLinksFromPageContent(page_link,page_content)

   #content_links = cleanLinks(page_link,content_links)

   #saveContentLinksInDb(link_id,content_links)

   page_content = processPageContent(page_link,page_content)

   #savePageContent(page_link,page_content)

   savePageDocContent(page_link,page_content)

''' @Task: Get all page content from the Repo '''
def getPageContentFromRepo():
  fr = open('1.html', 'r')
  page_content = fr.read()
  fr.close()
  return page_content

''' @Task: Get all links from page content '''
def getLinksFromPageContent(page_link,page_content):
  soup = BeautifulSoup(page_content, "html.parser")
  links = []
  for link in soup.findAll('a'):
      link = str(link.get('href'))
      links.append(link) #if url not in link:
  return links

''' @Task: Clean content links '''
def cleanLinks(url,content_links):
  links = []
  for link in content_links:
      if link is '#':
          content_links.remove(link)    # Remove all #
      if '//' not in link:
          links.append(url + link)      # IF link does not has // then add main url

  return links

''' @Task: Save page content links in links table '''
def saveContentLinksInDb(link_id,content_links):

   db = pymysql.connect(db_host, db_username, db_pass, db_name)  # Start Db connection

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

''' @Task: Return all text from the page content '''
def processPageContent(page_link, page_html):

    page_content = {}

    page_html_soup = createBeautifulSoupObject(page_html)

    soup = removeAllScriptsFromPageContent(page_html_soup)

    page_content['page_title'] = getPageTitle(soup)  # Get page title from the page title.

    text = soup.get_text()  # get all text

    lines = (line.strip() for line in text.splitlines())  # break into lines and remove leading and trailing space on each

    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))  # break multi-headlines into a line each

    all_text = '\n'.join(chunk for chunk in chunks if chunk)   # drop blank lines

    all_text = all_text.lower()  # Make all string lowercase

    all_text = all_text.split(' ')  # Make array from page content string

    remove_word = RemoveWords.getRemoveWord()  # Get all words that need to remove

    only_str = []

    for d in all_text:                        # Iterate all doc.
        if len(d) > 1:                        # IF doc length is greater than 1
            if d.isalnum() is True:           # IF doc is alfanumeric.
                if d.isdigit() is not True:   # IF doc is not a number.
                    if d not in remove_word:  # IF doc is not a removed word.
                        only_str.append(d)    # Then make the clean doc array.

    page_content['page_full_content'] = only_str
    return page_content
    #print ("\n".join(only_str))

''' @Task: Return page title From page html soup obj and Return page title. '''
def getPageTitle(soup):
    page_title = soup.title.string
    return page_title

''' @Task: Create BeautifulSoup object From page content and Return BeautifulSoup object. '''
def createBeautifulSoupObject(page_html):
    page_html_soup = BeautifulSoup(page_html,"html.parser") # create a new bs4 object from the html data loaded
    return page_html_soup

''' @Task: Remove all style and scripts From page content and Return it. '''
def removeAllScriptsFromPageContent(page_html_soup):
    for script in page_html_soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    return page_html_soup

''' @Task: Save page content in pages Table. '''
def savePageContent(page_link,page_content):

    page_title = page_content['page_title']
    page_full_content = ':'.join(page_content['page_full_content'])
    db = pymysql.connect(db_host, db_username, db_pass, db_name)  # Start Db connection

    cursor = db.cursor()
    sql = " INSERT INTO pages(page_link, page_title, page_full_content) \
            VALUES ('%s','%s','%s')" % \
            (page_link,page_title,page_full_content)
    try:
        cursor.execute(sql)  # Execute the SQL command
        db.commit()          # Commit your changes in the database
    except:
        db.rollback()        # Rollback in case there is any error

    db.close()               # Close Db connection

''' @Task: Save page doc in the page_docs Table '''
def savePageDocContent(page_link,page_content):

    #print ("\n".join(page_content['page_full_content']))

    page_full_content = page_content['page_full_content']
    for page_doc in page_full_content:
        if page_doc:                       # IF page_doc is not empty
            getPageDoc(page_doc)           # Get page_doc form the page_docs table

    db = pymysql.connect(db_host, db_username, db_pass, db_name)  # Start Db connection

    cursor = db.cursor()
    sql = " INSERT INTO pages(page_link) \
                VALUES ('%s')" % \
          (page_link)
    try:
        cursor.execute(sql)  # Execute the SQL command
        db.commit()  # Commit your changes in the database
    except:
        db.rollback()  # Rollback in case there is any error

    db.close()  # Close Db connection

def getPageDoc(page_doc):
    db = pymysql.connect(db_host, db_username, db_pass, db_name)  # Start Db connection

    cursor = db.cursor()
    sql = " INSERT INTO pages(page_link) \
                    VALUES ('%s')" % \
          (page_link)
    try:
        cursor.execute(sql)  # Execute the SQL command
        db.commit()  # Commit your changes in the database
    except:
        db.rollback()  # Rollback in case there is any error

    db.close()  # Close Db connection


startDataProcessor()


