from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url = "https://en.m.wikipedia.org/wiki/List_of_American_comedy_films"
from time import sleep
ourUrl = urlopen(url).read()

soup = BeautifulSoup(ourUrl,features="html.parser")
title = soup.title.text
print(title,"***")
body = soup.find("body",{"class":"mediawiki"})
# print(body)
outfile = open('wiki.txt','w')
outfile.write(body.text)

# link = soup.find('a')
links = [a for a in soup.find_all('a',attrs={'href':re.compile("^/wiki/")})]
# print(links)
for i in links:
    print(i)
