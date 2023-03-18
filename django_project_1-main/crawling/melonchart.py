import re
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/"

headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url,headers = headers)
res.raise_for_status()
soup  = BeautifulSoup(res.text,'lxml')

titles = soup.find('table').find("tbody").find_all("tr",attrs={"class":re.compile("^lst")})

my_dict={}
for n,title in enumerate(titles,start=1):
    t = title.find("div",attrs={"class":"ellipsis rank01"}).a.get_text()
    author = title.find("div",attrs={"class":"ellipsis rank02"}).a.get_text()
    my_dict[t]=author

#my_dict = {key[i]:value[i] for i in range(len(key))}
#for key, value in my_dict.items():
#print(my_dict.items())
song = list(my_dict.keys())
artict = list(my_dict.values())

     




