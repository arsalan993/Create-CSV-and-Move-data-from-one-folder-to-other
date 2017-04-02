import csv
from itertools import izip_longest
import shutil
import os

#add your path here
path = 'E:\excelfile\excelfile/'

#Data recieved after clustering of images
d = [['1.bmp','2.bmp','3.bmp'],['4.bmp','5.bmp','6.bmp','7.bmp','8.bmp'],['9.bmp','10.bmp','11.bmp','12.bmp','13.bmp','14.bmp']]
all = []
for values in izip_longest(*d):
    all.append(values)
with open('file2.csv','w+') as csvoutput:   
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerow(('0', '1', '2'))
    writer.writerows(all)
    csvoutput.close()

count = 0
name = []
#Now arranging data
with open('file2.csv','r') as inputcsv:   
    reader = csv.reader(inputcsv)
    for row in reader:
        print row
        if count == 0:
            name = row
            for i in range(len(row)):
                os.makedirs(str(row[i]))
            
        if count != 0:
            for j in range(len(row)):
                if len(row[j]) > 0:
                       shutil.move(path + 'unknown/' + str(row[j]),path + str(name[j]))
            
        count = count + 1

        
        
