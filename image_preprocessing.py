import cv2
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# image가 저장되어 있는 곳의 경로를 인자로 받으면 
# 해당 경로의 이미지를 읽어서 RGB2BGR로 이미지 처리 후 이미지 저장후 반환
# dir_path --> ex) 'cat_img_download'

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
def image_grid(cvt_images,image_length,main):
    Fig = plt.Figure(figsize=(12,5),dpi=100)
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