
import requests
from bs4 import BeautifulSoup as bss4
import csv

url = requests.get("https://kafiil.com/projects")

soup = bss4 ( url.text,'lxml')
#jobs_title= soup.findAll('p', {'class':'name mb-1'})
#print (jobs_title)
projects = soup.findAll('div',{'class':'project-box active'})
with open('project.csv','w',encoding = 'utf-8' ,newline='')as file :
    writer = csv.writer (file)
    writer.writerow(['project name', ' price'])

    for project in projects :
       info = project.find('div','info').text
       price=project.find('p','price').text
       writer.writerow([info,price])

print ('done')
