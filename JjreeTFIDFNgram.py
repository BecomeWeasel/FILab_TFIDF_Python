from __future__ import division
import math

def idf(urlNum, word, numDocWithVocabAscending):
    i=0
    numOfDocsWithWord = 0
    
    numDoc = numDocWithVocabAscending
    numDoc = list(numDoc)
    for w in numDoc:
        #print(w)
        
        if w[0] == word:
            numOfDocsWithWord = numDoc[i][1]
            #print("word found: " + word + "      and w[0]: " + w[0].decode('utf-8'))
            #print("URLNUM: " + str(urlNum))
            #print("num Docs with Word: " + str(numOfDocsWithWord))
            #print(math.log(urlNum / (1+numOfDocsWithWord)))
            continue
        i+=1
    
    return math.log(urlNum / (1+ numOfDocsWithWord))