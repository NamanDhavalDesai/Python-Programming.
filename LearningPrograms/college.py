from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
driver = webdriver.Chrome('C:/bin/chromedriver.exe')
course_name=[]
cost=[]
cost_type=[]
duration=[]
university=[]
location=[]
extrafacts=[]
for loop1 in range(659,660):#659
    if loop1==1:
        driver.get('https://www.mastersportal.com/search/#q=di-24|lv-master')
    else:
        driver.get('https://www.mastersportal.com/search/#q=di-24|lv-master|tc-EUR&start='+str(loop1-1)+'0')
    html = driver.page_source
    soup = BeautifulSoup(html)
    for tag in soup.find_all("span",class_="Fact KeyFact"):
        tag=tag.text
        cost.append(tag[1:tag.find('/')-1].replace(',',''))
        cost_type.append(tag[tag.find('/')+1:len(tag)].replace(' ',''))
    for tag in soup.find_all("span",class_="js-duration"):
        tag=tag.text
        duration.append(tag)
    for tag in soup.find_all("h3",class_="StudyTitle"):
        tag=tag.text
        course_name.append(tag[1:len(tag)-1])
    ctr1=1
    for tag in soup.find_all("span",class_="Fact LocationFact"):
        tag=tag.text
        if ctr1%2==1:
            university.append(tag)
        else:
            location.append(tag)
        ctr1=ctr1+1
    for tag in soup.find_all("div",class_="ExtraFacts"):
        tag=tag.text
        tag=tag[1:len(tag)-1]
        extrafacts.append(tag)
    print(loop1)
print('----------------------------------')
data={'Course Name':course_name,'University':university,'Location':location,'Cost':cost,'Cost per':cost_type,'Duration':duration,'Extra':extrafacts}
data=pandas.DataFrame(data)
print(data)
data.to_csv('MastersCollege.csv', mode='a', header=False)
#data.to_csv('MastersCollege.csv')
driver.close()
driver.quit()