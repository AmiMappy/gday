import feedparser
from bs4 import BeautifulSoup
import os

linux_today = feedparser.parse("https://feeds.feedburner.com/linuxtoday/linux")

print("----------LINUX TODAY----------")
print("\n")

for entry in linux_today.entries:
    print(entry.title + "\n------------------------------------------------------------------------------------------------------------------------------------------------")
    text = BeautifulSoup(entry.summary, features="lxml")    
    print(text.text)
    print(entry.link)
    print("\n\n")

