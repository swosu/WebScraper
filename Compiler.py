import csv
with open('Compiled_Data', 'w', newline='') as w:
    csv_compiled = csv.writer(w)
    
    with open('RMP_DATA_Total_Unique.csv', 'r') as f:
        csv_data = csv.reader(f)
        data = list(csv_data)
        with open('RMP_DATA_TAGS_Count.csv','r') as r:
                csv_tags = csv.reader(r)
                tags = list(csv_tags)
                n=0
                for k in range(5):       
                    L1 = []    
                    data1=[row for idx, row in enumerate(data) if idx == n]
                    for d in data1:
                        for d2 in d:
                            L1.append(d[d2])
                    
                    tags1=[row for idx, row in enumerate(tags) if idx == n]
                    for t in tags1:
                        for t2 in t:
                            L1.append(t[t2])
                    #out = data1, ', ', tags1
                    n+=1
                    print(L1)
                    print()
                    csv_compiled.writerow(L1)