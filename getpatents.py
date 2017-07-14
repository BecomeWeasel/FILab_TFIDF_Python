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
    timestart=time.time()
    getpatents_directory = os.getcwd()  # get current working directory
    errorCount = 0
    nlp = English()
    nlp.vocab["the"].is_stop = True
    nlp.vocab["THE"].is_stop = True
    PATCOUNT_ORIGIN = [205, 260, 280, 264, 298, 301, 293, 282, 332, 315, 346, 311, 265, 326, 375, 309, 348, 339, 446,
                       490, 488, 628, 723, 827, 884, 968, 1002, 1084, 1304, 1482, 1648, 1843, 2251, 2928, 3639, 3958,
                       3623, 2927, 2047, 904, 99
                       ]
    store_chunks_str_FullParent = []

    getpatents_directory_output = getpatents_directory + "/Patents/"
    if not os.path.exists(getpatents_directory_output):
        os.mkdir(getpatents_directory_output, 0o755)

    i = 0

    csvfile_PatNUM = open('(03) SolarPV_41585 Patent List ORIGINAL with dssc patents 9501 v0.2 only num.csv', 'r')
    csvfile_ouput_by_year = open(getpatents_directory_output + str(year) + '.csv', 'w+')

    reader_PatNO = csv.reader(csvfile_PatNUM, delimiter=' ', quotechar='|')
    writer_yearoutput = csv.writer(csvfile_ouput_by_year, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

    PATNUM = []

    for PATNO in reader_PatNO:
        PATNUM.append(PATNO[0])

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
            store_chunks_str_singlePatent.append(test)
        store_chunks_str_FullParent.append(store_chunks_str_singlePatent)

    for row_input in store_chunks_str_FullParent:
        row_input = str(row_input)
        writer_yearoutput.writerow(row_input.split(","))

    csvfile_PatNUM.close()
    csvfile_ouput_by_year.close()
    timeend=time.time()
    print("it takes {0} sec for the get Patent text of {1}".format((timeend - timestart),year))

    return None


getpatents(1976)
