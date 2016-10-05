import random
import urllib.request
from PyCode.tuna import Employee

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

#download_web_image("https://avatars3.githubusercontent.com/u/17844098?v=3&s=460")


emp = Employee("Zara", 2000)

def show():
    emp.displayEmployee()

show()