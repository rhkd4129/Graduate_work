import re
from turtle import title
import requests
from bs4 import BeautifulSoup
#https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN246&page=3
url = 'https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN246&page=1'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

#stitle

titles  = soup.find_all('p',attrs={"class":"stitle"})

for title in titles: 
    print(title.a.get_text())