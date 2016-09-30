# DataProcessor Engine
import DP.RemoveWords as RemoveWords

from bs4 import BeautifulSoup
import pymysql
import sys


# Start point of DataProcessor
def startDataProcessor():

    link_id = 1

    url = 'http://stackoverflow.com'

    page_content = getPageContentFromRepo()

    #content_links = getLinksFromPageContent(url,page_content)

    #content_links = cleanLinks(url,content_links)

    #saveContentLinksInDb(link_id,content_links)

    all_text = processPageContent(page_content)

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
        links.append(link) #if url not in link:
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

# Return all text from the page content
def processPageContent(html):

    soup = BeautifulSoup(html,"html.parser") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()

    # get all text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # drop blank lines
    all_text = '\n'.join(chunk for chunk in chunks if chunk)

    # Make all string lowercase
    all_text = all_text.lower()

    # Replace all \n with space
    all_text = all_text.replace('\n', ' ')

    # Replace all dot
    all_text = all_text.replace('.', '')

    # Make array from page content string
    all_text = all_text.split(' ')

    # Get all words that need to remove
    remove_word = RemoveWords.getRemoveWord()

    only_str = []

    for d in all_text:                        # Iterate all doc.
        if len(d) > 1:                        # IF doc length is greater than 1
            if d.isalnum() is True:           # IF doc is alfanumeric.
                if d.isdigit() is not True:   # IF doc is not a number.
                    if d not in remove_word:  # IF doc is not a removed word.
                        only_str.append(d)    # Then make the clean doc array.


    #print(all_text1)
    print ("\n".join(only_str))





startDataProcessor()


