import csv
from itertools import zip_longest

d = [[2,3,4,8],[5,6],[2,5,7,4,2,5,78,8,3,2,46]]
all = []
##with open("file.csv","w+") as f:
##writer = csv.writer(f)
##writer.writerow( ('Title 1', 'Title 2', 'Title 3') )

for values in zip_longest(*d):
    #writer.writerow(values)
    all.append(values)
    #f.close()
with open('file.csv','w+') as csvoutput:
    
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerow(('Title 1', 'Title 2', 'Title 3'))
    writer.writerows(all)
    csvoutput.close()
