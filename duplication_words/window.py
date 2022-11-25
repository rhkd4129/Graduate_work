import tkinter

from tkinter import *

global search_image_entry    
global number_entry          
duplication_words={
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

def GOClick():
    global search_image_entry
    global number_entry     
    search_image_name = str(search_image_entry.get())
    Clear()

    if search_image_name in duplication_words.keys():
        duplication_words_lbl = Label(main)
        duplication_words_lbl.config(text = search_image_name+'가 중의적 표현입니다')
        duplication_words_lbl.place(x = 300, y= 100)

        buttons = []
        

        words_number = len(duplication_words[search_image_name])
        x =20

        for i in range(words_number):
            search_image_name_btn = Button(main)
            search_image_name_btn.config(text=duplication_words[search_image_name][i])
            search_image_name_btn.place(x = x+150, y=250)
            search_image_name_btn.config()
            print(f'{ duplication_words[search_image_name][i]}   ',end = '')
        print('\n어떤 단어인가요?')
    else:
        duplication_words_lbl = Label(main)
        duplication_words_lbl.config(text = '없다 이놈아')
        duplication_words_lbl.place(x = 300, y= 100)


    main.geometry("800x800")
    main.option_add("*Font","맑은고딕 15")



mainWindow()
main.mainloop()