# @Processor : WebCrawler Engine
# @Author    : HAK

import requests

# Starting point of the web crawler
def startWebCrawler():
    url = 'http://stackoverflow.com/'
    page_content = getPageContent(url)
    savePageContentInRepo(page_content)

# Get all information from a web page
def getPageContent(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    return plain_text

# Save all source code to Repo
def savePageContentInRepo(page_content):
    file = open("Repo/1.html", "w")
    file.writelines(page_content)
    file.close()

startWebCrawler()