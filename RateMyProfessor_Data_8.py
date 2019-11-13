from bs4 import BeautifulSoup
import requests
import csv



csv_file = open('RMP_DATA_8.csv','w')
csv_url = open('RMP_URLs_8.csv','r')


csv_writer = csv.writer(csv_file, lineterminator = '\n')
csv_reader = csv.reader(csv_url)




def department():
    try:    
        department=soup.find('div', class_='result-title').text
        department = department.split("Professor in the")
        department = department[1].split("department") 
    except Exception as e:
            department = 'Not Found'
    return department[0].strip()

def school():
    try:    
        school=soup.find('a', class_='school').text
    except Exception as e:
            school = 'Not Found'
    return school

def city():
    try:    
        city=soup.find('h2', class_='schoolname').text
        city=city.split(",",1)
    except Exception as e:
            city = 'Not Found'
    return city[1].strip()

def quality():
    try:    
        quality=soup.find('div', class_='grade').text
    except Exception as e:
            quality = 'Not Found'
    return quality

def difficulty():
    try:    
        difficulty=soup.find('div', class_='breakdown-section difficulty').div.text
    except Exception as e:
            difficulty = 'Not Found'
    return difficulty.strip()

def repeat():
    try:    
        repeat=soup.find_all('div', class_='grade')
        repeat=repeat[1].text
    except Exception as e:
            repeat = ("N/A")
    return repeat.strip()

def tags():
    try:    
        tags=soup.find('div', class_='tag-box').text
        tags=tags.strip()
        tags=tags.split("\n")
    except Exception as e:
            tags = 'Not Found'
    return tags

def ratings():
    try:    
        ratings=soup.find('div', class_='table-toggle rating-count active').text
        ratings=ratings.replace('Student Ratings','')
    except Exception as e:
            ratings = 'Not Found'
    return ratings.strip()

def write():
    csv_writer.writerow([department(),school(),city(),quality(),difficulty(),repeat(),tags(),ratings(),rmp_data])
    print([department(),school(),city(),quality(),difficulty(),repeat(),tags(),ratings(),rmp_data])

for line in csv_reader:
    line=str(line).split("'")
#for line in range(1,2):
    rmp_data = f'https://www.{line[1]}'
    #rmp_data = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=87101'    
    source = requests.get(rmp_data).text
    soup = BeautifulSoup(source, 'lxml')  
    check = soup.find('body', class_='show_professor')
    if check:
        write()
    else:
        csv_writer.writerow(['No Data','No Data','No Data','No Data','No Data','No Data','No Data','No Data','No Data','No Data'])
        print(['No Data','No Data','No Data','No Data','No Data','No Data','No Data','No Data','No Data','No Data'])

  
csv_file.close()
csv_url.close()
