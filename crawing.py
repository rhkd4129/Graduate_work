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
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from image_preprocessing import cvt_image_save
# 직접 코딩한 함수 임포트 



############ 폴더 만드는 함수########################
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            #해당 폴더 없으면 생성 
    except OSError:
        print ('ERROR: Creating directory. ' +  directory)
            # 예외 처리 


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





###### 실질적으로 크롤링하는 함수 크롤링할 이미지키워드와 개수 입력
def craw(keyword:str,image_count:int) -> tuple[str,float,int]:
    # 크롬 웹드라이버 연결
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

    keyword = trans(keyword)
    # 폴더 생성 
    createFolder('./' + keyword + '_img_download')
    
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

    print("찾은 " + keyword + " 이미지 개수 : ", len(images))
    
    # 입력한 이미지 수만큼 출력되도록 에러는 넘어가는 방식
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

    cvt_images =cvt_image_save(keyword+'_img_download')
    image_length = len(cvt_images)
     # 이미지 처리 후 저장 

    return keyword,cvt_images,image_length


# 크롤링해서 저장된 이미지를 그리는 함수 
def grid(cvt_images,image_length,main):
    Fig = plt.Figure(figsize=(13,5),dpi=100)
        # plt.figure()그림그릴 도화지 선언 같은 역활

    for x in range(image_length):
        ax = Fig.add_subplot(1,image_length,x+1)
            # Fig(도화지)에 subplot을 추가하는데, 도화지에 여러개의 그림을 그릴려고 할때 사용
            # add_subplot(x,y,z) => (1,3,1)은 1*3 행렬모양의 그래프 (3개)  맨마지막 1은 첫번째 그래프를 가리킴
            # 원문 보시길.. 
        ax.set_xticks([])
        ax.set_yticks([])
        # x축과 y레이블은 없는게 깔끔해서 없앰 
        one = FigureCanvasTkAgg(Fig,main)
        # 뭐 tkinter랑 같이쓸려면 써야 한대서  씀
        one.get_tk_widget().place(x=100,y=100)
        # 이것도??
        ax.imshow(cvt_images[x])

    

