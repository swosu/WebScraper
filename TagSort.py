import os
import csv
import re

tagList=[]

with open('RMP_DATA_Total_Unique.csv', 'r') as f:
    csv_data = csv.reader(f)
    with open('RMP_DATA_TAGS_Count.csv', 'w', newline='') as w:
        csv_tagCount = csv.writer(w)
        for line in csv_data:
            tags = line[6] #selects tag section
            tags = tags[1:-1] #trims bracates
            tags = tags.split(',')
            tags.sort(key=lambda x: ''.join(x.split()).strip('"\''))
            ",".join(tags)
            tags = str(tags)
            stopIndex=0
            #print(tags)
            #print("did")
            with open('Tags.csv','r') as r:
                csv_tags = csv.reader(r)
                for row in csv_tags:
                    #print("did something")
                    #print(row)
                    stop = [(m.end()) for m in re.finditer('\)', tags)]#finds the index for the stop point
                    tagStart = tags.find(''.join(str(row)[2:-2])) #find the tag index start point   

                    if tagStart > 0:
                        tag1 = tags[tagStart:stop[stopIndex]]
                        stopIndex+=1                     
                        tag2 = tag1.split()
                        tag3= str(tag2[-1:])
                        tagf=tag3[3:-2].strip('()')
                        #print(tagStart, stop, stopIndex)
                        #print(tag1)
                    else:
                        tagf=0                
                    tagList.append(tagf)                   
            print(tagList)
            csv_tagCount.writerow(tagList)
            #print()
            tagList=[]