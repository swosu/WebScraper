import csv
import re

with open('RMP_DATA_Total_Unique_test.csv', 'r') as f:
    csv_reader = csv.reader(f)
    with open('Tags.csv','r') as r:
        csv_tags = csv.reader(r)
        for line in csv_reader:
            tags = line[6]
            tags = tags[1:-1]
            print(tags)
            print("____________________________________________________")
