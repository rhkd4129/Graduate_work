from tkinter import*
import sadariLogic
import sadariprint




# pack(side =  "top",left,right,bottom,   padx = 20, pady 20)
# grid(column =0,row = 2)       gird(column = 2,row -0,rowspan =2 // columnspan = 2)
# place(x = 20, y =29// relx = 0.3 rely = 0.4 상대적 위치)
def sadariresultshow(sadariarray,ent_num,k):
       column =0
       row = k
       while True:
               #왼쪽 끝 줄일때
               if(row ==0):
                        #print("왼쪽 줄 끝입니다")
                        if(sadariarray[column+1][row] ==1):
                                #오른쪽다리가 있을떄
                                if(sadariarray[column][row+1] == 1):
                                        row = row+2
                                        column = column+1
                                        if(column ==11):
                                                break
                                        #print("오른쪽으로 이동하고 한칸 아래로",column,row)
                                #그냥 아래로
                                else:
                                        column = column+1
                                        if(column ==11):
                                                break
                                        #print("아래로이동",column,row)
                #오른쪽 끝 줄일때
               elif(row ==(ent_num*2)-2 ):
                        #print("오른쪽 끝줄입니다")
                        if(sadariarray[column+1][row] ==1):
                                        #왼쪽다리가 있을떄
                                        if(sadariarray[column][row-1] == 1):
                                                row = row-2
                                                column = column+1
                                                if(column ==11):
                                                       break
                                                #print("왼쪽으로 이동하고 한칸 아래로",column,row)
                                        #그냥 아래로
                                        else:
                                                column = column+1
                                                if(column ==11):
                                                        break
                                                #print("아래로이동",column,row)
               else:
                        #print("양옆에 공간이 있습니다")
                        if(sadariarray[column+1][row] ==1):

                                #오른쪽 다리가 있을 떄
                                if(sadariarray[column][row+1] == 1):
                                        row = row+2
                                        column = column+1
                                        if(column ==11):
                                                       break
                                        #print("오른쪽으로 이동하고 한칸 아래로",column,row)

                                #왼쪽다리가 있을때
                                elif(sadariarray[column][row-1] == 1):
                                        row = row-2
                                        column = column+1
                                        if(column ==11):
                                                       break
                                        #print("왼쪽으로 이동하고 한칸 아래로",column,row)

                                #그냥 아래로
                                else:
                                        column = column+1
                                        if(column ==11):
                                                break
                                        #print("아래로이동",column,row)
       return row



main = Tk()
main.title("window")

# 창안에 위젯들 삭제
def Clear():
    for w in main.place_slaves():
        w.destroy()


def GOClick():
    global ent_num
    global sadariarray
    sadariarray = []
    ent_num = int(ent.get())
    sadariarray = sadariLogic.SadariInit(ent_num)
    sadariLogic.printSadari(sadariarray, ent_num)
    Clear()
    main.geometry("800x500")
    main.option_add("*Font","맑은고딕 15")
    a=1

    for i in range(ent_num):
        i = Entry(main)
        i.place(x = 50*a,y =35)
        i.config(width = 6)
        a +=2
    a=1
    for i in range(ent_num):
        i = Entry(main)
        i.place(x = 50*a,y =370)
        i.config(width = 6)
        a +=2
    PlayBtn()
    BackBtn()
    swidth = ((ent_num-1)*100)+70
    c = Canvas(main, width = swidth, height=310)
    c.place(x = 50, y = 60)
    # sadariprint.PrintVline(c,ent_num)
    # sadariprint.PrintSadari(main, ent_num, sadariarray)




def PlayBtn():
    Playbtn = Button(main)
    Playbtn.config(text = "Play")
    Playbtn.place(x=50 , y = 450)
    Playbtn.config(command = PlayClick)

def BackBtn():
    Backbtn = Button(main)
    Backbtn.config(text = "Back")
    Backbtn.place(x = 120 , y = 450)
    Backbtn.config(command = BackClick)

def ResultBtn():
    ResultBtn = Button(main)
    ResultBtn.config(text = "결과")
    ResultBtn.place(x = 50, y = 450)
    ResultBtn.config(command = ResultClick)
