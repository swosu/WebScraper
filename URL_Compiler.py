

csv_file1 = open('RMP_DATA_1.csv','r')
csv_file2 = open('RMP_DATA_2.csv','r')
csv_file3 = open('RMP_DATA_3.csv','r')
csv_file4 = open('RMP_DATA_4.csv','r')
csv_file5 = open('RMP_DATA_5.csv','r')
csv_file6 = open('RMP_DATA_6.csv','r')
csv_file7 = open('RMP_DATA_7.csv','r')
csv_file8 = open('RMP_DATA_8.csv','r')
csv_file = open('RMP_DATA_Total.csv','w')



csv_read = [csv_file1,csv_file2,csv_file3,csv_file4,csv_file5,csv_file6,csv_file7,csv_file8]



for file in csv_read:
    for line in file:
        csv_file.write(line)
        print (line)

csv_file1.close()
csv_file2.close()
csv_file3.close()
csv_file4.close()
csv_file5.close()
csv_file6.close()
csv_file7.close()
csv_file8.close()
csv_file.close()
