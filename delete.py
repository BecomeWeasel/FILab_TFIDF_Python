import csv
import os


def delete(targetyear, count):
    csv.field_size_limit(500 * 1024 * 1024)
    directory = os.getcwd()
    directory += "/Patents/"
    tmp = []
    csvfile = open(directory + str(targetyear) + '.csv', 'r')
    csvfile_output = open(directory + str(targetyear) + ' ver2.csv', 'w+')

    readercsvifle = csv.reader(csvfile, delimiter=' ',quotechar='|')
    writercsvfileoutput = csv.writer(csvfile_output, delimiter=',', quotechar=',', quoting=csv.QUOTE_NONE)

    i = 1

    for WORDS in readercsvifle:
        if i == count+1 :
            print("end")
            return None
        if i % 2 == 0 :
            i+=1
            continue
        tmp.append(WORDS)
        i+=1

    for INPUT in tmp:
        INPUT=str(INPUT)
        writercsvfileoutput.writerow(INPUT.split(","))

    csvfile_output.close()
    csvfile.close()


delete(1985,629)