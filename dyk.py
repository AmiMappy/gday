import wikipedia
import os
from bs4 import BeautifulSoup
import sys, os

pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)

mpsrc = "https://en.wikipedia.org/wiki/Main_Page"
os.system("touch " + fullpath + "/wmpsrc.html")
os.system("wget " + mpsrc + " -O "+ fullpath + "/wmpsrc.html > /dev/null 2>&1")
file = open(fullpath + "/wmpsrc.html", "r")

soup = BeautifulSoup(file.read(), "html.parser")
div = soup.find_all(id="mp-dyk")

print("--------DID YOU KNOW?--------\n\n")

for li_tag in div[0].find_all('li'):
    if li_tag.text != "Archive" and li_tag.text != "Start a new article" and li_tag.text != "Nominate an article":
        print(li_tag.text)
