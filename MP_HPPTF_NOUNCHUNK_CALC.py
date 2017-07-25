from __future__ import division
from __future__ import print_function

import csv

from spacy.en import English

#import PyPDF2
#import docx


nlp = English()
csvfile = open('(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS ORIGINAL.csv', 'r')
reader = csv.reader(csvfile, delimiter=',', quotechar=',')

store_chunks_str_FullParent = []

csvfile_ouput = open('(03)DSSC_9501 PatSnap v.02 HPP List ONLY HPP only patnum RESULTS WORDS TF ORIGINAL.csv', 'w+')
writer_yearoutput = csv.writer(csvfile_ouput, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
test=0
for pat in reader:
    test +=1
    textVocabs = {}
    textVocabsAscending1 = []
    totalNCinDoc = 0
    
    for word in pat:
        word = word.lstrip(' ').lower()
        textVocabs[word] = textVocabs.get(word, 0) + 1
        totalNCinDoc +=1
    textVocabs_items = textVocabs.items()
    textVocabs_items = list(textVocabs_items)
    
    x=0
    for items in textVocabs_items:
        items = list(items)
        items[1] = float(items[1] / totalNCinDoc)
        items = tuple(items)
        textVocabs_items[x] = items
        x+=1
    textVocabsAscending = sorted(textVocabs_items, key= lambda x: x[1]*-1)   
    
    for vocab in textVocabsAscending:   #JOINING VOCAB WITH FREQUENCY 'VOCAB: FREQ'
        textVocabsAscendingItem = ":".join([str(vocab[0]), str(vocab[1])]) #/ len(textVocabsAscending)
        textVocabsAscending1.append(textVocabsAscendingItem)

    #for word in textVocabsAscending1:
    outputText = str(textVocabsAscending1)
    print(outputText)
    writer_yearoutput.writerow(outputText.split(","))   
    
csvfile.close()
csvfile_ouput.close()
