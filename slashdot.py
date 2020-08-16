import feedparser
from bs4 import BeautifulSoup
import os

slashdot = feedparser.parse("http://rss.slashdot.org/Slashdot/slashdotMain")

print("----------SLASHDOT----------")
print("\n")

for entry in slashdot.entries:
    print(entry.title + "\n------------------------------------------------------------------------------------------------------------------------------------------------")
    text = BeautifulSoup(entry.summary, features="lxml")    
    print(text.text)
    print(entry.link)
    print("\n\n")

