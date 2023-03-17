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
import random

def image_index_shuffe(find_image_count,images_length):  
    random_choice=[]
    for i in range(find_image_count*2):
        random_index = random.randint(0,images_length-1)
        while random_index in random_choice:
                random_index = random.randint(0,images_length-1)
        random_choice.append(random_index)
    random_choice.sort()
    return random_choice



keyword, find_image_count = map(str,input('키워드와 이미지개수를 공백 구분하여 입력: ').split())
find_image_count = int(find_image_count)
imgUrls = []








chrome_options = Options()
#
# chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument('--headless')  #headless 모드 
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-gpu")  ##gpu 사용안하도록 설정


#크롭드라이버매니저를 통해서 크롭드라이버를 섳치(최신버전으로 자동으로 )
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)


driver.implicitly_wait(5)  #웹페이지가 로딩될때까지 5초는 기다림 
# driver.maximize_window()# 화면최대화
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")# 검색창 찾기
elem = driver.find_element(By.NAME, "q") # 검색창 태그 찾기
elem.send_keys(keyword) # 검색창에 키워드 입력
elem.send_keys(Keys.RETURN) 

enterSCROLL_PAUSE_TIME = 2
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

print("찾은 " + keyword + " 이미지 개수 : ", len(images))

count = 1

ranom_index_list = image_index_shuffe(find_image_count,len(images))
print(ranom_index_list)

for index in range(len(images)):
#for index in ranom_index_list:
    print(index)
    if(count -1 != find_image_count):
        try:
            images[index].click()
            print("Image Click!")
            
            # imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
            imgUrls.append(driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute('src'))
            print(imgUrls)
            count = count + 1
    #################### 예외 처리#################################################
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
    else:break
    driver.close()
print(imgUrls)