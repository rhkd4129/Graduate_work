import tkinter
from tkinter import *
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os



def cvt_image_save(dir_path:str)->list: 
  files_names =  [name for name in os.listdir(dir_path)]
  # dir_path의 경로로 들어가 (이미지)파일 저장
  print(files_names)

  cvt_images=[]
  # 이미지 처리 한 이미지 저장할 리스트
  for i , file_name in enumerate(files_names):
    
    path = os.path.join(dir_path,file_name)
    #인자로 받은 dir_path와 파일 이름을 결합하여 이미지 경로 생성
    # path ex) --> cat_img_download/1.jpg
    image = cv2.imread(path)
    # 이미지 읽은 후 저장
    cvt_image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cvt_images.append(cvt_image)
    # 이미지 변환 후 저장
  return cvt_images


# 크롤링해서 저장된 이미지를 그리는 함수 
def grid(cvt_images,image_length,main):
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



# 이건 랜덤으로 인덱스 뽑는건데 아직 사용은 안하고 만들어만 본거 추후에 
def random_idx(search_image_number,images_length) -> list:
    random_idx_list = []
    for _ in range(search_image_number):
        random_number = random.randint(0,images_length)
        random_idx_list.append(random_number)
    return random_idx_list

# cvt_images = cvt_image_save('graduate_work\hat_img_download')

main = Tk()

def mainWindow():
    # main.attributes("-fullscreen", True)
    main.attributes('-zoomed', True)
    # 창 크기 설정
    main.option_add("*Font","맑은고딕 20")
    # 폰트와 픽셀 크기 
    main.title("window")
    # 창 제목
################ <---- 첫쨰줄 ---->  #################

mainWindow()
main.mainloop()