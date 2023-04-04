from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # 크롭 드라이버 자동 업데이터 

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
from urllib.error import HTTPError,URLError
import time
import urllib.request
import os
import socket
import googletrans
import random
# from .image_preprocessing import cvt_image_save

# 직접 코딩한 함수 임포트 
import requests


############## 한글 입력받으면 번역하는 함수############
def trans(keyword:str)->str:
    # 입력받은 keyword가 한국어면 
    if not 'a' <= keyword[0] <= 'z' or 'A' <= keyword[0] <='Z':
        # 번역 api로 번역 
        translator = googletrans.Translator()
        result = translator.translate(keyword, dest='en')
        print(keyword + " => " + result.text)
        keyword = result.text
        return keyword
    # 입력받은 키워드가 영어라면 그냥 바로 영어반환
    else:
        return keyword

from io import BytesIO
###### 실질적으로 크롤링하는 함수 크롤링할 이미지키워드와 개수 입력
def craw(keyword:str,find_image_count:int):
    chrome_options = Options()
    # chrome_options.add_experimental_option('detach',True) # 모니터 창이 안꺼지게 유지?
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')        # 디레토리 사용안하게?
    chrome_options.add_argument("--allow-running-insecure-content") #경고창 안드게?
    chrome_options.add_argument("--disable-gpu")
    
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

    
    
    driver.implicitly_wait(5) 
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

    keyword = trans(keyword)
    # 폴더 생성 
    
    # 검색창 찾기
    elem = driver.find_element(By.NAME, "q") # 검색창 태그 찾기
    elem.send_keys(keyword) # 검색창에 키워드 입력
    elem.send_keys(Keys.RETURN) # enter

    # 딜레이 타임
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 브라우저 끝까지 스크롤을 내리기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 1
    image_length = len(images)
    print("찾은 " + keyword + " 이미지 개수 : ", image_length)

    image_file_list=[]
    for i in range(image_length):
        print(i)
        if(count - 1 != find_image_count):
            try:
                images[i].click()
                print("Image Click!")                 
                imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute('src')                                                 
     
                response = requests.get(imgUrl)
                image_content = response.content
                image_file = BytesIO(image_content)
                
                count = count + 1
          
                image_file_list.append(image_file)
                print('이미지 저장')
##################### 예외 처리#################################################
            except HTTPError as e:
                print(e)
                pass
            except ElementClickInterceptedException as e:
                print(e)
                pass
            except NoSuchElementException as e:
                print(e)
                pass
            except ConnectionResetError as e:
                print(e)
                pass
            except URLError as e:
                print(e)
                pass
            except socket.timeout as e:           ## 송신에러 (시간 초과)
                print(e)
                pass
            except socket.gaierror as e:          ## 주소정보를 얻지 못햇을 경우 
                print(e)
                pass
            except ElementNotInteractableException as e:
                print(e)
                break
        else: break
    driver.close()
    return keyword,image_file_list



keyword , a = craw('강아지', 2)
print('#################')
print(a)