import feedparser
from bs4 import BeautifulSoup
import os

toi = feedparser.parse("https://timesofindia.indiatimes.com/rssfeeds/66949542.cms")

print("----------TIMES OF INDIA----------")
print("\n")

count = 1

for entry in toi.entries:
    text = BeautifulSoup(entry.summary, features="lxml")
    print(entry.title + "\n------------------------------------------------------------------------------------------------------------------------------------------------")
    print(text.text)
    print("More info at")
    print(entry.link)
    print("\n\n")
    count = count + 1
