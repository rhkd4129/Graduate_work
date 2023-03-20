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
    

########## 찾은 이미지에서 랜덤으로 index 설정하는 함수   ############
def image_index_shuffe(find_image_count,images_length):  
    random_choice=[]
    for i in range(find_image_count*2):
        random_index = random.randint(0,images_length-1)
        while random_index in random_choice:
                random_index = random.randint(0,images_length-1)
        random_choice.append(random_index)
    random_choice.sort()
    return random_choice



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
    image_length = len(images)
    print("찾은 " + keyword + " 이미지 개수 : ", image_length)
    ################################################
    #TODO: 원하는 이미지개수에서 랜덤으로 무작위 이미지 뽑기 

    #if shffle:
    #    random_index_list=image_index_shuffe(find_image_count,len(images))
    #    print(random_index_list)
    #    ################################################
    #    shffle_images_list=[]
    #    for index in random_index_list:
    #        shffle_images_list.append(images[index])
    #    image_length = len(shffle_images_list)
    ################################################
    # 입력한 이미지 수만큼 출력되도록 에러는 넘어가는 방식
    
    for i in range(image_length):
        print(i)
        if(count - 1 != find_image_count):
            try:
                #if shffle:shffle_images_list[i].click()
                #else:images[i].click()
                images[i].click()
                print("Image Click!")
                
                # imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
                #imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')                                          
                imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute('src')                                          
                
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




    

