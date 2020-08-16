import feedparser
from bs4 import BeautifulSoup
import os

et = feedparser.parse("https://economictimes.indiatimes.com/rssfeedstopstories.cms")

print("----------ECONOMIC TIMES----------")
print("\n")

for entry in et.entries:
    print(entry.title + "\n------------------------------------------------------------------------------------------------------------------------------------------------")
    text = BeautifulSoup(entry.summary, features="lxml")    
    print(text.text + "\n")
    print("More info at\n")
    print(entry.link)
    print("\n\n")
