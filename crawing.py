from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
from urllib.error import HTTPError,URLError
import time
import urllib.request
import os
import socket
import googletrans


# 크롬 웹드라이버 연결
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")


# 폴더 만드는 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('ERROR: Creating directory. ' +  directory)



# 키워드 입력
keyword = input("Keyword : ")

# 키워드가 영어가 아니면 영어로 번역 처리
if not 'a' <= keyword[0] <= 'z' or 'A' <= keyword[0] <='Z':
    translator = googletrans.Translator()
    result = translator.translate(keyword, dest='en')
    print(keyword + " => " + result.text)
    keyword = result.text

# 폴더 생성
createFolder('./' + keyword + '_img_download')

# 이미지 개수 입력
image_count = int(input("Image count : "))


# 검색창 찾기
elem = driver.find_element(By.NAME, "q") # 검색창 태그 찾기
elem.send_keys(keyword) # 검색창에 키워드 입력
elem.send_keys(Keys.RETURN) # enter


SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 브라우저 끝까지 스크롤을 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height




images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
image_limit = 10
print("찾은 " + keyword + " 이미지 개수 : ", len(images))




# 입력한 이미지 수만큼 출력되도록 403 forbidden에러는 넘어가는 방식
for i in range(len(images)):
    if(count - 1 != image_count):
        try:
            images[i].click()
            print("Image Click!")
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
            
            # png, jpg 구분하여 저장
            if imgUrl.split('.')[-1] == 'png':
                urllib.request.urlretrieve(imgUrl, "./" + keyword + "_img_download/" + keyword + str(count) + ".png")
                print("PNG Image saved : {}_{}.png".format(keyword, count))
            else:
                urllib.request.urlretrieve(imgUrl, "./" + keyword + "_img_download/" + keyword + str(count) + ".jpg")
                print("JPG Image saved : {}_{}.jpg".format(keyword, count))
            count = count + 1
        # 예외 처리
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