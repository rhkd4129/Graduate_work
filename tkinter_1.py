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
global search_image_entry
global number_entry

global search_image_num
global number_num

###########################################################################
def Clear():
    for w in main.place_slaves():
        w.destroy()
###########################################################################
def mainWindow():
    global  search_image_entry
    global  number_entry

    main.geometry("700x500")
    main.option_add("*Font","맑은고딕 20")
    main.title("window")


################ <---- 첫쨰줄 ---->  #################

    search_image_lbl = Label(main)
    search_image_lbl.config(text = "search_image")
    search_image_lbl.place(x = 400, y= 80)

    search_image_entry = Entry(main)
    search_image_entry.place(x = 40, y= 80)

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


###########################################################################
def GOClick():
    global search_image_entry
    global number_num_entry

    search_image_name = str(search_image_entry.get())
    number_entry_num = int(number_entry.get())
    Clear()

    lbl1 = Label(main)
    lbl1.config(text =number_entry_num )
    lbl1.place(x = 1500, y= 150)

    lbl2 = Label(main)
    lbl2.config(text =search_image_name )
    lbl2.place(x = 1500, y= 300)

    keyword = search_image_name
    keyword = crawing(keyword,number_entry_num)

    cvt_images =cvt_image_save(keyword+'_img_download')
    image_length = len(cvt_images)

    Fig = plt.Figure(figsize=(13,5),dpi=100)

    for x in range(image_length):
        ax = Fig.add_subplot(1,image_length,x+1)
        ax.set_xticks([])
        ax.set_yticks([])
        one = FigureCanvasTkAgg(Fig,main)
        one.get_tk_widget().place(x=100,y=100)
        ax.imshow(cvt_images[x])

    main.geometry("1800x700")
    main.option_add("*Font","맑은고딕 15")
    
###########################################################################



mainWindow()
main.mainloop()