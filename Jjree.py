'''
Created on 1989. 3. 11.

@author: jjree
'''
# from __future__ import unicode_literals
# ! python3
from __future__ import division
from __future__ import print_function
from alchemyapi import AlchemyAPI
from pathlib import Path
import json

import time
import multiprocessing
from math import floor

import nltk
from nltk import ngrams
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import urllib
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

import PyPDF2
# import docx
# import readDocx
import readPDF
import readHTML1
import readHTML2

# from tkFont import BOLD

import tkinter as tk

import punktTokenizer
import preprocessor
from SVOExtracter import findSVOs, getAllSubs, getAllObjs, isNegated
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

# from tokenizer_exceptions import TOKENIZER_EXCEPTIONS, ORTH_ONLY

# import usr.local.lib.python2.7.dist-packages.spacy.en.language_data

# sys.path.append('/usr/local/lib/python2.7/dist-packages/spacy/en')
# from ..sys.path import language_data as base
# from ..language_data import update_exc, strings_to_exc


'''
demo_text1 = readDocx.getText('US7071258 - Graphene.docx')
demo_text1 = demo_text1.replace("the ", "")
demo_text1 = demo_text1.replace(" a ", "")
demo_text1 = demo_text1.replace("this ", "")
'''
# demo_text2 = readPDF.getPDFContent('US7071258 - Graphene.pdf')
# demo_text2 = readPDF.getPDFContent('US8871296 - Graphene 2.pdf')

# Extracting text from  WEBSITE
urlFixed = []

''' #GETTING PATENT NUMBERS FROM URLLIST.TXT FILE
urlFile = open("urlList.txt", "r+")
#urls = urlFile.readlines()
urls = urlFile.readlines()
'''

'''
#GETTING PATENT NUMBERS FROM CSV FILE
'''
'''
### GRAPHENE PATENTS
csvfile = open('(01)Graphene_5446.csv', 'r+')
savefile = open('(01)Graphene_5446_1.csv', 'w')
'''

### PHOTOLITHOGRAPHY PATENTS
# saving all text from website
# masterTxtFile = open('(02)Photolithography_6619 PatSnap MASTER TEXT FILE.csv', 'r+')
HPPListFile = open('(03)DSSC_9501 PatSnap v.02 HPP List.csv', 'r+')

'''
csvfile = open('(02)Photolithography_3623 ORIGINAL.csv', 'r+')
savefile = open('(02)Photolithography_3623_1.csv', 'w')

# error from 1578 had to restart program from 1578
csvfile = open('(02)Photolithography_3623 ORIGINAL 1578 to end.csv', 'r+')
savefile = open('(02)Photolithography_3623_2.csv', 'w')

# RUNNING NEW PATENT SET OF PHOTOLITHOGRAPHY FROM PATSNAP 96 PATENTS OF THE MAIN PATH
csvfile = open('(02)Photolithography_6619 PatSnap v.02 obtaining keywords.csv', 'r+')
savefile = open('(02)Photolithography_6619 PatSnap v.02 obtaining keywords OUTPUT.csv', 'w')

# NEW PATENT SET OF PHOTOLITHOGRAPHY FROM PATSNAP ALL PATENTS
csvfile = open('(02)Photolithography_6619 PatSnap ORIGINAL2 for keyword extraction of all patents.csv', 'r+')
savefile = open('(02)Photolithography_6619 PatSnap ORIGINAL2 for keyword extraction of all patents OUTPUT.csv', 'w')

csvfile = open('(02)Photolithography_6619 PatSnap ORIGINAL2 for keyword extraction of all patents 3112 to end.csv', 'r+')
savefile = open('(02)Photolithography_6619 PatSnap ORIGINAL2 for keyword extraction of all patents OUTPUT 3112 to end.csv', 'w')

# NEW PATENT SET OF PHOTOLITHOGRAPHY FROM PATSNAP after 2nd error/stop from 1547 of 3112 to end file
csvfile = open('(02)Photolithography_6619 PatSnap ORIGINAL2 for keyword extraction of all patents 1547 to end 2.csv', 'r+')
savefile = open('(02)Photolithography_6619 PatSnap ORIGINAL2 for keyword extraction of all patents OUTPUT 1547 to end 2.csv', 'w')
'''

# DSSC PATENT SET FROM PATSNAP DIVIDED BY YEAR
yearOfPatents = 1989
error1stCount = 0  # HTTP404 ERROR COUNT from 1st call
error2ndCount = 0  # HTTP404 ERROR COUNT from 2nd call

csvfile = open('(03)DSSC_9501 PatSnap v.02 1989 Patent for yearly keyword extraction.csv', 'r+')
csvfile_DFCalc = open('(03)DSSC_9501 PatSnap v.045 MAIN PATH PATENTS LIST FOR DF CALC.csv', 'r+')

savefile = open('(03)DSSC_9501 PatSnap v.02 1989 Patent for yearly keyword extraction OUTPUT.csv', 'w')

savefile2 = open('TF-IDF OUTPUT (1989).csv', 'w')

savefile_2gram = open('2GRAM OUTPUT (1989).csv', 'w')
savefile_3gram = open('3GRAM OUTPUT (1989).csv', 'w')
savefile_4gram = open('4GRAM OUTPUT (1989).csv', 'w')
savefile_2gram_TFIDF = open('2GRAM OUTPUT TFIDF (1989).csv', 'w')
savefile_3gram_TFIDF = open('3GRAM OUTPUT TFIDF (1989).csv', 'w')
savefile_4gram_TFIDF = open('4GRAM OUTPUT TFIDF (1989).csv', 'w')

savefile_DFList = open('DF LIST OUTPUT 1GRAM.csv', 'w')
savefile_DFList_2GRAM = open('DF LIST OUTPUT 2GRAM.csv', 'w')
savefile_DFList_3GRAM = open('DF LIST OUTPUT 3GRAM.csv', 'w')
savefile_DFList_4GRAM = open('DF LIST OUTPUT 4GRAM.csv', 'w')

savefile3 = open('TF-IDF OUTPUT ONLY.csv', 'w')
# savefile_FULLTEXT = open('FULL TEXT FROM WEBSITE.csv')

reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
reader2 = csv.reader(csvfile_DFCalc, delimiter=' ', quotechar='|')
HPPListreader = csv.reader(HPPListFile, delimiter=',', quotechar='|')

# masterwriter = csv.writer(masterTxtFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer = csv.writer(savefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer2gram = csv.writer(savefile_2gram, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer3gram = csv.writer(savefile_3gram, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer4gram = csv.writer(savefile_4gram, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer2gramTFIDF = csv.writer(savefile_2gram_TFIDF, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer3gramTFIDF = csv.writer(savefile_3gram_TFIDF, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer4gramTFIDF = csv.writer(savefile_4gram_TFIDF, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

