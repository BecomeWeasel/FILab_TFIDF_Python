from __future__ import division
from __future__ import print_function

import csv
import os.path
import time
from multiprocessing import *

from spacy.en import English
from textacy import *

import readWEBSITE


# import docx
# import readDocx
# from tkFont import BOLD


def getpatents(targetyear):
    timestart = time.time()
    getpatents_directory = os.getcwd()  # get current working directory
    errorCount = 0
    nlp = English()
    PATCOUNT_ORIGIN = [205, 260, 280, 264, 298, 301, 293, 282, 332, 315, 346, 311, 265, 326, 375, 309, 348, 339, 446,
                       490, 488, 628, 723, 827, 884, 968, 1002, 1084, 1304, 1482, 1648, 1843, 2251, 2928, 3639, 3958,
                       3623, 2927, 2047, 904, 99
                       ]
    store_chunks_FullParent = []

    getpatents_directory_output = getpatents_directory + "/Patents/"
    if not os.path.exists(getpatents_directory_output):
        os.mkdir(getpatents_directory_output, 0o755)

    csvfile_PatNUM = open('(03) SolarPV_41585 Patent List ORIGINAL with dssc patents 9501 v0.2 only num.csv', 'r')
    csvfile_ouput_by_year = open(getpatents_directory_output + str(targetyear) + '.csv', 'w+')

    reader_PatNO = csv.reader(csvfile_PatNUM, delimiter=' ', quotechar='|')
    writer_yearoutput = csv.writer(csvfile_ouput_by_year, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

    PATNUM = []
    splited_words = 0
    sumstart = 0
    normalcount = 0

    for PatCountofYear in PATCOUNT_ORIGIN:  # this for loop make PAT_HEADER set into right position.
        if splited_words >= targetyear - 1976:  # e.g , if targetyaer is 1977, PAT_HEADER need to start from 206. so sumstart=205 and PAT HEADER started from 206.
            break
        else:
            sumstart += PatCountofYear
            splited_words += 1
    PAT_HEADER = sumstart  # if PAT_HEADER=n,PAT_HEADER pointed nth row exactly in reader_PatNO.

    for PATNO in reader_PatNO:
        PATNUM.append(PATNO[0])
    # print(PATNUM[206])
    while normalcount < PATCOUNT_ORIGIN[targetyear % 1976]:
        PAT_HEADER += 1  # HEADER가 어디선가 +1이 안되고있움.
        # print(PAT_HEADER)
        if PAT_HEADER == (sumstart + PATCOUNT_ORIGIN[targetyear % 1976] + 1):
            # HEADER value exceed valid range of year's patent count.
            break

        url = ''.join(['https://patents.google.com/patent/', PATNUM[PAT_HEADER - 1],
                       '/en'])  # row 1 in reader_PatNO is stored PATNUM[0].

        print("\nURL NUMBER : " + str(PAT_HEADER) + " = " + url + "\n")

        urlText, backCitation, pubDate = readWEBSITE.getText(url)

        if urlText is None:  # error occur at parsing patent.
            errorCount += 1
            continue
        normalcount += 1

        doc = nlp(urlText.decode('utf-8'))
        chunks_store = []
        store_chunks_singlePatent = []
        store_chunks_singlePatent.append(PAT_HEADER)

        for word in doc.noun_chunks:
            chunks_store.append(word)

        for span in chunks_store:

            store_str = span.text  # get text part of span in chunks_store.
            splited_words = store_str.split()
            splited_word = []
            # store_chunks_singlePatent.append()
            for splited_single_word in splited_words:
                stop_TF = False
                ########### Below down is temporary 'stop word list' ##########
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
                if stop_TF is True:  # if word is in stopword list,check next word.
                    continue
                else:
                    splited_word.append(splited_single_word)

            combinedWord = " ".join(splited_word)  # join word into one string.
            if combinedWord is "":  # if string is null, string of word don't append into list.
                continue
            store_chunks_singlePatent.append(
                combinedWord)  # store_chunks_str_singlePatents store all of words used in particular PATENT.

        store_chunks_FullParent.append(
            store_chunks_singlePatent)  # store_chunks_str_FulParent store all of word used in all patent of targetyear.

    for row_input in store_chunks_FullParent:
        row_input = str(row_input)
        writer_yearoutput.writerow(row_input.split(","))

    print("Error occur {0} times. Success {1} times\n".format(errorCount, normalcount))
    csvfile_PatNUM.close()
    csvfile_ouput_by_year.close()
    timeend = time.time()
    print("it takes {0} sec for the get Patent text of {1}".format((timeend - timestart), targetyear))

    return None


getpatents(1977)
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
# '''
if __name__ == '__main__':
    yearinput = 1976
    while yearinput < 2016:
        p = Pool()
        result = p.map_async(getpatents, range(yearinput, yearinput + 2))
        result.wait()
        p.close()
        print("Parallel complete for {0} to {1}".format(yearinput, yearinput + 2))
        yearinput += 2
        # '''
