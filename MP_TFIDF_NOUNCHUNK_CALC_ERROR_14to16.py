from __future__ import division
from __future__ import print_function
'''
Created on 2017.8.8

'''
import csv
from multiprocessing import Process, Array
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def DFCALC1(word, DFCOUNT):
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
    csvfile = open('2014.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[38] = DFCOUNT[38] + 1
                break

    csvfile.close()



def DFCALC2(word, DFCOUNT):

    word = word.lower()
    csvfile = open('2015.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[39] = DFCOUNT[39] + 1
                break

    csvfile.close()


def DFCALC3(word, DFCOUNT):

    word = word.lower()
    csvfile = open('2016.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[40] = DFCOUNT[40] + 1
                break

    csvfile.close()

'''
def DFCALC4(word, DFCOUNT):
    csvfile = open('1997.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[21] = DFCOUNT[21] + 1
                break

    csvfile.close()

    csvfile = open('1998.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[22] = DFCOUNT[22] + 1
                break

    csvfile.close()

    csvfile = open('1999.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[23] = DFCOUNT[23] + 1
                break
    csvfile.close()

    csvfile = open('2000.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[24] = DFCOUNT[24] + 1
                break
    csvfile.close()

    csvfile = open('2001.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[25] = DFCOUNT[25] + 1
                break
    csvfile.close()

    csvfile = open('2002.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[26] = DFCOUNT[26] + 1
                break
    csvfile.close()

    csvfile = open('2003.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[27] = DFCOUNT[27] + 1
                break
    csvfile.close()

    csvfile = open('2004.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[28] = DFCOUNT[28] + 1
                break
    csvfile.close()

    csvfile = open('2005.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[29] = DFCOUNT[29] + 1
                break
    csvfile.close()
'''

def DFCHECK(setStart, setEnd):
    ERRORINPUT = open(
        '(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS DF FULL ORIGINAL each word in one row FINAL v0.3 unifying duplicates.csv',
        'rU')
    reader = csv.reader(ERRORINPUT, delimiter=',', quotechar=',')
    ValidOutput = open(
        '(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS DF FULL ORIGINAL each word in one row FINAL v0.3 unifying duplicates ' + str(
            setStart) + ' to ' + str(setEnd) + ' only 14 to 16.csv', 'w+')
    writer_OUTPUT = csv.writer(ValidOutput, delimiter=',', quotechar=',')

    targetWordIdx = 0
    errorCountInRange = 0

    for wordAndDFCounts in reader:
        targetWordIdx += 1

        if targetWordIdx < setStart:  # Pointer of DFCHECK not reached startpoint yet.
            continue

        if targetWordIdx > setEnd:  # Works done in range of setstart~setend.
            return errorCountInRange

        word_DFCOUNTsStore = []
        word_DFCOUNTsStore = wordAndDFCounts
        word_DFCOUNTsStore[0] = word_DFCOUNTsStore[0].lstrip(
            ' ')  # word_DFCOUNTsStore is word that needed to be checked.

        DFCountStore = []
        outputText = []
        # firstDF = 0  # firstDF is compared with word_DFCOUNTsStore[5],which is old DFCOUNT of 1980 in inputfile.
        # secondDF = 0  # secondDF is similar to firstDF.
        # thirdDF = 0  # thirdDF is similar to firstDF.
        # isError = False  # if isError boolean value is true,then,word in row have invalid DFCOUNT value.

        '''print("checking for words : " + word_DFCOUNTsStore[0])

        csv_1980 = open('1980.csv', 'rU')
        reader1980 = csv.reader(csv_1980, delimiter=',', quotechar=',')
        for patent_1980 in reader1980:
            for patword_1980 in patent_1980:
                patword_1980 = patword_1980.lower().lstrip(' ')
                if str(patword_1980) == str(word_DFCOUNTsStore[0]):
                    firstDF = firstDF + 1
                    break
        csv_1980.close()

        print("compared with old : " + word_DFCOUNTsStore[5] + " , " + str(firstDF))

        if firstDF != int(word_DFCOUNTsStore[5]):
            # check old DFCOUNT. If it is invalid, DFCALC procedure will be called.
            print("Error at " + word_DFCOUNTsStore[0] + " in 1980")  # Tell user to old DFCOUNT is invalid.
            isError = True  # Set error occur value to true.
            DFCountStore = DFCALC(word_DFCOUNTsStore)  # So to correct invalid DFCOUNT, call DFCALC.

        elif firstDF == int(word_DFCOUNTsStore[5]):
            print("No error at " + word_DFCOUNTsStore[0] + " in 1980")

        csv_2000 = open('2000.csv', 'rU')
        reader2000 = csv.reader(csv_2000, delimiter=',', quotechar=',')
        for patent_2000 in reader2000:
            for patword_2000 in patent_2000:
                patword_2000 = patword_2000.lower().lstrip(' ')
                if str(patword_2000) == str(word_DFCOUNTsStore[0]):
                    secondDF = secondDF + 1
                    break
        csv_2000.close()

        print("compared with old : " + word_DFCOUNTsStore[25] + " , " + str(secondDF))

        if secondDF != int(word_DFCOUNTsStore[25]) and isError is False:
            # check old DFCOUNT. If it is invalid, DFCALC procedure will be called.
            # And if isError is True, it means that DFCALC was already called, so don't need to do that again.
            print("Error at " + word_DFCOUNTsStore[0] + " in 2000")  # Tell user to old DFCOUNT is invalid.
            isError = True  # Set error occur value to true.
            DFCountStore = DFCALC(word_DFCOUNTsStore)  # So to correct invalid DFCOUNT, call DFCALC.

        elif secondDF != int(word_DFCOUNTsStore[25]) and isError is True:
            print("Error at " + word_DFCOUNTsStore[0] + " in 2000 but correction already done.")

        elif secondDF == int(word_DFCOUNTsStore[25]):
            print("No error at " + word_DFCOUNTsStore[0] + " in 2000")

        csv_2011 = open('2011.csv', 'rU')
        reader2011 = csv.reader(csv_2011, delimiter=',', quotechar=',')
        for patent_2011 in reader2011:
            for patword_2011 in patent_2011:
                patword_2011 = patword_2011.lower().lstrip(' ')
                if str(patword_2011) == str(word_DFCOUNTsStore[0]):
                    thirdDF = thirdDF + 1
                    break
        csv_2011.close()

        print("compared with old : " + word_DFCOUNTsStore[36] + " , " + str(thirdDF))

        if thirdDF != int(word_DFCOUNTsStore[36]) and isError is False:
            # check old DFCOUNT. If it is invalid, DFCALC procedure will be called.
            # And if isError is True, it means that DFCALC was already called, so don't need to do that again.
            print("Error at " + word_DFCOUNTsStore[0] + " in 2010")  # Tell user to old DFCOUNT is invalid.
            isError = True  # Set error occur value to true.
            DFCountStore = DFCALC(word_DFCOUNTsStore)  # So to correct invalid DFCOUNT, call DFCALC.

        elif thirdDF != int(word_DFCOUNTsStore[36]) and isError is True:
            print("Error at " + word_DFCOUNTsStore[0] + " in 2010 but correction already done.")

        elif thirdDF == int(word_DFCOUNTsStore[36]):
            print("No error at " + word_DFCOUNTsStore[0] + " in 2010")

        if isError is True:
            # if isError value is true ,it means that fucn DFCALC was called.
            # so old and invalid DFCOUNT in word_DFCOUNT sholud be changed.
            for i in range(1, 42):
                word_DFCOUNTsStore[i] = DFCountStore[i - 1]
            errorCountInRange += 1
        '''
        DFCountStore=DFCALC(word_DFCOUNTsStore)

        for i in range(1, 42):
            word_DFCOUNTsStore[i] = DFCountStore[i - 1]


        DFCOUNTtext = str(word_DFCOUNTsStore[1:])
        output = ",".join([str(word_DFCOUNTsStore[0]), str(DFCOUNTtext)])
        outputText.append(output)

        outputText = str(outputText)
        writer_OUTPUT.writerow(outputText.split(","))

        print("Invalid DFCOUNT correction of " + str(targetWordIdx) + " is done,\n\n")

    ValidOutput.close()
    ERRORINPUT.close()


def DFCALC(word_DFCOUNTs):
    DFCOUNT = Array('i', 41)

    p1 = Process(target=DFCALC1, args=(word_DFCOUNTs[0], DFCOUNT))
    p2 = Process(target=DFCALC2, args=(word_DFCOUNTs[0], DFCOUNT))
    p3 = Process(target=DFCALC3, args=(word_DFCOUNTs[0], DFCOUNT))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    DFCOUNTRETURN = []
    DFCOUNTRETURN = DFCOUNT[:]
    return DFCOUNTRETURN


totalErrorCount = DFCHECK(1, 1700)  # First parameter is starting word and second one is end word.
