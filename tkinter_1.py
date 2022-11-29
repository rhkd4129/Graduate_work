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
#직접 코딩한 함수  임포트

duplication_words_dict={
    '사과':['apple','apologize'],
    '배':['ship','pear','stomach']
}


global search_image_entry
global number_entry
###########################################################################
main = Tk()
#########################
# 화면에 있는 (뭐 버튼이나 레이블)s같은 요소들을 제거하는 함수인데 
# 화면전환전에 사용하는 함수 
def Clear():
    for w in main.place_slaves():
        w.destroy()
<<<<<<< HEAD

##########################################################################
=======
#######################################################################
>>>>>>> 296829055ba07cf773316d8d22da986c10328c39
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
<<<<<<< HEAD

    search_image_lbl = Label(main,text='search_image')
=======
    search_image_lbl = Label(main)
    search_image_lbl.config(text = "search_image")
>>>>>>> 296829055ba07cf773316d8d22da986c10328c39
    search_image_lbl.place(x = 400, y= 80)
    # 레이블 상입과 안에  들어강 내용과 위치 
    search_image_entry = Entry(main)
    search_image_entry.place(x = 40, y= 80)
<<<<<<< HEAD
    # entry 삽입(입력하는 칸)
################ <---- 두번째 줄 ---->  ###############

    number_lbl = Label(main,text='number')
=======
    # entry 삽입
################ <---- 두번째 줄 ---->  ###############
    number_lbl = Label(main)
    number_lbl.config(text = "number")
>>>>>>> 296829055ba07cf773316d8d22da986c10328c39
    number_lbl.place(x = 400, y= 150)
    number_entry = Entry(main)
    number_entry.place(x = 40, y= 150)
################ <---- 세번째 줄 ---->  ###############
    GObtn = Button(main,text='GO')
    GObtn.place(x = 400, y=250)
    GObtn.config(command = GOClick)
############################################################################
def duplication_screen(search_image_name)->bool:
    main.geometry("700x400")
    lbl_1 = Label(main)
    lbl_1.config(text ='어떤 단어가 맞나요?')
    lbl_1.place(x = 200, y= 250)
    duplication_word_lbl = Label(main)
    duplication_word_lbl.config(text = search_image_name+'가 중의적 표현입니다')
    duplication_word_lbl.place(x = 200, y= 50)

    duplication_words_length = len(duplication_words_dict[search_image_name])
    duplication_words = duplication_words_dict[search_image_name]

    # 동음의어가 두개라면 프레임에 맞게 x좌표 설정하고 3개라면 좀 더 x좌표를 좁게 설정
    # 4개인 경우는 아직 못봐서 우선 2개 아님 3개만 
    if duplication_words_length ==2 :x=130  
    else:x=30
    
    btn_dict ={}
    for i,duplication_word_btn in enumerate(duplication_words):
        keyword = duplication_word_btn
        print(type(keyword),keyword)

        btn_dict[duplication_word_btn] = Button(main)
        btn_dict[duplication_word_btn].config(text=duplication_words_dict[search_image_name][i])#,state='disabled'
        btn_dict[duplication_word_btn].place(x = x+40, y=150)

        # FIXME: 
        # 사과를 입력했다면 appple apologize 2개의 버튼이 생성은 되지만 각 버튼을 눌렀을때 해당 키워드가 크롤링되어야 한다,
        # 그러기 위해서 각 버튼에 event를 걸어야 하는데 그게 문제 
        
        # keyword,cvt_images,cvt_images_length =  duplication_word_btn.config(commend = craw(keyword,number_entry_num,inputType='ko'))
        #return_value = duplication_word_btn.config(command=Click('aaa'))
        # a = duplication_word_btn.bind('<Button-1>',(lambda event,x: print(x)))

        x+=200  ## 버튼이 일정 간격들 두고 생성
    main.option_add("*Font","맑은고딕 15")
    return True
###########################################################################
###########################################################################
def GOClick(): 
    #go 버튼을 눌렀을시 
    global search_image_entry
    global number_entry        
    # 첫 페이지(mainWindow) enrty의 값을 읽고  이 함수에 사용해야 하기 때문에 전역변수로 설정
    search_image_name = str(search_image_entry.get())
    number_entry_num = int(number_entry.get())
    ## entry의 값을 읽어오기 각각 (문자와 숫자형으로)
    Clear()


    # 입력한 키워드가 동음의어인지 검사 
    if search_image_name in duplication_words_dict.keys():
<<<<<<< HEAD
        lbl_1 = Label(main,text='어떤 단어가 맞나요')
        lbl_1.place(x = 200, y= 250)
        main.geometry("700x400")
        main.option_add("*Font","맑은고딕 15")
        duplication_word_lbl = Label(main)
        duplication_word_lbl.config(text = search_image_name+'가 중의적 표현입니다')
        duplication_word_lbl.place(x = 200, y= 50)
        # 입력한 단어command=lambda 가 중의적 표현이라고 알려주기 
        # keyword 사과 
=======
        duplication_screen(search_image_name)
>>>>>>> 296829055ba07cf773316d8d22da986c10328c39

    #아니면 바로 크롤링
    else:
        #  keyword = search_image_name
         # 번역이 완료된 keyword    
         search_image_name,cvt_images,cvt_images_length = craw(search_image_name,number_entry_num)
         grid(cvt_images,cvt_images_length,main)
         main.geometry("1700x700")
         main.option_add("*Font","맑은고딕 15")
  
###########################################################################

mainWindow()
main.mainloop()