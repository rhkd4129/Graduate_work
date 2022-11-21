import tkinter
from tkinter import *
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 6시 10분
main = Tk()

global search_image_entry
# global search_image_entry

global search_image_num
global number_num

image1 = cv2.imread('cat/1.jpg')    
image2 = cv2.imread('cat/2.png')    
image3 = cv2.imread('cat/3.jpg')    
image4 = cv2.imread('cat/4.jpg')    
  
images = [image1,image2,image3,image4]
cvt_images =[]
for image in images:
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cvt_images.append(image)
    
    



def Clear():
    for w in main.place_slaves():
        w.destroy()



def mainWindow():
    global  search_image_entry
    global  number_entry

    main.geometry("700x500")
    main.option_add("*Font","맑은고딕 20")
    main.title("window")


################ <---- 첫쨰줄 ---->  ################################

    search_image_lbl = Label(main)
    search_image_lbl.config(text = "search_image")
    search_image_lbl.place(x = 400, y= 80)


    search_image_entry = Entry(main)
    search_image_entry.place(x = 40, y= 80)



################ <---- 두번째 줄 ---->  ################################
    number_lbl = Label(main)
    number_lbl.config(text = "number")
    number_lbl.place(x = 400, y= 150)

    number_entry = Entry(main)
    number_entry.place(x = 40, y= 150)
    
################ <---- 세번째 줄 ---->  ################################    


    GObtn = Button(main)
    GObtn.config(text="GO")
    GObtn.place(x = 400, y=250)
    GObtn.config(command = GOClick)


def GOClick():
    global search_image_entry
    global number_num

    search_image_num = str(search_image_entry.get())
    Clear()
  
 
    Fig = plt.Figure(figsize=(13,5),dpi=100)

    for x in range(len(cvt_images)):
        ax = Fig.add_subplot(1,5,x+1)
        ax.set_xticks([])
        ax.set_yticks([])
        one = FigureCanvasTkAgg(Fig,main)
        one.get_tk_widget().place(x=100,y=100)
        ax.imshow(cvt_images[x])
    

    main.geometry("1800x700")
    main.option_add("*Font","맑은고딕 15")
    




mainWindow()
main.mainloop()