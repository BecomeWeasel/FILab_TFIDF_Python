from __future__ import division
from __future__ import print_function
from alchemyapi import AlchemyAPI
from pathlib import Path
import json
import os
import time
import io
from multiprocessing import *
from math import floor

import readWEBSITE

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


def getpatents(year):
    timestart = time.time()
    getpatents_directory = os.getcwd()  # get current working directory
    errorCount = 0
    nlp = English()
    PATCOUNT_ORIGIN = [205, 260, 280, 264, 298, 301, 293, 282, 332, 315, 346, 311, 265, 326, 375, 309, 348, 339, 446,
                       490, 488, 628, 723, 827, 884, 968, 1002, 1084, 1304, 1482, 1648, 1843, 2251, 2928, 3639, 3958,
                       3623, 2927, 2047, 904, 99
                       ]
    store_chunks_str_FullParent = []

    getpatents_directory_output = getpatents_directory + "/Patents/"
    if not os.path.exists(getpatents_directory_output):
        os.mkdir(getpatents_directory_output, 0o755)

    csvfile_PatNUM = open('(03) SolarPV_41585 Patent List ORIGINAL with dssc patents 9501 v0.2 only num.csv', 'r')
    csvfile_ouput_by_year = open(getpatents_directory_output + str(year) + '.csv', 'w+')

    reader_PatNO = csv.reader(csvfile_PatNUM, delimiter=' ', quotechar='|')
    writer_yearoutput = csv.writer(csvfile_ouput_by_year, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

    PATNUM = []
    tmp = 0
    sumstart = 0
    j = 0

    for PatCountofYear in PATCOUNT_ORIGIN:
        if tmp >= year - 1976:
            break
        else:
            sumstart += PatCountofYear
            tmp += 1
    PAT_HEADER = sumstart  # if PAT_HEADER=n,PAT_HEADER pointed nth row exactly in reader_PatNO.

    for PATNO in reader_PatNO:
        PATNUM.append(PATNO[0])
    # print(PATNUM[206])
    while j < PATCOUNT_ORIGIN[year % 1976]:
        PAT_HEADER += 1  # HEADER가 어디선가 +1이 안되고있움.
        # print(PAT_HEADER)
        if PAT_HEADER == (
                        sumstart + PATCOUNT_ORIGIN[year % 1976] + 1):  # HEADER value exceed valid range of year's patent count.
            break

        url = ''.join(['https://patents.google.com/patent/', PATNUM[PAT_HEADER - 1],
                       '/en'])  # row 1 in reader_PatNO is stored PATNUM[0].

        print("\nURL NUMBER : " + str(PAT_HEADER) + " = " + url + "\n")

        urlText, backCitation, pubDate = readWEBSITE.getText(url)

        if urlText is None:  # error occur at parsing patent.
            errorCount += 1
            continue
        j += 1

        doc = nlp(urlText.decode('utf-8'))
        chunks_store = []
        store_chunks_str_singlePatent = []

        for word in doc.noun_chunks:
            chunks_store.append(word)

        for span in chunks_store:

            store_str = span.text  # get text part of span in chunks_store.
            tmp = store_str.split()
            splited_word = []
            for splited_single_word in tmp:
                stop_TF = False
                if splited_single_word == 'a':
                    stop_TF = True
                if splited_single_word == 'A':
                    stop_TF = True
                if splited_single_word == 'an':
                    stop_TF = True
                if splited_single_word == 'An':
                    stop_TF = True
                if splited_single_word == 'the':
                    stop_TF = True
                if splited_single_word == 'The':
                    stop_TF = True
                if splited_single_word == 'THE':
                    stop_TF = True
                if splited_single_word == 'this':
                    stop_TF = True
                if splited_single_word == 'This':
                    stop_TF = True
                if splited_single_word == 'their':
                    stop_TF = True
                if splited_single_word == 'Their':
                    stop_TF = True
                if splited_single_word == 'Such':
                    stop_TF = True
                if splited_single_word == 'such':
                    stop_TF = True
                if splited_single_word == 'it':
                    stop_TF = True
                if splited_single_word == 'It':
                    stop_TF = True
                if splited_single_word == 'they':
                    stop_TF = True
                if splited_single_word == 'They':
                    stop_TF = True
                if splited_single_word == 'these':
                    stop_TF = True
                if splited_single_word == 'These':
                    stop_TF = True
                if stop_TF is True:
                    continue
                else:
                    splited_word.append(splited_single_word)

            test = " ".join(splited_word)
            if test is "":
                continue
            store_chunks_str_singlePatent.append(test)
        store_chunks_str_FullParent.append(store_chunks_str_singlePatent)

    for row_input in store_chunks_str_FullParent:
        row_input = str(row_input)
        writer_yearoutput.writerow(row_input.split(","))

    print("Error occur {0} times. Success {1} times\n".format(errorCount,j))
    csvfile_PatNUM.close()
    csvfile_ouput_by_year.close()
    timeend = time.time()
    print("it takes {0} sec for the get Patent text of {1}".format((timeend - timestart), year))

    return None


getpatents(2008)
############ DONE #############
##############################
'''
getpatents(2001)
getpatents(2002)
getpatents(2003)
getpatents(2004)
getpatents(2005)
getpatents(2006)
getpatents(2007)
getpatents(2008)
getpatents(2009)
getpatents(2010)
getpatents(2011)
getpatents(2012)
getpatents(2013)
getpatents(2014)
getpatents(2015)
getpatents(2016)
'''
'''
if __name__ == '__main__':
    yearinput = 1976
    while yearinput < 2016:
        p = Pool()
        result = p.map_async(getpatents, range(yearinput, yearinput + 2))
        result.wait()
        p.close()
        print("Parallel complete for {0} to {1}".format(yearinput, yearinput + 2))
        yearinput += 2
'''