import os
import sys
import socket
import time

from urllib.request import urlretrieve
from urllib.error import HTTPError,URLError
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image


sys.path.insert(0,'usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
# 창 안보이게 
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
# user agent 추가 
socket.setdefaulttimeout(30) #타임아웃 최대 30 
wd = webdriver.Chrome('chromedriver',options = chrome_options)


def click_and_save(dir_name:str,index:int,img:object,img_list_length:int) -> None:
  global scraped_count       

  print('click_and_save')
  try:
    img.click()                     
    time.sleep(2)  
    print('이미지클릭!')
    src = wd.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
    

    ## 이미지가 png,jpg인지 구분하여 저장 
    if src.split('.')[-1] =='png':  
        urlretrieve(src,dir_name+"/"+str(scraped_count+1)+".png")
        print(f"{index+1}/{img_list_length} PNG 이미지 저장")
    else:                          
        urlretrieve(src,dir_name+"/"+str(scraped_count+1)+".jpg")
        print(f"{index+1}/{img_list_length} JPG 이미지 저장")
    scraped_count+=1
    
###############################################  예외 처리 ############################################################
  except HTTPError as e:
        print(e)
        pass
  except ElementClickInterceptedException as e:
        print(e)
        pass
  except NoSuchElementException as e:
        print(e)
        pass


def scroll_down()->None:
  scroll_count  = 0                                                                         ## 스크롤을 내린 개수 
  button = False                                                                            ## button이 False면 아직 안눌린 상태
  while True:
    print(f"스크롤 다운 {scroll_count}")
    last_height = wd.execute_script("return document.body.scrollHeight")                    ## 현재 스크롤의 위치값을 반환
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")                    ##스크롤을 내리고 
    time.sleep(2)                                                                           ## js동작후 잠시 sleep() (로딩시간)
    scroll_count+=1                                                                        
 
    new_height = wd.execute_script("return document.body.scrollHeight")                     ## 새로운 스크롤의 위치를 반환
    if last_height == new_height:                                                           ## 스크롤전에 위치값과 내린 후의 위치값이 같다면(더 이상 내려갈 수 없는 상태 )
      print('페이지가 더이상 내려갈 수가 없습니다 ')
      print(last_height,new_height)
      if button is True:                                                                    ## 버튼이 눌러져 있는 상태라면 (이미 스크롤이 최대로 내려가서 버튼이 클릭된 상태)
        print('button이 눌렀으므로 나가기 ')                                                ## 나가기 
        break
      else:                                                                                                         ## 버튼이 눌러진 상태가 아니라면
        try:
          more_button  = wd.find_element(By.XPATH,'//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input')    ## button element요소 
          if more_button.is_displayed: 
            time.sleep(2) 
            print('버튼 클릭')
            button = True
        except NoSuchElementException as e:                              ## 버튼을 찾을 수 없으면 
          print(e)                                                       ## 사진 파일이 많지 않아 버튼이 아예 없는 경우도 존재
          print('버튼을 찾을 수 없다.')
          break                                                          ## 스크롤을 끝까지 내린 것이기 때문에 나가기



scraped_count = 0                ## 스크래핑 개수 

path = "./"                      ## 저장경로
query = input('검색어 입력:')    ## 검색할 image


dir_name = path+query            ## 저장할 디렉토리 이름
save_dir = dir_name             

if not os.path.exists(save_dir):       ###  저장할 디렉토리가 없으면 
  os.mkdir(save_dir)                   ###  디텍토리 생성
  print(f"[{dir_name}디렉토리 생성]")  

url = f'https://www.google.com/search?q={query}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiu7pL4_Jv7AhXEbd4KHfDPCY4Q_AUoAXoECAEQAw&biw=960&bih=936&dpr=1#imgrc=mTdY9XBEi_I7dM'
wd.get(url)
wd.maximize_window() #창을 최대화로  
div = wd.find_element(By.XPATH,'//*[@id="islrg"]/div[1]')                         #### 사진이 있는 div
img_list = div.find_elements(By.CSS_SELECTOR,'div.bRMDJf.islir > img') 

print(len(img_list),'개 이하로 크롤링 할 수 있습니다.')


#################################################################################################################################
while True:
  number = int(input('크롤링할 이미지 개수(0을 입력하면 숨겨진 그림까지 다 크롤링합니다(시간 소요 많음))'))
  if number <= len(img_list):
      img_list = img_list[:number]
      break                                                                     
  elif number == 0:                                                             ## number가 0이면 그냥 전체 크롤링
    scroll_down()                 
    break
  else: 
    print('크롤링 초과 다시 입력하세요 ')                

#################################################################################################################################

for index ,img in enumerate(img_list):                                
    try:
      click_and_save(dir_name,index,img,len(img_list))                            #### 실실적으로 이미지 클릭하여 저장하는 함수 

#################################################################################################################################
############################################# 예외 처리 ##########################################################################
#################################################################################################################################
    except ElementClickInterceptedException as e:
      print(e)
      wd.execute_script('window.scrollTo(0,window.scrollY+100')  ## 스크롤위치 재조정 
      time.sleep(2)                                              ## js 실행후 time 필요 
      click_and_save(dir_name,index,img,len(img_list))           ## 다시 시도 

    except NoSuchElementException as e:
      wd.execute_script('window.scrollTo(0,window.scrollY+100')
      time.sleep(1)
      click_and_save(dir_name,index,img,len(img_list))

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
    # except StaleElementReferenceException as e:

try:
  print('[스크래핑 종료(성공률:%.2f%%)]'% (scraped_count/len(img_list)*100.0)) 
except ZeroDivisionError as e:            # img_list가 0이면 0을 나눌수 없기 떄문에 예외처리
  print(e) 
  wd.quit()
    