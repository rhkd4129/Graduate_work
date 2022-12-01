import tkinter
from tkinter import *
from duplication_words_DB import duplication_words_dict
from crawing import craw
from image_preprocessing import image_grid
global search_image_entry
global number_entry

def Clear():
    for w in graduate_App.place_slaves():
        w.destroy()
#######################################################################

# 기본 메인 창
def mainWindow():
    global  search_image_entry
    global  number_entry

    graduate_App.geometry("700x500")                   # 창 크기 설정
    graduate_App.option_add("*Font","맑은고딕 20")      # 폰트와 픽셀 크기 
    graduate_App.title("window")                       # 창 제목
    
################ <---- 첫쨰줄 ---->  #################

    search_image_lbl = Label(graduate_App)
    search_image_lbl.config(text = "search_image")
    search_image_lbl.place(x = 400, y= 80)
    # 레이블 상입과 안에  들어강 내용과 위치 
    search_image_entry = Entry(graduate_App)
    search_image_entry.place(x = 40, y= 80)
    # entry 삽입
    
################ <---- 두번째 줄 ---->  ###############

    number_lbl = Label(graduate_App,text='number')
    number_lbl.place(x = 400, y= 150)
    number_entry = Entry(graduate_App)
    number_entry.place(x = 40, y= 150)

################ <---- 세번째 줄 ---->  ###############

    GObtn = Button(graduate_App,text='GO')
    GObtn.place(x = 400, y=250)
    GObtn.config(command = GOClick)

############################################################################

def duplication_screen_excute(search_image_name,number_entry_num):
    
    print(search_image_name,'를 크롤링 합니다 ')
    decide = input('yes or no?')
    if decide =='yes':pass
    else: return None
    search_image_name,cvt_images, image_length= craw(search_image_name,number_entry_num)
    Clear()
    graduate_App.geometry("1300x700")
    image_grid(cvt_images,image_length,graduate_App)



# 동음의어가 맞으면 실행됨
def duplication_screen(search_image_name,number_entry_num)->bool:
    graduate_App.geometry("700x400")
    lbl_1 = Label(graduate_App,text='어떤 단어가 맞나요?')
    lbl_1.place(x = 200, y= 250)

    duplication_word_lbl = Label(graduate_App,text=search_image_name+'가 동음이의어 입니다')
    duplication_word_lbl.place(x = 200, y= 50)

    duplication_words_length = len(duplication_words_dict[search_image_name])
    duplication_words = duplication_words_dict[search_image_name]

    # 동음의어가 두개라면 프레임에 맞게 x좌표 설정하고 3개라면 좀 더 x좌표를 좁게 설정
    # 4개인 경우는 아직 못봐서 우선 2개 아님 3개만 

    if duplication_words_length ==2 :x=130  
    else:x=30
    
    btn_dict ={}
    for i,duplication_word_btn in enumerate(duplication_words):
        print(type(duplication_word_btn),duplication_word_btn)
        btn_dict[duplication_word_btn] = Button(graduate_App,text=duplication_word_btn)
        btn_dict[duplication_word_btn].place(x = x+40, y=150)
        # btn_dict[duplication_word_btn].config(command = lambda : duplication_screen_excute(duplication_word_btn,number_entry_num))
        print(btn_dict[duplication_word_btn]['command'])
        x+=200  
    # btn_dict[duplication_word_btn].config(command = lambda : duplication_screen_excute(duplication_word_btn,number_entry_num))
    
    graduate_App.option_add("*Font","맑은고딕 15")
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
        duplication_screen(search_image_name,number_entry_num)

    #아니면 바로 크롤링
    else:
        #  keyword = search_image_name
         # 번역이 완료된 keyword    
         search_image_name,cvt_images,cvt_images_length = craw(search_image_name,number_entry_num)
         image_grid(cvt_images,cvt_images_length,graduate_App)
         graduate_App.geometry("1300x700")
         graduate_App.option_add("*Font","맑은고딕 15")
  
##########################################################################
graduate_App = Tk()
mainWindow()
graduate_App.mainloop()
#########################################################################