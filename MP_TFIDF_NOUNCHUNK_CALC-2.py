from __future__ import division
from __future__ import print_function
from alchemyapi import AlchemyAPI
from pathlib import Path
import json
import time
import nltk
from nltk import ngrams
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt    import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import math
import operator
from operator import itemgetter
import spacy
from spacy import *
from spacy.en import English
from spacy.en import language_data
from spacy.en import tokenizer_exceptions
from spacy.en.language_data import update_exc, strings_to_exc
from spacy.en.language_data import TOKENIZER_EXCEPTIONS, ORTH
from spacy import symbols
from spacy.symbols import *
#import PyPDF2
#import docx
# import readDocx
import readPDF
import readHTML1
import readHTML2
# from tkFont import BOLD
import punktTokenizer
import preprocessor
from SVOExtracter import findSVOs, getAllSubs, getAllObjs, isNegated
import os
import multiprocessing
from multiprocessing import Process, current_process, Pool
import os.path
import itertools
from scipy.special.basic import hyp0f1
import imp
import numpy
from cytoolz import itertoolz
from collections import Counter
from collections import defaultdict
import textacy 
from textacy import *
import spacy_utils_jree
import constants_jree
import extract_jree
import ftfy
import readWEBSITE
import JjreeTFIDF
import JjreeTFIDFNgram
import DFReader 
from spacy.lemmatizer import lemmatize
#import getpatent



def DFCALCforward(word, DFCOUNT):
    '''
    DFCOUNT = [0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0]
    '''
    word = word.lower()
    
    csvfile = open('1976.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[0] = DFCOUNT[0] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1977.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[1] = DFCOUNT[1] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1978.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[2] = DFCOUNT[2] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1979.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[3] = DFCOUNT[3] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1980.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[4] = DFCOUNT[4] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1981.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[5] = DFCOUNT[5] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1982.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[6] = DFCOUNT[6] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1983.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[7] = DFCOUNT[7] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1984.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[8] = DFCOUNT[8] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1985.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[9] = DFCOUNT[9] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    
    csvfile = open('1996.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[20] = DFCOUNT[20] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    

def DFCALCbackward(word, DFCOUNT):

    
    csvfile = open('2006.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[30] = DFCOUNT[30] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2007.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[31] = DFCOUNT[31] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2008.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[32] = DFCOUNT[32] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2009.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[33] = DFCOUNT[33] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2010.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[34] = DFCOUNT[34] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2011.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[35] = DFCOUNT[35] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2012.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[36] = DFCOUNT[36] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2013.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[37] = DFCOUNT[37] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2014.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[38] = DFCOUNT[38] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2015.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[39] = DFCOUNT[39] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2016.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[40] = DFCOUNT[40] + 1
                break
    #print(DFCOUNT)
    csvfile.close() 
    
def DFCALC3(word, DFCOUNT):
    csvfile = open('1986.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[10] = DFCOUNT[10] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1987.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[11] = DFCOUNT[11] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1988.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[12] = DFCOUNT[12] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1989.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[13] = DFCOUNT[13] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1990.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[14] = DFCOUNT[14] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1991.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[15] = DFCOUNT[15] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1992.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[16] = DFCOUNT[16] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1993.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[17] = DFCOUNT[17] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1994.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[18] = DFCOUNT[18] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1995.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[19] = DFCOUNT[19] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    
def DFCALC4(word, DFCOUNT):
    csvfile = open('1997.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[21] = DFCOUNT[21] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1998.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[22] = DFCOUNT[22] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('1999.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[23] = DFCOUNT[23] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2000.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[24] = DFCOUNT[24] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2001.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[25] = DFCOUNT[25] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2002.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[26] = DFCOUNT[26] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2003.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[27] = DFCOUNT[27] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2004.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[28] = DFCOUNT[28] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    csvfile = open('2005.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')    
    #print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[29] = DFCOUNT[29] + 1
                break
    #print(DFCOUNT)
    csvfile.close()
    
    
'''
def TFIDFCALC(year):
    
    
    i=0
    numOfDocsWithWord = 0
    
    numDoc = numDocWithVocabAscending
    numDoc = list(numDoc)
    for w in numDoc:
        #print(w)
        
        if w[0].decode('utf-8') == word:
            numOfDocsWithWord = numDoc[i][1]
            #print("word found: " + word + "      and w[0]: " + w[0].decode('utf-8'))
            #print("URLNUM: " + str(urlNum))
            #print("num Docs with Word: " + str(numOfDocsWithWord))
            #print(math.log(urlNum / (1+numOfDocsWithWord)))
            continue
        i+=1
    
    return math.log(urlNum / (1+ numOfDocsWithWord))

    print()
'''

if __name__ == "__main__":
    nlp = English()
    csvfile = open('(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS TF words only.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    i=0
    errorCount = 0
    
    store_chunks_str_FullParent = []
    
    csvfile_ouput_by_year = open('(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS DF.csv', 'w+')
    writer_yearoutput = csv.writer(csvfile_ouput_by_year, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    
    year = 1976
    patentNum = 1
    for patNum in reader:
        print(patentNum)  
        patWords = []
        outputText = []    
        for word in patNum:
            word = word.lstrip(' ')
            patWords.append(word)
        
        #print(patWords)
        for word in patWords:
            
            DFCOUNT = multiprocessing.Array('i',41)
            print(word)
            p1 = multiprocessing.Process(target = DFCALCforward, args = (word,DFCOUNT)) 
            p2 = multiprocessing.Process(target = DFCALCbackward, args = (word,DFCOUNT))
            p3 = multiprocessing.Process(target = DFCALC3, args = (word,DFCOUNT))
            p4 = multiprocessing.Process(target = DFCALC4, args = (word,DFCOUNT))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p1.join()
            p2.join()
            p3.join()
            p4.join()
            
            #print(word)
            #print(DFCOUNT[:])
            DFCOUNTtext = str(DFCOUNT[:])
            output = ",".join([str(word), str(DFCOUNTtext)])
            #print(output)
            outputText.append(output)
        
        outputText = str(outputText)
        #print(outputText)
        writer_yearoutput.writerow(outputText.split(","))
        patentNum +=1
    csvfile.close()
           
    '''    
    while i < PATCOUNT_ORIGIN[year % 1976]:
        i += 1
        url = ''.join(['https://patents.google.com/patent/', PATNUM[i - 1], '/en'])

        print("\nURL NUMBER : " + str(i) + " = " + url)

        urlText, backCitation, pubDate = readWEBSITE.getText(url)

        if urlText is None:
            errorCount += 1
            i=-1
            continue

        doc = nlp(urlText.decode('utf-8'))
        chunks_store = []
        store_chunks_str_singlePatent = []

        for word in doc.noun_chunks:
            chunks_store.append(word)
    '''
    '''
    p = Pool(2)
    year = 1989
    nextyear = 1990
    results = p.map_async(TFIDFCALC, range(1989,1990))
    '''




print("END OF PROGRAM")