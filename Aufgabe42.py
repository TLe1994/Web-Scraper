# imports
from bs4 import BeautifulSoup
import requests
import nltk


def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj
#über die Seiten mit der Auflistung der Titel iterieren    
for page in range(1,5,1): 
    url = "https://www.heise.de/thema/https?seite=" + str(page)  
    #zu der Liste der Titeln navigieren      
    soup = getPage(url).find(class_="keywordliste")
    soup=soup.find('nav')
    soup=soup.find_all('header')
    titel=''
    #Titeln aus den Headern extrahieren 
    for i in soup:
        titel=titel+(i.text)
#Text in Wörter/Punktationszeichen trennen
tokenit = nltk.tokenize.WordPunctTokenizer().tokenize(titel)
#Häufigkeit jedes Wortes/Punktationszeichen ermitteln. Nur die häufigsten werden angezeigt
count=dict(nltk.FreqDist(tokenit).most_common(4))
#Punktationszeichen löschen
if '-' in count:
    del count['-']
print('Top-3 Wörter sind:')
print(count)



