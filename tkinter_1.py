import tkinter
from tkinter import *
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from image_preprocessing import cvt_image_save

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

from crawing import translate,crawing,createFolder
from image_preprocessing import cvt_image_save

###########################################################################
main = Tk()
###########################################################################
global search_image_entry    # entry(입력창) 개체 여기에 get을 해서 entry에 입력한 값을 받아올 수 잇다.
global number_entry          # entry(입력창) 개체 



###########################################################################
# 화면에 있는 (뭐 버튼이나 레이블)같은 요소들을 제거하는 함수인데 
# 화면전환전에 사용하는 함수 
def Clear():
    for w in main.place_slaves():
        w.destroy()

#######################################################################
# 기본 메인 창
def mainWindow():
    global  search_image_entry
    global  number_entry

    main.geometry("700x500")
    # 창 크기 설정
    main.option_add("*Font","맑은고딕 20")
    # 폰트와 픽셀 크기 
    main.title("window")
    # 창 제목


################ <---- 첫쨰줄 ---->  #################

    search_image_lbl = Label(main)
    search_image_lbl.config(text = "search_image")
    search_image_lbl.place(x = 400, y= 80)
    # 레이블 상입과 안에  들어강 내용과 위치 

    search_image_entry = Entry(main)
    search_image_entry.place(x = 40, y= 80)
    # entry 삽입
    
    
################ <---- 두번째 줄 ---->  ###############
    number_lbl = Label(main)
    number_lbl.config(text = "number")
    number_lbl.place(x = 400, y= 150)

    number_entry = Entry(main)
    number_entry.place(x = 40, y= 150)
    
################ <---- 세번째 줄 ---->  ###############
    GObtn = Button(main)
    GObtn.config(text="GO")
    GObtn.place(x = 400, y=250)
    GObtn.config(command = GOClick)

## 두번째 세번째줄도 그냥 레이블과, entry,버튼 삽입하고 위치정하는 거 
###########################################################################

# 첫 페이지에 GO 버튼을 누르면 실행되는 함수 이 함수가 실행되면 실질적으로 
# 크롤링과 이미지 저장 그래프 그리기가 실행된다.

def GOClick():
    global search_image_entry
    global number_entry        
    # 첫 페이지(mainWindow) enrty의 값을 읽고  이 함수에 사용해야 하기 때문에 전역변수로 설정
    search_image_name = str(search_image_entry.get())
    number_entry_num = int(number_entry.get())
    ## entry의 값을 읽어오기 각각 (문자와 숫자형으로)
    Clear()
    ## 화면 전환전에 사용하는 함수 위에서 entry의 값을 먼저 읽어오고
    ## 선언해야 된다. 아니면 값이 안받아와짐 

    # lbl1 = Label(main)
    # lbl1.config(text =number_entry_num )
    # lbl1.place(x = 1500, y= 150)
    # lbl2 = Label(main)
    # lbl2.config(text =search_image_name )
    # lbl2.place(x = 1500, y= 300)

    keyword = search_image_name
    # 번역이 완료된 keyword
    keyword = crawing(keyword,number_entry_num)
    # 크롤링 하기 
    # keyword가 이후에도 쓰이기 떄문에 return으로 keyword 받아옴

    cvt_images =cvt_image_save(keyword+'_img_download')

    # 이미지 처리 후 저장 
    image_length = len(cvt_images)

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
        # 

    main.geometry("1700x700")
    main.option_add("*Font","맑은고딕 15")


# 이해안되면 물어보세욥
###########################################################################

mainWindow()
main.mainloop()