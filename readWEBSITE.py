import urllib.request
from bs4 import BeautifulSoup
import punktTokenizer
from string import *
import re
import itertools
import requests

def getText(file):
    
    text = ""
    backCitation = []
    pubDate = ""
    abs = ""
    clm = ""
    desc = ""
    try :
        url = urllib.request.urlopen(file).read()
    except urllib.error.HTTPError as e:
        print("HTTP404 ERROR")
        return None,None,None

    soup = BeautifulSoup(url, "lxml")
    
     #Find by INCLUSION
    for table in soup.find_all("tr", class_= "description-tr"):
        table.decompose()
    
    for date in soup.find_all("dd"):    
        for publicationDate in date.find_all("time", itemprop="publicationDate"):
            pubDate = publicationDate.get_text()
            pubDate = pubDate[:4]
    
    for abstract in soup.find_all("div", class_= "abstract"):
        abs = abstract.get_text()
    '''  
    for claim in soup.find_all("section", itemprop="claims"):
        clm = claim.get_text()    
    '''
    for descriptionLineNum in soup.find_all("div", class_="description-line-number"):
        descriptionLineNum.decompose()    
    
    for description in soup.find_all("section", itemprop = "description"):    
    #for description in soup.find_all("div", class_ = "description"):
        desc = description.get_text()
    
    if desc == "":
        for description in soup.find_all("div", class_ = "description-line"):
            desc = description.get_text()
    
    if desc == "":
        for description in soup.find_all("section", itemprop = "description"):
            desc = description.get_text()
    
    for citation in soup.find_all("tr", itemprop = "backwardReferences"):
        for backwardCitation in citation("span", itemprop = "publicationNumber"):
            bwdCit = backwardCitation.get_text()
            backCitation.append(bwdCit.encode('utf-8'))
        #<span itemprop="publicationNumber">US9034421B2</span>
    
    for headings in soup.find_all("heading"):
        headings.decompose()
        
    for tables in soup.find_all("table"):
        tables.decompose()
    
    
    text = "\n".join([abs, clm, desc])
    
    
    
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out
    
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    
    #if text == "" and backCitation == "" and pubDate == "":
        
    
    
    return text.encode('utf-8'), backCitation, pubDate
    
    