from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('RMP_URLs_6.csv','w')

csv_writer = csv.writer(csv_file, lineterminator = '\n')
offset = 50000*20
count = 0
#83773+1
for x in range(0,10001):        
    rmp_listings = f'https://www.ratemyprofessors.com/search.jsp?query=&queryoption=HEADER&stateselect=&country=&dept=&queryBy=teacherName&facetSearch=&schoolName=&offset={offset}&max=20'
    source = requests.get(rmp_listings).text
    soup = BeautifulSoup(source, 'lxml')
    offset += 20 
    for listing in soup.find_all('li', class_='listing PROFESSOR'):
        try:
            url = listing.a['href']
            rmp_url = f'ratemyprofessors.com{url}'
        except Exception as e:
            rmp_url = 'Professor Not Found'        
        csv_writer.writerow([rmp_url])
        count += 1
        print( count,"     ",rmp_url)

    
    
csv_file.close()