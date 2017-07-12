from __future__ import division
from __future__ import print_function
import csv
import math
import os


def dfRead(HPPword, HPPkey, HPPwordList):
    # only 1GRAM TFIDF OUTPUT OF ALL PATENT AT THAT YEAR

    directory = os.getcwd()
    directory += "/inputs/"

    csvfile_1989_wordList = open(directory + 'TF-IDF OUTPUT (1989) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1990_wordList = open(directory + 'TF-IDF OUTPUT (1990) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1991_wordList = open(directory + 'TF-IDF OUTPUT (1991) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1992_wordList = open(directory + 'TF-IDF OUTPUT (1992) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1993_wordList = open(directory + 'TF-IDF OUTPUT (1993) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1994_wordList = open(directory + 'TF-IDF OUTPUT (1994) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1995_wordList = open(directory + 'TF-IDF OUTPUT (1995) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1996_wordList = open(directory + 'TF-IDF OUTPUT (1996) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1997_wordList = open(directory + 'TF-IDF OUTPUT (1997) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1998_wordList = open(directory + 'TF-IDF OUTPUT (1998) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_1999_wordList = open(directory + 'TF-IDF OUTPUT (1999) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2000_wordList = open(directory + 'TF-IDF OUTPUT (2000) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2001_wordList = open(directory + 'TF-IDF OUTPUT (2001) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2002_wordList = open(directory + 'TF-IDF OUTPUT (2002) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2003_wordList = open(directory + 'TF-IDF OUTPUT (2003) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2004_wordList = open(directory + 'TF-IDF OUTPUT (2004) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2005_wordList = open(directory + 'TF-IDF OUTPUT (2005) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2006_wordList = open(directory + 'TF-IDF OUTPUT (2006) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2007_wordList = open(directory + 'TF-IDF OUTPUT (2007) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2008_wordList = open(directory + 'TF-IDF OUTPUT (2008) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2009_wordList = open(directory + 'TF-IDF OUTPUT (2009) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2010_wordList = open(directory + 'TF-IDF OUTPUT (2010) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2011_wordList = open(directory + 'TF-IDF OUTPUT (2011) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2012_wordList = open(directory + 'TF-IDF OUTPUT (2012) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2013_wordList = open(directory + 'TF-IDF OUTPUT (2013) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2014_wordList = open(directory + 'TF-IDF OUTPUT (2014) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2015_wordList = open(directory + 'TF-IDF OUTPUT (2015) RAW WORDS FOR DF CALC.csv', 'r+')
    csvfile_2016_wordList = open(directory + 'TF-IDF OUTPUT (2016) RAW WORDS FOR DF CALC.csv', 'r+')

    reader1989 = csv.reader(csvfile_1989_wordList, delimiter=' ', quotechar='|')
    reader1990 = csv.reader(csvfile_1990_wordList, delimiter=' ', quotechar='|')
    reader1991 = csv.reader(csvfile_1991_wordList, delimiter=' ', quotechar='|')
    reader1992 = csv.reader(csvfile_1992_wordList, delimiter=' ', quotechar='|')
    reader1993 = csv.reader(csvfile_1993_wordList, delimiter=' ', quotechar='|')
    reader1994 = csv.reader(csvfile_1994_wordList, delimiter=' ', quotechar='|')
    reader1995 = csv.reader(csvfile_1995_wordList, delimiter=' ', quotechar='|')
    reader1996 = csv.reader(csvfile_1996_wordList, delimiter=' ', quotechar='|')
    reader1997 = csv.reader(csvfile_1997_wordList, delimiter=' ', quotechar='|')
    reader1998 = csv.reader(csvfile_1998_wordList, delimiter=' ', quotechar='|')
    reader1999 = csv.reader(csvfile_1999_wordList, delimiter=' ', quotechar='|')
    reader2000 = csv.reader(csvfile_2000_wordList, delimiter=' ', quotechar='|')
    reader2001 = csv.reader(csvfile_2001_wordList, delimiter=' ', quotechar='|')
    reader2002 = csv.reader(csvfile_2002_wordList, delimiter=' ', quotechar='|')
    reader2003 = csv.reader(csvfile_2003_wordList, delimiter=' ', quotechar='|')
    reader2004 = csv.reader(csvfile_2004_wordList, delimiter=' ', quotechar='|')
    reader2005 = csv.reader(csvfile_2005_wordList, delimiter=' ', quotechar='|')
    reader2006 = csv.reader(csvfile_2006_wordList, delimiter=' ', quotechar='|')
    reader2007 = csv.reader(csvfile_2007_wordList, delimiter=' ', quotechar='|')
    reader2008 = csv.reader(csvfile_2008_wordList, delimiter=' ', quotechar='|')
    reader2009 = csv.reader(csvfile_2009_wordList, delimiter=' ', quotechar='|')
    reader2010 = csv.reader(csvfile_2010_wordList, delimiter=' ', quotechar='|')
    reader2011 = csv.reader(csvfile_2011_wordList, delimiter=' ', quotechar='|')
    reader2012 = csv.reader(csvfile_2012_wordList, delimiter=' ', quotechar='|')
    reader2013 = csv.reader(csvfile_2013_wordList, delimiter=' ', quotechar='|')
    reader2014 = csv.reader(csvfile_2014_wordList, delimiter=' ', quotechar='|')
    reader2015 = csv.reader(csvfile_2015_wordList, delimiter=' ', quotechar='|')
    reader2016 = csv.reader(csvfile_2016_wordList, delimiter=' ', quotechar='|')

    DFCOUNT = [0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 0]

    wordDFCOUNTFound = False

    print(
        "===================================================== COMPARING NEW WORD ===================================: " + HPPword + " HPPkey: " + str(
            HPPkey))
    '''
    for key in HPPwordList.keys():
        
        if key > HPPkey:
            break
        if HPPkey == key:
            break
        if wordDFCOUNTFound == False and HPPkey != key:
            print("ENTERING IF STATEMENT")
            for word in HPPwordList[key]:
                #print(word[0])
                #w = word[0]
                #print("--------------WORD [0]: " + str(word) + " and HPPWORD: " + str(HPPword))
                if word[0] == HPPword:
                    print("PREVIOUS DFCOUNT OF WORD FOUND --- SKIPPING LONG SEARCH PROCESS ================ WORD[0]:" + str(word[0]) + " and HPPWORD: " + str(HPPword))
                    wordDFCOUNTFound = True
                    DFCOUNT = word[1]
                    break
    '''
    # print ("DIDNT FIND WORD IN PREVIOUS KEYS    _#$&*#%(_)@#$*_)@(#$*%  LOOKING THROUGH THE WHOLE PATENT LIST OF 9501 PATENTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    if wordDFCOUNTFound is False:  # DFCOUNT != [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
        for HPP in reader1989:

            for word in HPP:
                word = word.replace(",", "")  # ???

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[0] = DFCOUNT[0] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1990:

            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[1] = DFCOUNT[1] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1991:

            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[2] = DFCOUNT[2] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1992:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[3] = DFCOUNT[3] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1993:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[4] = DFCOUNT[4] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1994:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[5] = DFCOUNT[5] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1995:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[6] = DFCOUNT[6] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1996:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[7] = DFCOUNT[7] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1997:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[8] = DFCOUNT[8] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1998:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[9] = DFCOUNT[9] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader1999:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[10] = DFCOUNT[10] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2000:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[11] = DFCOUNT[11] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2001:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[12] = DFCOUNT[12] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2002:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[13] = DFCOUNT[13] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2003:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[14] = DFCOUNT[14] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2004:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[15] = DFCOUNT[15] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2005:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[16] = DFCOUNT[16] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2006:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[17] = DFCOUNT[17] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2007:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[18] = DFCOUNT[18] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2008:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[19] = DFCOUNT[19] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)
        '''
        for HPP in reader2009:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[20] = DFCOUNT[20] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)
        '''

        for HPP in reader2010:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[21] = DFCOUNT[21] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2011:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[22] = DFCOUNT[22] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2012:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[23] = DFCOUNT[23] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2013:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[24] = DFCOUNT[24] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2014:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[25] = DFCOUNT[25] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2015:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[26] = DFCOUNT[26] + 1
                    # print("NEW DF COUNT: ")
                    # print(DFCOUNT)

        for HPP in reader2016:
            for word in HPP:
                word = word.replace(",", "")

                if word == HPPword:
                    # print("======= COMPARING: " + HPPword + " and: " + word)
                    DFCOUNT[27] = DFCOUNT[27] + 1
                    ##print("NEW DF COUNT: ")
                    # print(DFCOUNT)

    # DFCOUNT = str(DFCOUNT.replace(",", " - "))




    csvfile_1989_wordList.close()
    csvfile_1990_wordList.close()
    csvfile_1991_wordList.close()
    csvfile_1992_wordList.close()
    csvfile_1993_wordList.close()
    csvfile_1994_wordList.close()
    csvfile_1995_wordList.close()
    csvfile_1996_wordList.close()
    csvfile_1997_wordList.close()
    csvfile_1998_wordList.close()
    csvfile_1999_wordList.close()
    csvfile_2000_wordList.close()
    csvfile_2001_wordList.close()

    PatCOUNT = [49, 68, 81, 85, 107,
                100, 124, 103, 96, 95,
                127, 219, 287, 263, 254,
                199, 172, 176, 179, 183,
                247, 427, 739, 961, 1106,
                1457, 1086, 430]

    # print(DFCOUNT)
    i = 0
    for df in DFCOUNT:
        DFCOUNT[i] = float(DFCOUNT[i] / PatCOUNT[i]) * 100

        i += 1
    # print(DFCOUNT)

    return DFCOUNT
