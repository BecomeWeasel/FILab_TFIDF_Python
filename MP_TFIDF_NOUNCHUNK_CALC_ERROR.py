from __future__ import division
from __future__ import print_function

import csv
import multiprocessing
from multiprocessing import Process


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
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[0] = DFCOUNT[0] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1977.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[1] = DFCOUNT[1] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1978.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[2] = DFCOUNT[2] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1979.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[3] = DFCOUNT[3] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1980.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[4] = DFCOUNT[4] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1981.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[5] = DFCOUNT[5] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1982.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[6] = DFCOUNT[6] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1983.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[7] = DFCOUNT[7] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1984.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[8] = DFCOUNT[8] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1985.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[9] = DFCOUNT[9] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1996.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[20] = DFCOUNT[20] + 1
                break
    # print(DFCOUNT)
    csvfile.close()


def DFCALCbackward(word, DFCOUNT):
    csvfile = open('2006.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[30] = DFCOUNT[30] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2007.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[31] = DFCOUNT[31] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2008.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[32] = DFCOUNT[32] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2009.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[33] = DFCOUNT[33] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2010.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[34] = DFCOUNT[34] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2011.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[35] = DFCOUNT[35] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2012.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[36] = DFCOUNT[36] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2013.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[37] = DFCOUNT[37] + 1
                break


def DFCALC3(word, DFCOUNT):
    csvfile = open('1986.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[10] = DFCOUNT[10] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1987.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[11] = DFCOUNT[11] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1988.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[12] = DFCOUNT[12] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1989.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[13] = DFCOUNT[13] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1990.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[14] = DFCOUNT[14] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1991.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[15] = DFCOUNT[15] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1992.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[16] = DFCOUNT[16] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1993.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[17] = DFCOUNT[17] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1994.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[18] = DFCOUNT[18] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1995.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[19] = DFCOUNT[19] + 1
                break
    # print(DFCOUNT)
    csvfile.close()


def DFCALC4(word, DFCOUNT):
    csvfile = open('1997.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[21] = DFCOUNT[21] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1998.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[22] = DFCOUNT[22] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('1999.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[23] = DFCOUNT[23] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2000.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[24] = DFCOUNT[24] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2001.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[25] = DFCOUNT[25] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2002.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[26] = DFCOUNT[26] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2003.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[27] = DFCOUNT[27] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2004.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[28] = DFCOUNT[28] + 1
                break
    # print(DFCOUNT)
    csvfile.close()

    csvfile = open('2005.csv', 'rU')
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    # print(word)
    for patent in reader:
        for patword in patent:
            patword = patword.lower().lstrip(' ')
            if str(patword) == str(word):
                DFCOUNT[29] = DFCOUNT[29] + 1
                break
    # print(DFCOUNT)
    csvfile.close()


def DFCHECK(WorkAmount):
    ERRORINPUT = open('INPUTFILENAMEHERE.csv', 'rU')
    reader = csv.reader(ERRORINPUT, delimiter=',', quotechar=',')
    ValidOutput = open('OUTFILENAME.csv', 'rU')
    writer_OUTPUT = csv.writer(ValidOutput, delimiter=',', quotechar=',')
    WorkDone = 0
    for row in reader:
        WorkDone += 1
        if WorkDone == WorkAmount:
            break

        word_DFCOUNTs = []
        word_DFCOUNTs = row
        DFCountStore = []
        outputText = []
        firstDF = 0
        secondDF = 0
        thirdDF = 0
        errorTF = False
        print("checking for words : " + word_DFCOUNTs[0])

        csv_1980 = open('1980.csv', 'rU')
        reader1980 = csv.reader(csv_1980, delimiter=',', quotechar=',')
        for patent in reader1980:
            for patword in patent:
                patword = patword.lower().lstrip(' ')
                if str(patword) == str(word_DFCOUNTs[0]):
                    firstDF = firstDF + 1
                    break
        csv_1980.close()
        if firstDF != word_DFCOUNTs[5]:
            errorTF = True
            DFCountStore = DFCALC(word_DFCOUNTs)

        csv_2000 = open('2000.csv', 'rU')
        reader2000 = csv.reader(csv_2000, delimiter=',', quotechar=',')
        for patent in reader2000:
            for patword in patent:
                patword = patword.lower().lstrip(' ')
                if str(patword) == str(word_DFCOUNTs[0]):
                    secondDF = secondDF + 1
                    break
        csv_2000.close()
        if secondDF != word_DFCOUNTs[25]:
            errorTF = True
            DFCountStore = DFCALC(word_DFCOUNTs)

        csv_2011 = open('2011.csv', 'rU')
        reader2011 = csv.reader(csv_2011, delimiter=',', quotechar=',')
        for patent in reader2011:
            for patword in patent:
                patword = patword.lower().lstrip(' ')
                if str(patword) == str(word_DFCOUNTs[0]):
                    thirdDF = thirdDF + 1
                    break
        csv_2011.close()
        if thirdDF != word_DFCOUNTs[36]:
            errorTF = True
            DFCountStore = DFCALC(word_DFCOUNTs)

        if errorTF is True:
            for i in range(1, 42):
                word_DFCOUNTs[i] = DFCountStore[i - 1]

        DFCOUNTtext = str(word_DFCOUNTs[1:])
        output = ",".join([str(word_DFCOUNTs[0]), str(DFCOUNTtext)])
        outputText.append(output)

        outputText = str(outputText)
        writer_OUTPUT.writerow(outputText.split(","))

    ValidOutput.close()
    ERRORINPUT.close()


def DFCALC(word_DFCOUNTs):
    DFCOUNT = multiprocessing.Array('i', 41)

    p1 = multiprocessing.Process(target=DFCALCforward, args=(word_DFCOUNTs[0], DFCOUNT))
    p2 = multiprocessing.Process(target=DFCALCbackward, args=(word_DFCOUNTs[0], DFCOUNT))
    p3 = multiprocessing.Process(target=DFCALC3, args=(word_DFCOUNTs[0], DFCOUNT))
    p4 = multiprocessing.Process(target=DFCALC4, args=(word_DFCOUNTs[0], DFCOUNT))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    return DFCOUNT


DFCHECK(500)