writerDFLIST = csv.writer(savefile_DFList, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

writer2 = csv.writer(savefile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer3 = csv.writer(savefile3, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# writer4 = csv.writer(savefile_FULLTEXT, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) #no need to use

csvInput = []

urlNum = 1  # modify 'urlNum=0' into 'urlNum=1'

# SPACY ADDING EXCEPTIONS ABBREVIATION#
ORTH_ONLY = [u"etc.", u"Etc.", u"Appl.", u"Vol.", u"Phys.", u"Lett.", u"Ser.", u"pp.",
             u"et.", u"al.", u"FIG.", u"No.", u"1.", u"2.", u"3.", u"4.", u"5.", u"6.",
             u"7.", u"8.", u"9.", u"10.", u"11.", u"12.", u"13.", u"14.", u"15.", u"16.",
             u"17.", u"18.", u"19.", u"20.", u"A.", u"B.", u"D.", u"E.", u"F.",
             u"G.", u"H.", u"I.", u"J.", u"K.", u"L.", u"M.", u"N.", u"O.", u"P.", u"Q.",
             u"R.", u"S.", u"T.", u"U.", u"V.", u"W.", u"X.", u"Y.", u"Z.", u"FIG.", u"FIGS.", u"U.S.", u"Pat.",
             u"Nos.",
             u"Example 1.", u"Example 2.", u"Example 3.", u"Example 4.", u"Example 5.", u"Example 6.", u"Example 7.",
             u"Example 8.", u"Example 9.", u"Example 10.", u"Example 11.", u"Example 12.", u"Example 13.",
             u"Example 14.", u"Example 15."]

converted = strings_to_exc(ORTH_ONLY)
update_exc(TOKENIZER_EXCEPTIONS, converted)

textVocabsALL = {}
textVocabsTagsALL = {}
numDocWithVocab = {}
numDocWithVocabAscending = {}
numDocWithVocab2Gram = {}
numDocWithVocab2GramAscending = {}
numDocWithVocab3Gram = {}
numDocWithVocab3GramAscending = {}
numDocWithVocab4Gram = {}
numDocWithVocab4GramAscending = {}

fullPatentVocabDict = {}
fullPatentVocabDict2Gram = {}
fullPatentVocabDict3Gram = {}
fullPatentVocabDict4Gram = {}

nlp = English()
nlp1 = spacy.load("en")

# ADDING STOP WORDS TO SPACY NLP VOCAB
stopWordList = [u'description', u'invention', u'abstract', u'claim', u'method', u'embodiment', u'pat.', u'no.', u'of',
                u'and', u'present', u'fig.'

                ]
for stopWord in stopWordList:
    word = nlp1.vocab[stopWord]
    word.is_stop = True

# GETTING HPP WORD LIST

HPPNUM = 1
DFCOUNT = [0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0]  # DF Counter from 1989 to 2016  = 28 Values
PatCOUNT = [49, 68, 81, 85, 107,
            100, 124, 103, 96, 95,
            127, 219, 287, 263, 254,
            199, 172, 176, 179, 183,
            247, 427, 739, 961, 1106,
            1457, 1086, 430]
HPPList = []
HPPWords = {}
HPPwordList = {}
errorPatents = []

# CREATING PATENT LIST OF HPP
for patent in HPPListreader:
    HPPList.append(patent)

# print(HPPList)
# print(HPPList[1][2])
# print(HPPList[1][1])




###
tmpmatrix = []
for url in reader:
    tmpmatrix.append(url[0])
# print(tmpmatrix[0], tmpmatrix[1])

'''
# FINDING DF OF HPP'S WORDS
for HPP in reader2:
    HPPwordListTemp = []
    
    
    for word in HPP:
        HPPwordListTemp1 = []
        
        word = word.replace(",", "")
        
        HPPwordListTemp1.append(word)
        HPPwordListTemp1.append(DFCOUNT)
        HPPwordListTemp.append(HPPwordListTemp1)
        
    #print(HPPwordListTemp)
    HPPwordList[HPPNUM] = HPPwordListTemp
    HPPNUM +=1
 
for key in HPPwordList.keys():
    i=0
    for word in HPPwordList[key]:
        w = word[0]
        word[1] = DFReader.dfRead(w, key, HPPwordList)
        #print(word)
        HPPwordList[key][i] = word
        i+=1
    print(HPPwordList[key])
    HPPwordList1 = str(HPPwordList[key])
    writerDFLIST.writerow(HPPwordList1.split(","))
'''


# Performance is usually relative to execution speed.
# Separate code into two block to improve performance.
# Using multi-processing can improve execution speed.
# First one of separted part is "Get patent and calculate TF"
# function named getPatentAndCalcTF



def getPatentAndCalcTF(start,
                       end):  # TODO: if end==0, result write on 2GRAM OUTPUT("YEAR").csv else result write on 2GRAM OUTPUT("YEAR").csv
    # GETTING TEXT FROM GOOGLE PATENT WEBSITES

    ############
    ############ variable used in function : getPatentAndCalcTF and function : DFAndTFIDF
    global urlNum
    global word
    global numDocWithVocab
    global numDocWithVocabAscending
    global numDocWithVocab2Gram
    global numDocWithVocab2GramAscending
    global numDocWithVocab3Gram
    global numDocWithVocab3GramAscending
    global numDocWithVocab4Gram
    global numDocWithVocab4GramAscending

    global fullPatentVocabDict
    global fullPatentVocabDict2Gram
    global fullPatentVocabDict3Gram
    global fullPatentVocabDict4Gram

    global nlp
    global nlp1

    global error1stCount
    global error2ndCount
    ############


    starttmp = start
    urlNum = start + 1
    # for url in reader:

    for head in range(start, end + 1):
        # if urlNum == end:
        # urlNum -= 1
        # return None
        textVocabs = {}
        textVocabs_items = {}
        textVocabsAscending = {}
        textVocabsAscending1 = []
        textVocabsDeps = {}
        textVocabsTags = {}
        totalWordsInDoc = 0

        # newUrl = ''.join(['https://patents.google.com/patent/', url[0], '/en'])


        newUrl = ''.join(['https://patents.google.com/patent/', tmpmatrix[head], '/en'])

        print("\nURL NUMBER: " + str(urlNum) + " = " + newUrl)

        urlText, backCitation, pubDate = readWEBSITE.getText(newUrl)

        if urlText is None:  # TODO : FIXED @7.6 22:31 modification on 'urlText = None' to 'urlText is None'
            if start == 0:  # start 0 means function is called for 1st time and executed on P1. else P2 call function.
                error1stCount += 1  # error from 1st func call
            else:
                error2ndCount += 1  # error from 2nd func call

            continue  # HTTP404 Error check

        backCitationText = ""

        for cit in backCitation:
            backCitationTextEmpty = True
            if backCitationText == "":
                backCitationText = cit
                backCitationTextEmpty = False
                # if backCitationTextEmpty is True and backCitationText != "":
                #   backCitationText = " | ".join([backCitationText, cit])

        ### END OF URL EXTRACTION FROM CSV FILE AND WRITING BACKWARD CITATION AND PUB YEAR IN SAME CSV FILE

        ##################################################################################
        ### START FINDING KEY WORDS
        ##################################################################################
        doc = nlp(urlText.decode('utf-8'))

        # DELETING STOP WORDS FROM TEXT FOR
        document = [words for words in doc if words.is_stop == False]
        stopWordLessDoc = ""
        for word in document:
            stopWordLessDoc = stopWordLessDoc + word.text + " "
        document = stopWordLessDoc

        ##################################################################################
        #                    NGRAMS CALCULATING
        ##################################################################################


        try:
            ngramDoc = textacy.Doc(document)


        except urllib.error.HTTPError as e:
            print("RUNTIME ERROR AT THIS PATENT")
            errorPatents.append(urlNum)
            continue
        # ngramDoc = [words for words in ngramDoc if words.is_stop == False]


        # print("---Printing NGRAMS---")
        twoGrams = ngramDoc.to_bag_of_terms(ngrams=2, normalize='lemma', as_strings=True)
        threeGrams = ngramDoc.to_bag_of_terms(ngrams=3, normalize='lemma', as_strings=True)
        fourGrams = ngramDoc.to_bag_of_terms(ngrams=4, normalize='lemma', as_strings=True)

        twoGramsSorted = sorted(twoGrams.items(), key=lambda x: x[1], reverse=True)
        threeGramsSorted = sorted(threeGrams.items(), key=lambda x: x[1], reverse=True)
        fourGramsSorted = sorted(fourGrams.items(), key=lambda x: x[1], reverse=True)

        # print(twoGramsSorted)
        # print(threeGramsSorted)
        # print(fourGramsSorted)

        ###########################################################
        #                2GRAM COUNTER
        ###########################################################
        twoGramsSortedText = []
        twoGramsSortedText1 = []

        # CALCULATING TF = FREQ/TOTAL WORDS
        i = 0
        for word in twoGramsSorted:
            word = list(word)
            # print("---word[1]: " + str(word[1]))
            word[1] = float(word[1] / len(twoGramsSorted))
            # print("=== NEW word[1]: " + str(word[1]))
            word = tuple(word)
            twoGramsSorted[i] = word
            i += 1

        for word in twoGramsSorted:
            # twoGramsSortedText = []
            twoGramsSortedText = " : ".join([(word[0]), str(word[1])])
            twoGramsSortedText1.append(twoGramsSortedText)

        fullPatentVocabDict2Gram[urlNum] = twoGramsSorted
        twoGramsSortedText1 = str(twoGramsSortedText1)
        writer2gram.writerow(
            twoGramsSortedText1.split(","))  # save sequence happen here. # TODO : this line ,may, need two version.

        # CALCULATING DF OF 2GRAM TERMS
        for vocabInDoc in twoGramsSorted:
            numDocWithVocab2Gram[vocabInDoc[0]] = numDocWithVocab2Gram.get(vocabInDoc[0], 0) + 1
        numDocWithVocab2Gram_items = numDocWithVocab2Gram.items()
        numDocWithVocab2GramAscending = sorted(numDocWithVocab2Gram_items, key=lambda x: x[1] * -1)

        ###########################################################
        #                3GRAM COUNTER
        ###########################################################
        threeGramsSortedText = []
        threeGramsSortedText1 = []

        # CALCULATING TF = FREQ/TOTAL WORDS
        i = 0
        for word in threeGramsSorted:
            word = list(word)
            # print("---word[1]: " + str(word[1]))
            word[1] = float(word[1] / len(threeGramsSorted))
            # print("=== NEW word[1]: " + str(word[1]))
            word = tuple(word)
            threeGramsSorted[i] = word
            i += 1
        for word in threeGramsSorted:
            threeGramsSortedText = " : ".join([(word[0]), str(word[1])])
            threeGramsSortedText1.append(threeGramsSortedText)

        fullPatentVocabDict3Gram[urlNum] = threeGramsSorted
        threeGramsSortedText1 = str(threeGramsSortedText1)
        writer3gram.writerow(threeGramsSortedText1.split(","))

        # CALCULATING DF OF 3GRAM TERMS
        for vocabInDoc in threeGramsSorted:
            numDocWithVocab3Gram[vocabInDoc[0]] = numDocWithVocab3Gram.get(vocabInDoc[0], 0) + 1
        numDocWithVocab3Gram_items = numDocWithVocab3Gram.items()
        numDocWithVocab3GramAscending = sorted(numDocWithVocab3Gram_items, key=lambda x: x[1] * -1)

        ###########################################################
        #                    4GRAM COUNTER
        ###########################################################
        fourGramsSortedText = []
        fourGramsSortedText1 = []

        # CALCULATING TF = FREQ/TOTAL WORDS
        i = 0
        for word in fourGramsSorted:
            word = list(word)
            # print("---word[1]: " + str(word[1]))
            word[1] = float(word[1] / len(fourGramsSorted))
            # print("=== NEW word[1]: " + str(word[1]))
            word = tuple(word)
            fourGramsSorted[i] = word
            i += 1
        for word in fourGramsSorted:
            fourGramsSortedText = " : ".join([(word[0]), str(word[1])])
            fourGramsSortedText1.append(fourGramsSortedText)

        fullPatentVocabDict4Gram[urlNum] = fourGramsSorted
        fourGramsSortedText1 = str(fourGramsSortedText1)
        writer4gram.writerow(fourGramsSortedText1.split(","))

        # CALCULATING DF OF 4GRAM TERMS
        for vocabInDoc in fourGramsSorted:
            numDocWithVocab4Gram[vocabInDoc[0]] = numDocWithVocab4Gram.get(vocabInDoc[0], 0) + 1
        numDocWithVocab4Gram_items = numDocWithVocab4Gram.items()
        numDocWithVocab4GramAscending = sorted(numDocWithVocab4Gram_items, key=lambda x: x[1] * -1)

        urlNum += 1
        starttmp += 1

        '''
        ###########################################################
        # 1GRAM WORD LIST with TF / TF-IDF
        ###########################################################
        sents = []
        new_sents = []
        for sent in doc.sents:
            sents.append(sent)   
        
        i=0
        clean_token_tags_sents = []
        for sent in sents:
            i += 1
            #print("Processing sentence# %d: %s" % (i, sent))
            token_tags = []
            toks = nlp(sent.text.encode("ascii", "ignore").decode("utf-8"))
            for tok in toks:
                token_tags.append((tok.lemma_, tok.pos_, tok.dep_))
            
            clean_token_tags = []
            
            #COUNTING WORDS: TF
            for tt in token_tags:
                if tt[1] == u"SPACE":
                    continue
                clean_token_tags.append(tt)
                clean_token_tags_sents.append(tt)
                if (nlp.vocab[tt[0]].is_stop == False) and (tt[1] != u'PUNCT') and (tt[1] != u'NUM'):
                    totalWordsInDoc +=1
                    textVocabs[tt[0]] = textVocabs.get(tt[0], 0) + 1
                    textVocabsTags[tt[1]] = textVocabsTags.get(tt[1], 0) + 1
                    #LIST OF ALL VOCAB IN ALL TEXT
                    #textVocabsALL[tt[0]] = textVocabsALL.get(tt[0], 0) + 1
                    #textVocabsTagsALL[tt[1]] = textVocabsTagsALL.get(tt[1], 0) + 1
    
        
        masterInputText = ";".join([url[0], str(clean_token_tags_sents)])
        masterwriter.writerow(masterInputText.split(";"))
        
        textVocabs_items = textVocabs.items()
        textVocabs_items = list(textVocabs_items)
        
        # CALCULATING TF = FREQ/TOTAL WORDS 1GRAM
        x=0
        for items in textVocabs_items:
            items = list(items)
            items[1] = float(items[1] / totalWordsInDoc)
            items = tuple(items)
            textVocabs_items[x] = items
            x+=1
        textVocabsAscending = sorted(textVocabs_items, key= lambda x: x[1]*-1)   
        
        fullPatentVocabDict[urlNum] = textVocabsAscending
        
        #NUMBER OF DOCUMENTS WITH EACH VOCAB
        for vocabInDoc in textVocabsAscending:
            if(nlp.vocab[vocabInDoc[0]].is_stop == False) and vocabInDoc[1] != u'PUNCT':
                numDocWithVocab[vocabInDoc[0]] = numDocWithVocab.get(vocabInDoc[0], 0) + 1
        numDocWithVocab_items = numDocWithVocab.items()
        numDocWithVocabAscending = sorted(numDocWithVocab_items, key= lambda x: x[1]*-1)
    
        #print(numDocWithVocabAscending)
        
        for vocab in textVocabsAscending:   #JOINING VOCAB WITH FREQUENCY 'VOCAB: FREQ'
            textVocabsAscendingItem = ":".join([str(vocab[0]), str(vocab[1])]) #/ len(textVocabsAscending)
            textVocabsAscending1.append(textVocabsAscendingItem)
    
        
        #for vocab in textVocabsAscending1:
        textVocabsAscending2 = " | ".join(textVocabsAscending1)
        csvInputText = ",".join([url[0], backCitationText, pubDate, str(textVocabsAscending2)])
        csvInput.append(csvInputText)
        writer.writerow(csvInputText.split(","))
        urlFixed.append(newUrl)                
    
    # CALCULATING TF-IDF 1GRAM
    print("-----Calculating TF-IDF----- 1GRAM")
    i=0
    for patNum in fullPatentVocabDict:
        i+=1
        
        j=0
        for word in fullPatentVocabDict[i]:
            
            word = list(word)
            word1 = word
            
            tf = word[1]  
            wordIdf = JjreeTFIDF.idf(urlNum, word[0], numDocWithVocabAscending) 
            TF_IDF = float(tf * wordIdf)
            
            word.append(TF_IDF)
            word = tuple(word)
            
            word1[1] = TF_IDF
            word1 = tuple(word1)
            
            fullPatentVocabDict[i][j] = word1
            j+=1
    
    # SORTING 1 GRAM WORDS
    i=1
    sortedFullPatentVocabDict = fullPatentVocabDict
    for patent in sortedFullPatentVocabDict:
        sortedFullPatentVocabDict[i] = sorted(sortedFullPatentVocabDict[i], key = itemgetter(1), reverse = True)
        i+=1
    
    
    # CHANGING 1GRAM TO WORD:TF-IDF FORMAT THEN SAVING TO FILE
    k=1
    for patent in sortedFullPatentVocabDict: 
        j=0
        for word in sortedFullPatentVocabDict[k]:
            sortedFullPatentVocabDict[k][j] = " : ".join([str(sortedFullPatentVocabDict[k][j][0]), str(sortedFullPatentVocabDict[k][j][1]) ]) #, str(sortedFullPatentVocabDict[k][j][2])])
            j+=1
        k+=1
    p=1    
    for patent in sortedFullPatentVocabDict:
        tfidfText = ",".join([str(patent), str(sortedFullPatentVocabDict[p])])
        writer2.writerow(tfidfText.split(","))
        p+=1
    '''


timeFuncStart = time.time()
getPatentAndCalcTF(0, floor(49 / 2) - 1)  # call getPatentAndCalcTF and execute half part of patent @ 7.8 00:52
timeFuncEnd = time.time()
print("It has been {0} seconds for the get Patent and calculate TF of N-gram 1ST".format(timeFuncEnd - timeFuncStart))

timeFuncStart = time.time()
getPatentAndCalcTF(floor(49 / 2), 49 - 2)  # call getPatentAndCalcTF and execute remain part of patent @ 7.8 00:52
timeFuncEnd = time.time()

savefile_2gram.close()  # TODO : FIXED @7.7 05:29 fisrt priority problem occured in write tfidf. TFDIF csv file is same as TF csv file.
savefile_3gram.close()  # identifying of problem cause is not yet done. @ 7.9 03:00
savefile_4gram.close()
print("It has been {0} seconds for the get Patent and calculate TF of N-gram 2ND".format(timeFuncEnd - timeFuncStart))

# print(errorPatents)

##################################################################################
# CALCULATING TF-IDF 2GRAM
##################################################################################
timeStart = time.time()
# TODO : Need to group func getPatentAndCalcTF and func calcTFIDF

print("-----Calculating TF-IDF----- 2GRAM")

i = 0  # TODO: initial value of i must be changed, and it is connected to first function's parameters.
# print(fullPatentVocabDict2Gram)
for patNum in fullPatentVocabDict2Gram:
    i += 1
    j = 0
    k = 0
    for HPP in HPPList:

        # print(HPPList[k][1])
        # print(HPPList[k][2])
        # print(patNum)
        if str(HPPList[k][1]) == str(yearOfPatents) and str(HPPList[k][2]) == str(patNum):

            print(" \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ HPP FOUND AND CALCULATING TFIDF - PatNum: " + str(patNum))
            for word in fullPatentVocabDict2Gram[i]:
                word = list(word)
                word1 = word
                tf = word[1]

                # wordIdf = JjreeTFIDFNgram.idf(urlNum, word[0], numDocWithVocab2GramAscending)
                wordIdf = JjreeTFIDFNgram.idf(PatCOUNT[int(yearOfPatents) % 1989] - error1stCount - error2ndCount,
                                              word[0], numDocWithVocab2GramAscending)
                # first paramter of idf func (PatCOUNT~) means valid number of patent
                TF_IDF = float(tf * wordIdf)
                # print("2 gram word: " + str(word) + "  tf: " + str(tf) + " urlNum: " + str(urlNum) + " wordIDF: " + str(wordIdf) + " TFIDF: " + str(TF_IDF))

                word.append(TF_IDF)
                word = tuple(word)
                word1[1] = TF_IDF  # TODO: TF/IDF calculation works well. maybe save problem. overwrite on word1[1]
                # don't need to word1[1]=TF_IDF cause already word1[2]==TF_IDF is true . don't know why.
                word1 = tuple(word1)
                fullPatentVocabDict2Gram[i][j] = word1
                j += 1
        k += 1

timeNow = time.time()
print("It has been {0} seconds for the 2Gram CALCULATION to END".format(timeNow - timeStart))

timeStart = time.time()
print("-----SORTING TF-IDF----- 2GRAM")
# SORTING 2 GRAM WORDS
i = 1
sortedFullPatentVocabDict2Gram = fullPatentVocabDict2Gram
for patent in sortedFullPatentVocabDict2Gram:
    try:  # TODO: FIXED @7.9 05:41 error handler problem. if we use try, csv file will be empty ,else TFIDF file is equal to TF file.
        sortedFullPatentVocabDict2Gram[i] = sorted(sortedFullPatentVocabDict2Gram[i], key=itemgetter(1), reverse=True)
        i += 1
    except:
        print("exception")
        i += 1
        continue
timeNow = time.time()
print("It has been {0} seconds for the 2Gram SORTING to END".format(timeNow - timeStart))

timeStart = time.time()
print("-----SAVING TF-IDF----- 2GRAM")
# CHANGING 2GRAM TO WORD:TF-IDF FORMAT THEN SAVING TO FILE
k = 1  # TODO : k should change into start point temporary change value into 25

# k = 25
for patent in sortedFullPatentVocabDict2Gram:
    j = 0
    try:
        for word in sortedFullPatentVocabDict2Gram[k]:
            sortedFullPatentVocabDict2Gram[k][j] = " : ".join(
                [sortedFullPatentVocabDict2Gram[k][j][0], str(sortedFullPatentVocabDict2Gram[k][j][1])]).encode('utf-8')
            j += 1
    except:
        continue
    k += 1
p = 1
for patent in sortedFullPatentVocabDict2Gram:
    try:
        tfidfText = ",".join([str(patent), str(sortedFullPatentVocabDict2Gram[p])])
        # TODO: FIXED @7.7 16:07 L:659 'encode('utf-8')' delete
        writer2gramTFIDF.writerow(tfidfText.split(","))  # save sequence happen here.
        #  TODO : this line ,may, need two version.
        p += 1
    except:
        print("exception at save TFIDF of 2gram")
        p += 1
        continue

timeNow = time.time()
print("It has been {0} seconds for the 2Gram SAVING to END".format(timeNow - timeStart))

##################################################################################
# CALCULATING TF-IDF 3GRAM
##################################################################################
timeStart = time.time()

print("-----Calculating TF-IDF----- 3GRAM")

i = 0
for patNum in fullPatentVocabDict3Gram:
    i += 1
    j = 0
    k = 0
    for HPP in HPPList:
        if str(HPPList[k][1]) == str(yearOfPatents) and str(HPPList[k][2]) == str(patNum):

            print(
                " \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ HPP FOUND AND CALCULATING TFIDF \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            for word in fullPatentVocabDict3Gram[i]:
                word = list(word)
                word1 = word
                tf = word[1]
                # wordIdf = JjreeTFIDFNgram.idf(urlNum, word[0], numDocWithVocab3GramAscending)
                wordIdf = JjreeTFIDFNgram.idf(PatCOUNT[int(yearOfPatents) % 1989] - error1stCount - error2ndCount,
                                              word[0], numDocWithVocab3GramAscending)
                # first paramter of idf func (PatCOUNT~) means valid number of patent
                TF_IDF = float(tf * wordIdf)
                word.append(TF_IDF)
                word = tuple(word)
                word1[1] = TF_IDF
                word1 = tuple(word1)
                fullPatentVocabDict3Gram[i][j] = word1
                j += 1
        k += 1

timeNow = time.time()
print("It has been {0} seconds for the 3Gram CALCULATION to END".format(timeNow - timeStart))

timeStart = time.time()
print("-----SORTING TF-IDF----- 3GRAM")

# SORTING 3 GRAM WORDS
i = 1
sortedFullPatentVocabDict3Gram = fullPatentVocabDict3Gram
for patent in sortedFullPatentVocabDict3Gram:
    try:
        sortedFullPatentVocabDict3Gram[i] = sorted(sortedFullPatentVocabDict3Gram[i], key=itemgetter(1), reverse=True)
        i += 1
    except:
        i += 1
        continue
timeNow = time.time()
print("It has been {0} seconds for the 3Gram SORTING to END".format(timeNow - timeStart))

timeStart = time.time()
print("-----SAVING TF-IDF----- 3GRAM")
# CHANGING 3GRAM TO WORD:TF-IDF FORMAT THEN SAVING TO FILE
k = 1
for patent in sortedFullPatentVocabDict3Gram:
    j = 0
    try:
        for word in sortedFullPatentVocabDict3Gram[k]:
            sortedFullPatentVocabDict3Gram[k][j] = " : ".join(
                [sortedFullPatentVocabDict3Gram[k][j][0], str(sortedFullPatentVocabDict3Gram[k][j][1])]).encode('utf-8')
            j += 1
    except:
        print("##########ERROR SAVE 3GRAM 1ST")
        continue
    k += 1
p = 1
for patent in sortedFullPatentVocabDict3Gram:
    tfidfText = ",".join([str(patent), str(sortedFullPatentVocabDict3Gram[p])])
    # L:721 'encode('utf-8')' delete @7.7 16:07
    writer3gramTFIDF.writerow(tfidfText.split(","))
    p += 1

timeNow = time.time()
print("It has been {0} seconds for the 3Gram SAVING to END".format(timeNow - timeStart))

##################################################################################
# CALCULATING TF-IDF 4GRAM
##################################################################################
timeStart = time.time()

print("-----Calculating TF-IDF----- 4GRAM")

i = 0
for patNum in fullPatentVocabDict4Gram:
    i += 1
    j = 0
    k = 0
    for HPP in HPPList:
        if str(HPPList[k][1]) == str(yearOfPatents) and str(HPPList[k][2]) == str(patNum):

            print(
                " \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ HPP FOUND AND CALCULATING TFIDF \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            for word in fullPatentVocabDict4Gram[i]:
                word = list(word)
                word1 = word
                tf = word[1]
                # wordIdf = JjreeTFIDFNgram.idf(urlNum, word[0], numDocWithVocab4GramAscending)
                wordIdf = JjreeTFIDFNgram.idf(PatCOUNT[int(yearOfPatents) % 1989] - error1stCount - error2ndCount,
                                              word[0], numDocWithVocab4GramAscending)
                # first paramter of idf func (PatCOUNT~) means valid number of patent
                TF_IDF = float(tf * wordIdf)
                word.append(TF_IDF)
                word = tuple(word)
                word1[1] = TF_IDF
                word1 = tuple(word1)
                fullPatentVocabDict4Gram[i][j] = word1
                j += 1
        k += 1

timeNow = time.time()
print("It has been {0} seconds for the 4Gram CALCULATION to END".format(timeNow - timeStart))

timeStart = time.time()
print("-----SORTING TF-IDF----- 4GRAM")
# SORTING 4 GRAM WORDS
i = 1
sortedFullPatentVocabDict4Gram = fullPatentVocabDict4Gram
for patent in sortedFullPatentVocabDict4Gram:
    try:
        sortedFullPatentVocabDict4Gram[i] = sorted(sortedFullPatentVocabDict4Gram[i], key=itemgetter(1), reverse=True)
        i += 1
    except:
        i += 1
        continue
timeNow = time.time()
print("It has been {0} seconds for the 4Gram SORTING to END".format(timeNow - timeStart))

timeStart = time.time()
print("-----SAVING TF-IDF----- 4GRAM")
# CHANGING 4GRAM TO WORD:TF-IDF FORMAT THEN SAVING TO FILE
k = 1
for patent in sortedFullPatentVocabDict4Gram:
    j = 0
    try:
        for word in sortedFullPatentVocabDict4Gram[k]:
            sortedFullPatentVocabDict4Gram[k][j] = " : ".join(
                [sortedFullPatentVocabDict4Gram[k][j][0], str(sortedFullPatentVocabDict4Gram[k][j][1])]).encode('utf-8')
            j += 1
    except:
        continue
    k += 1
p = 1
for patent in sortedFullPatentVocabDict4Gram:
    tfidfText = ",".join([str(patent), str(sortedFullPatentVocabDict4Gram[p])])
    # L:779 'encode('utf-8')' delete @7.7 16:07
    writer4gramTFIDF.writerow(tfidfText.split(","))
    p += 1

timeNow = time.time()
print("It has been {0} seconds for the 4Gram SAVING to END".format(timeNow - timeStart))

print("END OF PROGRAM")
csvfile.close()
csvfile_DFCalc.close()
savefile.close()
savefile2.close()
# savefile_FULLTEXT.close()
# savefile_2gram.close()
# savefile_3gram.close()
# savefile_4gram.close()
savefile_2gram_TFIDF.close()
savefile_3gram_TFIDF.close()
savefile_4gram_TFIDF.close()
savefile_DFList.close()
HPPListFile.close()
# masterTxtFile.close()



######################################################################################## 
########      MAIN TEXT PROCESSING PART
#################################################################################################################################

'''
print("Starting readWEBSITE")
demo_text1 = readWEBSITE.getText('https://patents.google.com/patent/US19890093923A1/en')

#Extracting text from HTML
demo_text2 = readHTML2.getText('US7071258 - Graphene.html')
#demo_text2 = readHTML2.getText('US8871296B2 - Graphene 2.html')
#demo_text2 = readHTML1.getText('US19890079932 - Graphene 3.html')


#NLTK PUNKT Sentence Tokenizer
demo_text2a = demo_text1.decode('utf-8')
demo_text2a = punktTokenizer.tokenize(demo_text2a)
demo_text_All = demo_text2a[:]
demo_text0to99 = demo_text2a[0:100]
demo_text100to199 = demo_text2a[100:200]
demo_text200to299 = demo_text2a[200:300]
demo_text300to399 = demo_text2a[300:400]
demo_text400to499 = demo_text2a[400:500]
demo_text500to599 = demo_text2a[500:600]

textAll = '\n'.join(demo_text_All)
text1 = '\n'.join(demo_text0to99)
text2= '\n'.join(demo_text100to199)
text3 = '\n'.join(demo_text200to299)
text4 = '\n'.join(demo_text300to399)
text5 = '\n'.join(demo_text400to499)
text6 = '\n'.join(demo_text500to599)

#adding EXCEPTIONS of abbreviations
ORTH_ONLY = [u"etc.", u"Etc.", u"Appl.", u"Vol.", u"Phys.", u"Lett.", u"Ser.", u"pp.",
             u"et.", u"al.", u"FIG.", u"No.", u"1.", u"2.", u"3.", u"4.", u"5.", u"6.", 
             u"7.", u"8.", u"9.", u"10.", u"11.", u"12.", u"13.", u"14.", u"15.", u"16.", 
             u"17.", u"18.", u"19.", u"20.", u"A.", u"B.", u"D.", u"E.", u"F.", 
             u"G.", u"H.", u"I.", u"J.", u"K.", u"L.", u"M.", u"N.", u"O.", u"P.", u"Q.", 
             u"R.", u"S.", u"T.", u"U.", u"V.", u"W.", u"X.", u"Y.", u"Z."]

converted = strings_to_exc(ORTH_ONLY)
update_exc(TOKENIZER_EXCEPTIONS, converted)

#Preprocessing Text
nlp = English()
testDoc1 = nlp(textAll)

sents = []
new_sents = []
for sent in testDoc1.sents:
    sents.append(sent)
    
i=0
vocab0_ascending = {}
vocab0 = {}
vocab0_items = {}
lemma_hyphen_tag = {}
tags0 = {}
deps0 = {}
tagged_sents0 = []
vocab = {}
tags = {}
tagged_sents = []


fout = open(os.path.join("spacyoutput.txt"), "wb")
for sent in sents:
    i += 1
    print("Processing sentence# %d: %s" % (i, sent))
    token_tags = []
    token_tags_full = []
    toks = nlp(sent.text.encode("ascii", "ignore").decode("utf-8"))
    #print (toks)
    
    #svos0 = {}
    
    #svos0 = list(textacy.extract.subject_verb_object_triples(toks))
    svos0 = list(extract_jree.subject_verb_object_triples(toks))
    print("TEXTACY SVO =========")
    print(svos0)
    nounChunks = list(textacy.extract.noun_chunks(toks))
    print("NOUN CHUNKS")
    print(nounChunks)
    
    for svo in svos0:
        svo = list(svo)
        s = svo[0]
        v = svo[1]
        o = svo[2]
        s = str(s)
        o = str(o)
        eachS = s.split()
        eachS = list(eachS)
        eachO = o.split()
        eachO = list(eachO)

        for nc in nounChunks:
            lastElementInNounChunk = nc[-1] #last word in the NC list
            #extending SUBJECT as NC: when subject is compound words
            if eachS[-1] != eachS[0]:
                if eachS[0] == str(nc[-2]) and eachS[1] == str(nc[-1]):
                    svo[0] = nc
                    print("COMPOUND FOUND************************************                                  ******************************************")
            #extending SUBJECT as NC
            if str(lastElementInNounChunk) == str(svo[0]):
                svo[0] = nc
            #extending OBJECT as NC: when object is compound words
            if eachO[-1] != eachO[0]:
                if eachO[0] == str(nc[-2]) and eachO[1] == str(nc[-1]):
                    svo[2] = nc
                    print("COMPOUND FOUND************************************                                  ******************************************")
            #extending OBJECT as NC
            if str(lastElementInNounChunk) == str(svo[2]):
                svo[2] = nc
        print("NEW SVO::::::")
        print(svo)
    
    
    
    svos = []
    svos = findSVOs(toks)
    print("SPACY TUTORIAL EXAMPLE SVO------------------=========")
    print(svos)
    
    
    # 
    for tok in toks:
        token_tags.append((tok.lemma_, tok.pos_, tok.dep_))
        token_tags_full.append((tok.lemma_, tok.pos_, tok.dep_, tok.head.orth_, tok.head.head.orth_, [t.orth_ for t in tok.lefts], [t.orth_ for t in tok.rights]))
    find_hyphen = []
    clean_hyphen_tags = []
    clean_hyphen_tags_text = []
    SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]
    OBJECTS = ["dobj", "dative", "attr", "oprd"]
    
    j=0
    next_tag = []
    nextX2_tag = []
    nextX3_tag = []
    nextX4_tag = []
    nextX5_tag = []
    nextX6_tag = []
    nextX7_tag = []
    nextWordAfterHyphen = False
    
    for hyphen_tag, next_tag, nextX2_tag, nextX3_tag, nextX4_tag, nextX5_tag, nextX6_tag in itertools.izip_longest(token_tags_full, token_tags[1:], token_tags[2:], token_tags[3:], token_tags[4:], token_tags[5:], token_tags[6:]):     
        hyphenated_word = []
        
        if hyphen_tag[1] == u"SPACE":
            continue
        
        '''

'''
        stopword = vocab.(hyphen_tag[0])
        if stopword.is_stop:
            print("STOPWORDWASHERE")
            continue
        '''

'''   
            
        #if hyphen_tag[0] == u"(" or u")" and hyphen_tag[1] == u"PUNCT":
        #    continue
        if hyphen_tag[0] == u"-":
            nextWordAfterHyphen = True #switch ON for following word skipping if comes after hyphen
            continue
        if nextWordAfterHyphen == True:
            nextWordAfterHyphen = False #switch OFF after skipping word after hyphen
            continue
        #cleaning text if hyphen found
     
        #double hyphenated word
        if (nextX3_tag is not None and next_tag[0] == u"-" and nextX3_tag[0] == u"-"):
            hyphenated_word.append("".join((hyphen_tag[0], next_tag[0], nextX2_tag[0], nextX3_tag[0], nextX4_tag[0])))
            hyphen_tag = list(hyphen_tag)
            hyphen_tag[0] = hyphenated_word[0]
            
            #COMPOUND NOUN/PRONOUN = NOUN
            if (hyphen_tag[1] == u'NOUN' or u'PROPN' and nextX2_tag[1] == u'NOUN' or u'PROPN' 
                and nextX4_tag[1] == u'NOUN' or u'PROPN' and nextX5_tag[1] == u'VERB'):
                hyphen_tag[1] == u'NOUN'    
            #COMPOUND ADJ = ADJ
            if (hyphen_tag[1] == u'NOUN' or u'PROPN' and nextX2_tag[1] == u'ADJ'):
                hyphen_tag[1] = u'ADJ'
            if (hyphen_tag[1] == u'NOUN' or u'PROPN' and nextX2_tag[1] == u'PART'):
                hyphen_tag[1] = u'ADJ'
            if (hyphen_tag[1] == u'ADJ' and nextX2_tag[1] == u'PART'):
                hyphen_tag[1] = u'ADJ'
            #COMPOUND VERB
            if (hyphen_tag[1] == u'NOUN' and nextX2_tag[1] == u'NOUN' and nextX4_tag[1] == u'NOUN' and nextX5_tag[1] != u'VERB' and nextX6_tag[1] != u'VERB'):
                hyphen_tag[1] = u'VERB'
            if all ([hyphen_tag[1] == u'NOUN', nextX2_tag[1] == u'VERB']):
                hyphen_tag[1] = u'VERB'
            #NUMBER-NUMBER = NUMBER    
            #if all ([hyphen_tag[1] == u'NUM', nextX2_tag[1] == u'NUM']):
            #    hyphen_tag[1] = u'NUM'
            #Exception such as when tagger makes mistake
            if (nextX5_tag[1] == u'NOUN' or u'PROPN'):
                hyphen_tag[1] = u'ADJ'
            if (nextX5_tag[1] == u'ADJ' and nextX6_tag[1] == u'NOUN'):
                hyphen_tag[1] = u'ADJ'
            hyphen_tag[2] = nextX4_tag[2]
            hyphen_tag = tuple(hyphen_tag)
        
        #single hyphenated word    
        if (nextX3_tag is not None and next_tag[0] == u"-" and nextX3_tag[0] != u"-"):
            hyphenated_word.append(("".join((hyphen_tag[0], next_tag[0], nextX2_tag[0])))) 
            hyphen_tag = list(hyphen_tag)
            temp_tag = [u'', u'']
            is_compound_noun = False
            
            #COMPOUND NOUN/PRONOUN = NOUN
            if (((hyphen_tag[1] == u'NOUN') or (hyphen_tag[1] ==u'PROPN')) 
                                                and ((nextX2_tag[1] == u'NOUN') or (nextX2_tag[1] == u'PROPN')) 
                                                and (((nextX3_tag[1] == u'VERB') or (nextX3_tag[1] == u'PUNCT') 
                                                      or (nextX3_tag[1] == u'CONJ') or (nextX3_tag[1] == u'ADP')))):
                temp_tag[1] == u'NOUN'  
                is_compound_noun = True  
            #COMPOUND ADJ = ADJ
            if ((hyphen_tag[1] == (u'NOUN' or u'PROPN')) and (nextX2_tag[1] == u'ADJ') 
                                                    and (nextX3_tag[1] == u'ADJ' or nextX3_tag[1] == u'NOUN')):
                temp_tag[1] = u'ADJ'
            if ((hyphen_tag[1] == (u'NOUN' or u'PROPN')) and (nextX2_tag[1] == u'PART') 
                                                        and (nextX2_tag[1] != u'VERB')):
                temp_tag[1] = u'ADJ'
            if ((hyphen_tag[1] == u'ADJ') and (nextX2_tag[1] == u'PART')):
                temp_tag[1] = u'ADJ'
            #COMPOUND VERB
            if ((hyphen_tag[1] == u'NOUN') and (nextX2_tag[1] == u'NOUN') 
                                            and (nextX3_tag[1] != u'VERB') 
                                            and (nextX4_tag[1] != u'VERB') ):
                if is_compound_noun == True:
                    temp_tag[1] = u'NOUN'
                if is_compound_noun == False:
                    temp_tag[1] = u'VERB'
            if ((hyphen_tag[1] == u'NOUN') and (nextX2_tag[1] == u'VERB') 
                                            and (hyphen_tag[0] != u"un") 
                                            and (hyphen_tag[0] != u"re") 
                                            and (hyphen_tag[0] != u"ir")):
                temp_tag[1] = u'VERB'
            #Exception such as when tagger makes mistake
            if ((nextX3_tag[1] == u'NOUN' or u'PROPN') and (nextX3_tag[1] != u'PART') and (nextX3_tag[1] != u'ADP') and (nextX3_tag[1] != u'PUNCT')):
                temp_tag[1] = u'ADJ'
            if ((nextX3_tag[1] == u'ADJ') and (nextX4_tag[1] == u'NOUN')):
                temp_tag[1] == u'ADJ'
            #NUMBER-NUMBER = NUMBER
            if all ([hyphen_tag[1] == u'NUM', nextX2_tag[1] == u'NUM']):
                temp_tag[1] = u'NUM'
            if ((hyphen_tag[1] == u'NOUN') and (nextX2_tag[1] == u'ADV')):
                temp_tag[1] = u'ADV'
            if ((hyphen_tag[1] == u'ADV') and (nextX2_tag[1] == u'VERB')):
                temp_tag[1] = u'ADJ'
            
            if(temp_tag[1] == u''):
                temp_tag[1] = nextX2_tag[1]
                
            hyphen_tag[0] = hyphenated_word[0]
            hyphen_tag[1] = temp_tag[1]
            hyphen_tag[2] = nextX2_tag[2]
            print("++++ Hyphen tag[1] of " + str(hyphen_tag[0]) + " is : " + str(hyphen_tag[1]) + " and hyphen tag DEP_ is: " + str(hyphen_tag[2]))
            hyphen_tag = tuple(hyphen_tag)
            
        clean_hyphen_tags.append(hyphen_tag)
        clean_hyphen_tags_text.append(hyphen_tag[0])
        #print(clean_hyphen_tags_text)
        
        #lemma_hyphen_tag[0] = hyphen_tag[0].lemma_
        #print (lemma_hyphen_tag[0])
        if (nlp.vocab[hyphen_tag[0]].is_stop == False) and (hyphen_tag[1] != u'PUNCT') and (hyphen_tag[1] != u'NUM'):
            vocab0[hyphen_tag[0]] = vocab0.get(hyphen_tag[0], 0) + 1
            tags0[hyphen_tag[1]] = tags0.get(hyphen_tag[1], 0) + 1
            deps0[hyphen_tag[2]] = deps0.get(hyphen_tag[2], 0) + 1
    tagged_sents0.append(clean_hyphen_tags)

    #sorting Term Frequency of Words most to least
    #print(tags0)
    #print(deps0)
    vocab0_items = vocab0.items()
    vocab0_ascending = sorted(vocab0_items, key= lambda x: x[1]*-1)   
    #print(vocab0_ascending)
    
    '''
#########
#
# SAO EXTRACTION
#
#########

# print(clean_hyphen_tags_text)
'''
    svos = []
    
    verbs = [tok for tok in clean_hyphen_tags if tok[1] == "VERB" and tok[2] != "aux"]
    print(verbs)
    for v in verbs:
            subs = [tok for tok in v[5] if tok[2] in SUBJECTS and tok[1] != "DET"]
            print(subs)
            
            subs, verbNegated = getAllSubs(v)
            if len(subs) >0:
                v, objs = getAllObjs(v,clean_hyphen_tags_text)
                for sub in subs:
                    for obj in objs:
                        objNegated = isNegated(obj)
                        svos.append((sub.lower_, "!"+v.lower_ if verbNegated or objNegated else v.lower_, obj.lower_))
            
    print(svos)
    '''

'''
    for tok in clean_hyphen_tags:
            
        if tok[1] == "VERB" and tok[2] !="aux":
            verbs = []
            verbs = tok
            print("---VERB---")
            print(verbs)
            
        if tok[2] in SUBJECTS:
            subjects = []
            subjects = tok
            print("===SUBJECT===")
            print(subjects)
        if tok[2] in OBJECTS:
            objects = []
            objects = tok
            print("<<<OBJECTS>>>")
            print(objects)
    
    
        
        
    #print(findSVOs(toks))  
    
    
    cleaned_sentences1 = " ".join(["/".join([hyphen_tag[0], hyphen_tag[1]])
            for hyphen_tag in clean_hyphen_tags])
    
    #print(cleaned_sentences1)
    
    
    #print("vocab:: %s\n" % " ".join(vocab0[:]))
    print("HYPHEN Processed: %s\n" % (" ".join(["/".join([hyphen_tag[0], hyphen_tag[1], hyphen_tag[2]])
        for hyphen_tag in clean_hyphen_tags])))
    fout.write("%s\n" % (" ".join(["/".join([hyphen_tag[0], hyphen_tag[1], hyphen_tag[2]]) 
        for hyphen_tag in clean_hyphen_tags])))
    
    
    clean_token_tags = []
    for tt in token_tags:
        if tt[1] == u"SPACE":
            continue
        clean_token_tags.append(tt)
        vocab[tt[0]] = vocab.get(tt[0], 0) + 1
        tags[tt[1]] = tags.get(tt[1], 0) + 1
    tagged_sents.append(clean_token_tags)
    print("Processed sentence: %s\n" % (" ".join(["/".join([tt[0], tt[1], tt[2]])
        for tt in clean_token_tags])))
    fout.write("%s\n" % (" ".join(["/".join([tt[0], tt[1], tt[2]]) 
        for tt in clean_token_tags])))
    
    
fout.close()
#[t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])
'''

'''
#5grams of sentences
fgrams = open(os.path.join("spacyoutput_ngrams.txt"), "wb")
for tagged_sent in tagged_sents:
    sent_grams = []
    gram_labels = []
    # lowercase the words
    tagged_sent = [(x[0].lower(), x[1]) for x in tagged_sent]
    # replace with UNK for specific words
    tagged_sent = [(x[0] if vocab.has_key(x[0]) else "UNK", x[1]) 
                         for x in tagged_sent]
    # put pre- and post- padding
    tagged_sent.insert(0, ("PAD", "PAD"))
    tagged_sent.insert(0, ("PAD", "PAD"))
    tagged_sent.append(("PAD", "PAD"))
    tagged_sent.append(("PAD", "PAD"))
    for i in range(len(tagged_sent) - 4):
        sent_gram = tagged_sent[i:i+5]
        # label of middle word, and input words is 5-gram around word
        fgrams.write("%s\t%s\n" % (sent_gram[2][1], 
                                   " ".join([x[0] for x in sent_gram])))
fgrams.close()
'''

'''
print('')
print('')
print(
    '            ,                                                                                                                              ')
print(
    '      .I7777~                                                                                                                              ')
print(
    '     .I7777777                                                                                                                             ')
print(
    '   +.  77777777                                                                                                                            ')
print(
    ' =???,  I7777777=                                                                                                                          ')
print(
    '=??????   7777777?   ,:::===?                                                                                                              ')
print(
    '=???????.  777777777777777777~         .77:    ??           :7                                              =$,     :$$$$$$+  =$?          ')
print(
    ' ????????: .777777777777777777         II77    ??           :7                                              $$7     :$?   7$7 =$?          ')
print(
    '  .???????=  +7777777777777777        .7 =7:   ??   :7777+  :7:I777?    ?777I=  77~777? ,777I I7      77   +$?$:    :$?    $$ =$?          ')
print(
    '    ???????+  ~777???+===:::         :7+  ~7   ?? .77    +7 :7?.   II  7~   ,I7 77+   I77   ~7 ?7    =7:  .$, =$    :$?  ,$$? =$?          ')
print(
    '    ,???????~                        77    7:  ?? ?I.     7 :7     :7 ~7      7 77    =7:    7  7    7~   7$   $=   :$$$$$$~  =$?          ')
print(
    '    .???????  ,???I77777777777~     :77777777~ ?? 7:        :7     :7 777777777:77    =7     7  +7  ~7   $$$$$$$$I  :$?       =$?          ')
print(
    '   .???????  ,7777777777777777      7=      77 ?? I+      7 :7     :7 ??      7,77    =7     7   7~ 7,  =$7     $$, :$?       =$?          ')
print(
    '  .???????. I77777777777777777     +7       ,7???  77    I7 :7     :7  7~   .?7 77    =7     7   ,77I   $+       7$ :$?       =$?          ')
print(
    ' ,???????= :77777777777777777~     7=        ~7??  ~I77777  :7     :7  ,777777. 77    =7     7    77,  +$        .$::$?       =$?          ')
print(
    ',???????  :7777777                                                                                77                                       ')
print(
    ' =?????  ,7777777                                                                               77=                                        ')
print(
    '   +?+  7777777?                                                                                                                           ')
print(
    '    +  ~7777777                                                                                                                            ')
print(
    '       I777777                                                                                                                             ')
print(
    '          :~                                                                                                                               ')
'''

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()
# output = open('output.txt', 'w')


'''
text0to99 = Path('outputList1.txt')
text1 = text0to99.read_text()

text0to99.close()

text100to199 = open('outputList2.txt', 'r')
text2 = text100to199.read()
text100to199.close()

text200to299 = open('outputList3.txt', 'r')
text3 = text200to299.read()
text200to299.close()

text300to399 = open('outputList4.txt', 'r')
text4 = text300to399.read()
text300to399.close()

text400to499 = open('outputList5.txt', 'r')
text5 = text400to499.read()
text400to499.close()

text500to599 = open('outputList6.txt', 'r')
text6 = text500to599.read()
text500to599.close()
'''

'''
print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Entities ##')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text', demo_text)

if response['status'] == 'OK':
    print('## Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Concepts ##')
    for concept in response['concepts']:
        print('text: ', concept['text'])
        print('relevance: ', concept['relevance'])
        print('')
else:
    print('Error in concept tagging call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')
print('')
print('')

print('Processing html: ', demo_html)
print('')

response = alchemyapi.sentiment('html', demo_html)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Document Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in sentiment analysis call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Targeted Sentiment Analysis Example    #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.sentiment_targeted('text', demo_text, 'Denver')

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Targeted Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in targeted sentiment analysis call: ',
          response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Text Extraction Example                #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.text('url', demo_url)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Text ##')
    print('text: ', response['text'].encode('utf-8'))
    print('')
else:
    print('Error in text extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Author Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.author('url', demo_url)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Author ##')
    print('author: ', response['author'].encode('utf-8'))
    print('')
else:
    print('Error in author extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Language Detection Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.language('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Language ##')
    print('language: ', response['language'])
    print('iso-639-1: ', response['iso-639-1'])
    print('native speakers: ', response['native-speakers'])
    print('')
else:
    print('Error in language detection call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Title Extraction Example               #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.title('url', demo_url)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Title ##')
    print('title: ', response['title'].encode('utf-8'))
    print('')
else:
    print('Error in title extraction call: ', response['statusInfo'])
'''

'''
print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', text1)
print('')
output.write("Processing text: " + text1.encode('utf-8'))
output.write("")

OPTIONS = {'maxRetrieve': 100, 'keywords': 1}
response = alchemyapi.relations('text', text1, OPTIONS)

if response['status'] == 'OK':
    numSAO = 0
    print('## Object ##')
    output.write("## Object ##")
    print(json.dumps(response, indent=4))
    output.write(json.dumps(response, indent=4))

    print('')
    print('## Relations ##')
    output.write("" + '\n')
    output.write("## Relations ##" + '\n')
    
    subject0 = ""
    subject1 = "a"
    for relation in response['relations']:
        subject1 = relation['subject']['text'].encode('utf-8')
        if subject0 !=subject1:
            if 'subject' in relation:
                print ("------ SAO NUMBER: " , numSAO+1, " ------")
                print('Subject: ', relation['subject']['text'].encode('utf-8'))
                output.write('\n' + '\n' + "------ SAO NUMBER: " + str(numSAO+1) + "------" + '\n')
                output.write("Subject: " + relation['subject']['text'].encode('utf-8')+ '\n')
            if 'action' in relation:
                print('Action: ', relation['action']['text'].encode('utf-8'))
                output.write("Action: " + relation['action']['text'].encode('utf-8')+ '\n')    
            if 'object' in relation:
                print('Object: ', relation['object']['text'].encode('utf-8'))
                output.write("Object: " + relation['object']['text'].encode('utf-8') + '\n')
            if 'subject' in relation and 'action' in relation and 'object' in relation: 
                print('SAO: ', relation['subject']['text'].encode('utf-8'), relation['action']['text'].encode('utf-8'), relation['object']['text'].encode('utf-8')) 
                print('Simplified: ', relation['subject']['text'].encode('utf-8'), relation['action']['text'].encode('utf-8'), relation['object']['text'].encode('utf-8'))
                testDoc1 = nlp(relation['subject']['text'] + relation['action']['text'] + relation['object']['text'])
                for word in testDoc1:
                    print(word.text, word.lemma_, word.tag_, word.pos_)
                print(findSVOs(testDoc1))
                    
                output.write("SAO: " + relation['subject']['text'].encode('utf-8') + " " + relation['action']['text'].encode('utf-8') + " "  + relation['object']['text'].encode('utf-8') + '\n')
                output.write('Simplified: ' + relation['subject']['text'].encode('utf-8') + " " + relation['action']['text'].encode('utf-8') + " " + relation['object']['text'].encode('utf-8') + '\n')
            print('')
            output.write('\n')
            numSAO = numSAO+1
            subject0 = relation['subject']['text'].encode('utf-8')
    
else:
    print('Error in relation extraction call: ', response['statusInfo'])

print('Number of SAO: ', numSAO)
output.write('\n' + "Number of SAO: " + str(numSAO))

print('Processing text: ', text2)
print('')
output.write("Processing text: " + text2.encode('utf-8'))
output.write("")

OPTIONS = {'maxRetrieve': 100, 'keywords': 1}
response = alchemyapi.relations('text', text2, OPTIONS)

if response['status'] == 'OK':
    #print('## Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Relations ##')
    output.write("" + '\n')
    output.write("## Relations ##" + '\n')
    

    for relation in response['relations']:
        subject1 = relation['subject']['text'].encode('utf-8')
        if subject0 !=subject1:
            if 'subject' in relation:
                print ("------ SAO NUMBER: " , numSAO+1, " ------")
                print('Subject: ', relation['subject']['text'].encode('utf-8'))
                output.write('\n' + '\n' + "------ SAO NUMBER: " + str(numSAO+1) + "------" + '\n')
                output.write("Subject: " + relation['subject']['text'].encode('utf-8')+ '\n')
            if 'action' in relation:
                print('Action: ', relation['action']['text'].encode('utf-8'))
                output.write("Action: " + relation['action']['text'].encode('utf-8')+ '\n')    
            if 'object' in relation:
                print('Object: ', relation['object']['text'].encode('utf-8'))
                output.write("Object: " + relation['object']['text'].encode('utf-8') + '\n')
            if 'subject' in relation and 'action' in relation and 'object' in relation: 
                print('SAO: ', relation['subject']['text'].encode('utf-8'), relation['action']['text'].encode('utf-8'), relation['object']['text'].encode('utf-8')) 
                print('Simplified: ', relation['subject']['text'].encode('utf-8'), relation['action']['text'].encode('utf-8'), relation['object']['text'].encode('utf-8'))
                output.write("SAO: " + relation['subject']['text'].encode('utf-8') + " " + relation['action']['text'].encode('utf-8') + " "  + relation['object']['text'].encode('utf-8') + '\n')
                output.write('Simplified: ' + relation['subject']['text'].encode('utf-8') + " " + relation['action']['text'].encode('utf-8') + " " + relation['object']['text'].encode('utf-8') + '\n')
            print('')
            output.write('\n')
            numSAO = numSAO+1
            subject0 = relation['subject']['text'].encode('utf-8')
    
else:
    print('Error in relation extraction call: ', response['statusInfo'])

print('Number of SAO: ', numSAO)
output.write('\n' + "Number of SAO: " + str(numSAO))
'''

'''
print('')
print('')
print('')
print('############################################')
print('#   Taxonomy  Example                      #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.taxonomy('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Categories ##')
    for category in response['taxonomy']:
        print(category['label'], ' : ', category['score'])
    print('')

else:
    print('Error in taxonomy call: ', response['statusInfo'])

print('')
print('')
'''
