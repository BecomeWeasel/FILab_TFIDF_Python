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

    csvfile = open('1976.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[0] = DFCOUNT[0] + 1
                break

    csvfile.close()

    csvfile = open('1977.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[1] = DFCOUNT[1] + 1
                break

    csvfile.close()

    csvfile = open('1978.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[2] = DFCOUNT[2] + 1
                break

    csvfile.close()

    csvfile = open('1979.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[3] = DFCOUNT[3] + 1
                break

    csvfile.close()

    csvfile = open('1980.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[4] = DFCOUNT[4] + 1
                break

    csvfile.close()

    csvfile = open('1981.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[5] = DFCOUNT[5] + 1
                break

    csvfile.close()

    csvfile = open('1982.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[6] = DFCOUNT[6] + 1
                break

    csvfile.close()

    csvfile = open('1983.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[7] = DFCOUNT[7] + 1
                break

    csvfile.close()

    csvfile = open('1984.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[8] = DFCOUNT[8] + 1
                break

    csvfile.close()

    csvfile = open('1985.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[9] = DFCOUNT[9] + 1
                break

    csvfile.close()

    csvfile = open('1996.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[20] = DFCOUNT[20] + 1
                break

    csvfile.close()


def DFCALCbackward(word, DFCOUNT):
    csvfile = open('2006.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[30] = DFCOUNT[30] + 1
                break

    csvfile.close()

    csvfile = open('2007.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[31] = DFCOUNT[31] + 1
                break

    csvfile.close()

    csvfile = open('2008.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[32] = DFCOUNT[32] + 1
                break

    csvfile.close()

    csvfile = open('2009.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[33] = DFCOUNT[33] + 1
                break

    csvfile.close()

    csvfile = open('2010.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[34] = DFCOUNT[34] + 1
                break

    csvfile.close()

    csvfile = open('2011.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[35] = DFCOUNT[35] + 1
                break

    csvfile.close()

    csvfile = open('2012.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[36] = DFCOUNT[36] + 1
                break

    csvfile.close()

    csvfile = open('2013.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[37] = DFCOUNT[37] + 1
                break


def DFCALC3(word, DFCOUNT):
    csvfile = open('1986.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[10] = DFCOUNT[10] + 1
                break

    csvfile.close()

    csvfile = open('1987.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[11] = DFCOUNT[11] + 1
                break

    csvfile.close()

    csvfile = open('1988.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[12] = DFCOUNT[12] + 1
                break

    csvfile.close()

    csvfile = open('1989.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[13] = DFCOUNT[13] + 1
                break

    csvfile.close()

    csvfile = open('1990.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[14] = DFCOUNT[14] + 1
                break

    csvfile.close()

    csvfile = open('1991.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[15] = DFCOUNT[15] + 1
                break

    csvfile.close()

    csvfile = open('1992.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[16] = DFCOUNT[16] + 1
                break

    csvfile.close()

    csvfile = open('1993.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[17] = DFCOUNT[17] + 1
                break

    csvfile.close()

    csvfile = open('1994.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[18] = DFCOUNT[18] + 1
                break

    csvfile.close()

    csvfile = open('1995.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')

    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[19] = DFCOUNT[19] + 1
                break

    csvfile.close()


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


def DFCHECK(setStart, setEnd):
    ERRORINPUT = open(
        '(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS DF FULL ORIGINAL each word in one row FINAL v0.3 unifying duplicates.csv',
        'rU')
    reader = csv.reader(ERRORINPUT, delimiter=',', quotechar=',')
    ValidOutput = open(
        '(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS DF FULL ORIGINAL each word in one row FINAL v0.3 unifying duplicates ' + str(
            setStart) + ' to ' + str(setEnd) + '.csv', 'w+')
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
        firstDF = 0  # firstDF is compared with word_DFCOUNTsStore[5],which is old DFCOUNT of 1980 in inputfile.
        secondDF = 0  # secondDF is similar to firstDF.
        thirdDF = 0  # thirdDF is similar to firstDF.
        isError = False  # if isError boolean value is true,then,word in row have invalid DFCOUNT value.

        print("checking for words : " + word_DFCOUNTsStore[0])

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

    p1 = Process(target=DFCALCforward, args=(word_DFCOUNTs[0], DFCOUNT))
    p2 = Process(target=DFCALCbackward, args=(word_DFCOUNTs[0], DFCOUNT))
    p3 = Process(target=DFCALC3, args=(word_DFCOUNTs[0], DFCOUNT))
    p4 = Process(target=DFCALC4, args=(word_DFCOUNTs[0], DFCOUNT))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    DFCOUNTRETURN = []
    DFCOUNTRETURN = DFCOUNT[:]
    return DFCOUNTRETURN


totalErrorCount = DFCHECK(18022, 18023)  # First parameter is starting word and second one is end word.
