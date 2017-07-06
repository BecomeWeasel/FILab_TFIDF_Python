import os.path
import csv

csvfile = open('(03)DSSC_9501 PatSnap v.012 as matlab input.csv', 'r+')
#savefile = open('', 'w')

reader = csv.reader(csvfile, delimiter=',', quotechar='|')


prevpatentyear = 0
thispatentyear = 0
patentlist = []

for patent in reader:
    #for patentYear in patent:

    
    
    print(patent)
    if prevpatentyear == 0:
        prevpatentyear = patent[2]
    
    thispatentyear = patent[2]
    
    if thispatentyear == prevpatentyear:
        patentlist.append(patent[0])

    if thispatentyear != prevpatentyear:
        
        newFileName=''.join(['(03)DSSC_9501 PatSnap v.02 ', prevpatentyear, ' Patent for yearly keyword extraction.csv'])
        
        savefile = open(newFileName, 'w')
        writer = csv.writer(savefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(patentlist)
        savefile.close()
        
        patentlist = []
        patentlist.append(patent[0])
        prevpatentyear = thispatentyear

newFileName=''.join(['(03)DSSC_9501 PatSnap v.02 ', prevpatentyear, ' Patent for yearly keyword extraction.csv'])
        
savefile = open(newFileName, 'w')
writer = csv.writer(savefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(patentlist)
savefile.close()