import tkinter
from tkinter import *
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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




from crawing import craw,grid


duplication_words_dict={
    '사과':['apple','apologize'],
    '배':['ship','pear','stomach']
}

###########################################################################
main = Tk()
###########################################################################
global search_image_entry    # entry(입력창) 개체 여기에 get을 해서 entry에 입력한 값을 받아올 수 잇다.
global number_entry          # entry(입력창) 개체 



###########################################################################
# 화면에 있는 (뭐 버튼이나 레이블)s같은 요소들을 제거하는 함수인데 
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

    ################################################

    if search_image_name in duplication_words_dict.keys():
        lbl_1 = Label(main)
        lbl_1.config(text ='어떤 단어가 맞나요?')
        lbl_1.place(x = 200, y= 250)
        main.geometry("700x400")
        main.option_add("*Font","맑은고딕 15")
        duplication_word_lbl = Label(main)
        duplication_word_lbl.config(text = search_image_name+'가 중의적 표현입니다')
        duplication_word_lbl.place(x = 200, y= 50)
        # 입력한 단어command=lambda 가 중의적 표현이라고 알려주기 
        # keyword 사과 

        duplication_words_number = len(duplication_words_dict[search_image_name])
        duplication_words = duplication_words_dict[search_image_name]
        
        if duplication_words_number ==2 :x=130
        else:x=30
        
        for i,duplication_word_btn in enumerate(duplication_words):
            keyword = duplication_word_btn
            print(type(keyword),keyword)

            duplication_word_btn = Button(main)
            duplication_word_btn.config(text=duplication_words_dict[search_image_name][i])
            duplication_word_btn.place(x = x+40, y=150)
            # keyword,cvt_images,cvt_images_length =  duplication_word_btn.config(commend = craw(keyword,number_entry_num,inputType='ko'))
            #return_value = duplication_word_btn.config(command=Click('aaa'))
            a = duplication_word_btn.bind('<Button-1>',(lambda event,x: print(x)))
            print(a)
            x+=200
        main.geometry("1700x700")
        main.option_add("*Font","맑은고딕 15")

        # 없으면 바로 크롤링으로 넘어감
    else:
        keyword = search_image_name
            # 번역이 완료된 keyword
        keyword,cvt_images,cvt_images_length = craw(keyword,number_entry_num)
        grid(cvt_images,cvt_images_length,main)
            # 크롤링 하기 
            # keyword가 이후에도 쓰이기 떄문에 return으로 keyword 받아옴
        main.geometry("1700x700")
        main.option_add("*Font","맑은고딕 15")
# 이해안되면 물어보세욥
###########################################################################
def Click(text):
    print(text)
    return 10
def dr():
    main.geometry("1700x700")
    main.option_add("*Font","맑은고딕 15")

mainWindow()
main.mainloop()