import csv
import sys
import shutil
f = open('eggs.csv', 'wb')
try:
    writer = csv.writer(f)
    writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
    for i in range(10):
        writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
finally:
    f.close()

    with open('eggs.csv','r') as csvinput:
        reader = csv.reader(csvinput)
        all = []
        row = reader.next()
        row.append('Title 4')
        print row
        all.append(row)
        for row in reader:
            print row
            row.append(row[0])
            all.append(row)
       
        

        print all
        csvinput.close()
        with open('eggs.csv','w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            writer.writerows(all)
            csvoutput.close()
        with open('eggs.csv','r') as csvinput:
            r = csv.reader(csvinput)
            lines = [l for l in r]
            print type(lines)
            print lines
            lines[2][1] = '30'
            csvinput.close()
        with open('eggs.csv','w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            writer.writerows(lines)
            csvoutput.close()
        shutil.move('C:/Users/Arsla/Desktop/excelfile/folder1/2.bmp','C:/Users/Arsla/Desktop/excelfile/folder2')
        

##        with open('eggs.csv', 'a+') as csvfile:
##            fieldnames = ['Title 2', 'Title 3']
##            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
##            writer.writeheader()
##            writer.writerow({'Title 2': 'Baked', 'Title 3': 'Beans'})
##            writer.writerow({'Title 2': 'Lovely', 'Title 3': 'Spam'})
##            writer.writerow({'Title 3': 'Spam'})
##            csvfile.close()



    #print "all done"
