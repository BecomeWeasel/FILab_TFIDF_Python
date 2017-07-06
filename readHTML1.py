import urllib
from bs4 import BeautifulSoup
import punktTokenizer

def getText(file):
    
    text = ""
    soup = BeautifulSoup(open(file), 'html.parser')
    
    '''
    url = 'US7071258 - Graphene.html'
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    '''
    '''
    #Find by INCLUSION
    for importantText in soup.find_all("div", "patent-section-header"):
        importantText = importantText.get_text()
        
    text = importantText
    '''
    
    
    #Find by DELETION
    for title in soup.find_all("title"):
        title.decompose()
        
    for heading in soup.find_all("heading"):
        heading.decompose()
    
    for sectionName in soup.find_all("div", "patent-section-header"):
        sectionName.decompose()
        
    #for tableNum in soup.find_all("td", string = '1', limit=1):
    #    tableNum.decompose()
    
    for citation in soup.find_all("div", class_="patent-section patent-tabular-section"):
        citation.decompose() #removing citation information
    
    for citation2 in soup.find_all("a", {"id":"backward-citations"}):
        citation2.decompose()
    
    for citation3 in soup.find_all("table", class_="patent-data-table"):
        citation3.decompose()
        
    for citation4 in soup.find_all('span', {'class': 'patent-bibdata-value'}):
        citation4.decompose()
    
    for nobr in soup.find_all("nobr"):
        nobr.decompose()     #removing links at the bottom of Google patents
    
    for IFI in soup.find('span', text = 'Data provided by IFI CLAIMS Patent Services'):
        IFI.extract()           #removing txt: "Data provided by IFI Claims patent services"
    
    for rotate in soup.find_all("div", "modal-dialog"):
        rotate.decompose()        #removing txt: "Rotate"
        
    for originalImage in soup.find_all("a", "patent-lightbox-fullsize-link"):
        originalImage.decompose() #removing txt: "Original Image"
        
    for dash in soup.find_all("div", "footer-table"):
        dash.decompose()          #removing txt: "-" that was in btwn menu options
   
    for activityLink in soup.find_all("span", "activity-link"):
        activityLink.decompose()  #removing activity link: "Contribute better translation" in Google patents
    
    for menu in soup.find_all("span", "gb_4"):
        menu.decompose()
    
    for menu1 in soup.find_all("span", "gb_lb gb_ga"):
        menu1.decompose()
        
    for menu2 in soup.find_all("span", "gb_tb"):
        menu2.decompose()   
    
    for menu3 in soup.find_all("div", "gb_qb"):
        menu3.decompose()  
    
    for menu4 in soup.find_all("span", "gb_vb"):
        menu4.decompose()  
    
    for menu5 in soup.find_all("div", "gb_nb"):
        menu5.decompose()  
        
    for menu6 in soup.find_all("div", "gb_ub"):
        menu6.decompose() 
    
    for menu7 in soup.find_all("div", "gb_jb"):
        menu7.decompose() 
    
    for menu8 in soup.find_all("legend", "gbxx"):
        menu8.decompose() 
    
    for menu9 in soup.find_all("li", "gbe gbmtc"):
        menu9.decompose() 
        
    for menu10 in soup.find_all("a", "gb_ka gb_Pe"):
        menu10.decompose()
        
    for menu11 in soup.find_all("a", "gb_la gb_Ke"):
        menu11.decompose()
    
    for menu12 in soup.find_all("a", "gb_Fa gb_Ne gb_Ue gb_wb"):
        menu12.decompose()
    
    for menu13 in soup.find_all("div", "kd-appbar"):
        menu13.decompose()
    
    for menu14 in soup.find_all("td", class_="patent-data-table-td"):
        menu14.decompose()
    
    if soup.find("div", class_='patent-section-footer'):
        for menu15 in soup.find_all("div", class_="patent-section-footer"):
            menu15.decompose()
        
    if soup.find("div", id = "footer_table"):
        for menu16 in soup.find_all("div", id = "footer_table"):
            menu16.decompose()
            
    for url in soup.find_all('span', itemprop='url'):
        url.decompose()
        
    for shortcut in soup.find_all("div", "gb_xa"):
        shortcut.decompose()
    
    for patentMainTitle in soup.find_all('span', 'main-title'):
        patentMainTitle.decompose()     #removing patent title of "abstract ..." text
    
    for userName in soup.find_all("div", "gb_nf gb_R gb_Cf gb_uf"):
        userName.decompose()              #removing user name text
    
    for patentDescription in soup.find_all('span', itemprop='description'):
        patentDescription.decompose()     #removing patent description of "abstract ..." text
    
    if soup.find('div', id='intl_patents_v'):
        for intlPatent in soup.find('div', id='intl_patents_v'):
            intlPatent.decompose()    #removing international patent search text
    
    if soup.find_all('div', 'description-line-number'):
        for lineNum in soup.find_all("div", "description-line-number"):
            lineNum.decompose()
    
    for bibData in soup.find_all("table", "patent-bibdata"):
        bibData.decompose()
        
    for bibData1 in soup.find_all("span", class_="patent-bibdata-value"):
        bibData1.decompose()
        
    for button in soup.find_all("div", "viewport-chrome-toolbar viewport-chrome-toolbar-horizontal"):
        button.decompose()        #removing chrome toolbar buttons in Google Patents
            
    for titleGray in soup.find_all("h1", "title gray"):
        titleGray.decompose()     #removing title gray: "Original Text" in Google patents
        
    
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out
    
    # get text
    text = soup.get_text()
    text = text.replace('a).', 'a)')
    text = text.replace('b).', 'b)')
    text = text.replace('c).', 'c)')
    text = text.replace('d).', 'd)')
    text = text.replace('e).', 'e)')                    
                        
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    #text = '\n'.join(chunk for chunk in chunks if chunk)
    
    #tokenize text
    #text = punktTokenizer.tokenize(text)
    
    return text.encode('utf-8')
    #return text