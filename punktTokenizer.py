import nltk
from nltk.tokenize.punkt    import PunktSentenceTokenizer, PunktParameters
#from _mysql import NULL


#sentence_splitter = PunktSentenceTokenizer(punkt_param)
#text = "is THAT what you mean, Mrs. Hussey?"
#sentences = sentence_splitter.tokenize(text)
#

outputList1 = open('outputList1.txt', 'w') 
outputList2 = open('outputList2.txt', 'w') 
outputList3 = open('outputList3.txt', 'w') 
outputList4 = open('outputList4.txt', 'w') 
outputList5 = open('outputList5.txt', 'w') 
outputList6 = open('outputList6.txt', 'w') 
outputList7 = open('outputList7.txt', 'w') 
outputList8 = open('outputList8.txt', 'w') 
outputList9 = open('outputList9.txt', 'w') 
outputList10 = open('outputList10.txt', 'w') 
outputList11 = open('outputList11.txt', 'w') 
outputList12 = open('outputList12.txt', 'w') 
outputList13 = open('outputList13.txt', 'w') 
outputList14 = open('outputList14.txt', 'w') 
outputList15 = open('outputList15.txt', 'w') 
outputList16 = open('outputList16.txt', 'w') 
outputList17 = open('outputList17.txt', 'w') 
outputList18 = open('outputList18.txt', 'w') 
outputList19 = open('outputList19.txt', 'w') 
outputList20 = open('outputList20.txt', 'w') 
outputList21 = open('outputList21.txt', 'w') 
outputList22 = open('outputList22.txt', 'w') 
outputList23 = open('outputList23.txt', 'w') 
outputList24 = open('outputList24.txt', 'w') 
outputList25 = open('outputList25.txt', 'w') 

extra_abbreviations = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e']
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentence_tokenizer._params.abbrev_types.update(extra_abbreviations)

def tokenize(fileName):
    extra_abbreviations = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'e.g', 'pp', 'lett', 'phys','fig', 'vol', 'appl', 'al', 'etc','i.e']
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sent_detector._params.abbrev_types.update(extra_abbreviations)
    
    
    '''
    sentences = [] 
    for paragraph in fileName.split('\n'): 
        sentences.extend(punkt.tokenize(paragraph)) 
    '''
    
    textList = []
    #textList = sent_detector.tokenize(fileName.strip())
    for paragraph in fileName.split('\n'):
        
        textList.extend(sent_detector.tokenize(paragraph))
    '''
    numOfFilesNeeded = (len(textList)/100)+1
    if numOfFilesNeeded == 1:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
    if numOfFilesNeeded == 2:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
        
        textList2 = textList[100:200]
        outputList2.write(" \n".join(textList2).encode('utf-8'))
        
    if numOfFilesNeeded == 3:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
        
        textList2 = textList[100:200]
        outputList2.write(" \n".join(textList2).encode('utf-8'))
        
        textList3 = textList[200:300]
        outputList3.write(" \n".join(textList3).encode('utf-8'))
        
    if numOfFilesNeeded == 4:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
        
        textList2 = textList[100:200]
        outputList2.write(" \n".join(textList2).encode('utf-8'))
        
        textList3 = textList[200:300]
        outputList3.write(" \n".join(textList3).encode('utf-8'))
           
        textList4 = textList[300:400]  
        outputList4.write(" \n".join(textList4).encode('utf-8'))
        
    if numOfFilesNeeded == 5:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
        
        textList2 = textList[100:200]
        outputList2.write(" \n".join(textList2).encode('utf-8'))
        
        textList3 = textList[200:300] 
        outputList3.write(" \n".join(textList3).encode('utf-8'))
          
        textList4 = textList[300:400]
        outputList4.write(" \n".join(textList4).encode('utf-8'))
        
        textList5 = textList[400:500] 
        outputList5.write(" \n".join(textList5).encode('utf-8'))
        
    if numOfFilesNeeded == 6:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
        
        textList2 = textList[100:200]
        outputList2.write(" \n".join(textList2).encode('utf-8'))
        
        textList3 = textList[200:300] 
        outputList3.write(" \n".join(textList3).encode('utf-8'))
          
        textList4 = textList[300:400]
        outputList4.write(" \n".join(textList4).encode('utf-8'))
        
        textList5 = textList[400:500] 
        outputList5.write(" \n".join(textList5).encode('utf-8'))
        
        textList6 = textList[500:600] 
        outputList6.write(" \n".join(textList6).encode('utf-8'))
        
    if numOfFilesNeeded == 7:
        textList1 = textList[0:100]
        outputList1.write(" \n".join(textList1).encode('utf-8'))
        
        textList2 = textList[100:200]
        outputList2.write(" \n".join(textList2).encode('utf-8'))
        
        textList3 = textList[200:300] 
        outputList3.write(" \n".join(textList3).encode('utf-8'))
          
        textList4 = textList[300:400]
        outputList4.write(" \n".join(textList4).encode('utf-8'))
        
        textList5 = textList[400:500] 
        outputList5.write(" \n".join(textList5).encode('utf-8'))
        
        textList6 = textList[500:600] 
        outputList6.write(" \n".join(textList6).encode('utf-8'))
        
        textList7 = textList[600:700] 
        outputList7.write(" \n".join(textList7).encode('utf-8'))
    '''    
    #tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
    
    '''
    outputList6.write(" \n".join(textList6).encode('utf-8'))
    outputList7.write(" \n".join(textList7).encode('utf-8'))
    outputList8.write(" \n".join(textList8).encode('utf-8'))
    outputList9.write(" \n".join(textList9).encode('utf-8'))
    outputList10.write(" \n".join(textList10).encode('utf-8'))
    outputList11.write(" \n".join(textList11).encode('utf-8'))
    outputList12.write(" \n".join(textList12).encode('utf-8'))
    outputList13.write(" \n".join(textList13).encode('utf-8'))
    outputList14.write(" \n".join(textList14).encode('utf-8'))
    outputList15.write(" \n".join(textList15).encode('utf-8'))
    outputList16.write(" \n".join(textList16).encode('utf-8'))
    outputList17.write(" \n".join(textList17).encode('utf-8'))
    outputList18.write(" \n".join(textList18).encode('utf-8'))
    outputList19.write(" \n".join(textList19).encode('utf-8'))
    outputList20.write(" \n".join(textList20).encode('utf-8'))
    outputList21.write(" \n".join(textList21).encode('utf-8'))
    outputList22.write(" \n".join(textList22).encode('utf-8'))
    outputList23.write(" \n".join(textList23).encode('utf-8'))
    outputList24.write(" \n".join(textList24).encode('utf-8'))
    outputList25.write(" \n".join(textList25).encode('utf-8'))
    '''
    #tokenizedText = ' \n'.join(sent_detector.tokenize(fileName.strip()))
    
    #textList = ' \n'.join(textList)
    
    #print('\n-----\n'.join(tokenizedText.tokenize(text.strip())))
    
    #print("outputList1")
    #return .join(textList)

    #return tokenizedText
    return textList