def nrsort(nrlist):
    nrlist = nrlist
    nlist = []
    rlist = []
    nrlen = len(nrlist)
    print(nrlen)
    for i in range(nrlen):
        if i < nrlen/2:
            rlist.append(nrlist[i])
        else:
            nlist.append(nrlist[i])


    print(int(nrlen/4))
    for i in range(int(nrlen/4)):
        rlist[i], rlist[-1*(i+1)] = rlist[-1*(i+1)], rlist[i]
        nlist[i], nlist[-1*(i+1)] = nlist[-1*(i+1)], nlist[i]



    print(nlist)
    print(rlist)

    return nlist, rlist


def PlayClick():
    global ent_num
    global entList
    global nrlist
    i = 0
    entList=[]
    nrlist = []
    nlist = []
    rlist = []
    for x  in main.place_slaves():
        entList.append(x)

    # Entry의 텍스트를 모두 추출하는 부분
    # 아래에서 말고 위에서 하는 이유는 중간에 Clear()부분에서
    # Entry가 모두 제거되기 때문에 Clear() 뒤에 텍스트를 추출 못함
    # nrlist에 이름, 결과 모두 받음, 나중에 분류
    for x in entList:
        if str(type(x)) == "<class 'tkinter.Entry'>":
              nrlist.append(x.get())
    nlist, rlist = nrsort(nrlist)
    Clear()
    main.geometry("800x500")
    main.option_add("*Font","맑은고딕 15")

    # 이름 입력하는 부분
    a=1
    b=0
    for i in range(ent_num):
        i = Button(main, text = nlist[b])
        i.place(x = 50*a,y =25)
        # i.insert(0, nlist[b])
        i.config(width = 6)
        a +=2
        b+=1

  # 결과 입력하는 부분
    a=1
    b=0
    for i in range(ent_num):
        i = Entry(main)
        i.place(x = 50*a,y =370)
        i.insert(0, rlist[b])
        i.config(width = 6)
        a +=2
        b+=1

    swidth = ((ent_num-1)*100)+70
    c = Canvas(main, width = swidth, height=310)
    c.place(x = 50, y = 60)
    ResultBtn()
    sadariprint.PrintSadari(c, ent_num, sadariarray)



def BackClick():
    Clear()
    mainWindow()


def ResultClick():
    global entList
    global nrlist
    global resultlist  #결과값의 x좌표
    global rlist
    resultlist = []
    nlist = []
    rlist = []
    Clear()
    main.geometry("800x500")
    main.option_add("*Font","맑은고딕 15")
    i=0
    ResultLabel = Label(main, text = "결과")
    ResultLabel.place(x=50, y=25)
    nlist, rlist = nrsort(nrlist)

    k=0
    for x in range(ent_num):
        resultlist.append(sadariresultshow(sadariarray,ent_num,k))
        k = k+2

    #rlist 홀수 인덱스에 0추가
    k=1
    for x in range(ent_num-1):
        rlist.insert(k,0)
        k = k+2

    a=0
    for i in range(ent_num):
        i = Label(main, text=nlist[i])
        i.place(x = 150,y =135+(40*(a+1)))
        i.config(width = 6)
        a += 1

    a = 0
    for i in range(ent_num):
        i = Label(main,text = rlist[resultlist[i]])
        i.place(x = 350,y =135+(40*(a+1)))
        i.config(width = 6)
        a += 1

    rilstReset()


    #rilst 다시 원래대로
def rilstReset():
    global ent_num
    global rlist
    k=1
    for x in range(ent_num-1):
        del rlist[k]
        k = k+2
    return rlist


def mainWindow():
    main.geometry("400x400")
    main.option_add("*Font","맑은고딕 20")

    lab = Label(main)
    lab.config(text = "개수입력")
    lab.place(x = 145, y= 50)

    global ent
    ent = Entry(main)
    ent.place(x = 40, y= 80)


    GObtn = Button(main)
    GObtn.config(text="GO")
    GObtn.place(x = 160, y= 120)
    GObtn.config(command = GOClick)



mainWindow()


main.mainloop()
