import cv2
import matplotlib.pyplot as plt
import os


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