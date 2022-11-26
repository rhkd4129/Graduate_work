import tkinter

from tkinter import *

global search_image_entry    
global number_entry          

# 동음의어 사전 
duplication_words_dict={
    '사과':['apple','apologize'],
    '배':['ship','pear','stomach']
}

main = Tk()


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

def Clear():
    for w in main.place_slaves():
        w.destroy()

def duplication_word_valid(keyword):
    # 사전에서 입력한 키워드가 있는지 검사 
    if keyword in duplication_words_dict.keys():
        duplication_word_lbl = Label(main)
        duplication_word_lbl.config(text = keyword+'가 중의적 표현입니다')
        duplication_word_lbl.place(x = 200, y= 50)
        # 입력한 단어가 중의적 표현이라고 알려주기 
        # keyword 사과 
        buttons = []
        


        duplication_words_number = len(duplication_words_dict[keyword])
        duplication_words = duplication_words_dict[keyword]
        
        if duplication_words_number ==2 :x=130
        else:x=30

        for i,duplication_word_btn in enumerate(duplication_words):
            duplication_word_btn = Button(main)
            duplication_word_btn.config(text=duplication_words_dict[keyword][i])
            duplication_word_btn.place(x = x+40, y=150)
            duplication_word_btn.config()
            x+=200
        lbl_1 = Label(main)
        lbl_1.config(text ='어떤 단어가 맞나요?')
        lbl_1.place(x = 200, y= 250)



def GOClick():
    global search_image_entry
    global number_entry     
    keyword = str(search_image_entry.get())
    Clear()


    # 사전에서 입력한 키워드가 있는지 검사 
    if keyword in duplication_words_dict.keys():
        duplication_word_lbl = Label(main)
        duplication_word_lbl.config(text = keyword+'가 중의적 표현입니다')
        duplication_word_lbl.place(x = 200, y= 50)
        # 입력한 단어가 중의적 표현이라고 알려주기 
        # keyword 사과 
     
        


        duplication_words_number = len(duplication_words_dict[keyword])
        duplication_words = duplication_words_dict[keyword]
        
        if duplication_words_number ==2 :x=130
        else:x=30

        for i,duplication_word_btn in enumerate(duplication_words):
            duplication_word_btn = Button(main)
            duplication_word_btn.config(text=duplication_words_dict[keyword][i])
            duplication_word_btn.place(x = x+40, y=150)
            # duplication_word_btn.config(command=lambda  )
            x+=200
        lbl_1 = Label(main)
        lbl_1.config(text ='어떤 단어가 맞나요?')
        lbl_1.place(x = 200, y= 250)



    # 없으면 바로 크롤링으로 넘어감
    else:
        duplication_words_lbl = Label(main)
        duplication_words_lbl.config(text = '없다 이놈아')
        duplication_words_lbl.place(x = 300, y= 100)


    main.geometry("700x300")
    main.option_add("*Font","맑은고딕 15")



mainWindow()
main.mainloop()