import cv2
import matplotlib.pyplot as plt
import os
# 이건 사용할지 안할지 모르지만 일단 만들어 둠 
# def filter_and_remove(dir_name:str,query:str,filter_size:int)->None:
#   filtered_count =0
#   try:
#     for index,file_name in enumerate(os.listdir(dir_name)):
#       file_path = os.path.join(dir_name,file_name)
#       img = Image.open(file_path)
#       if img.width <filter_size and img.height<filter_size:  ## 지정해준 필터사이즈보다 크면 
#         img.close()                                          ## 먼저 이미지를 나가기하고
#         os.remove(file_path)                                 ## 이미지제거
#         print(f"{index} 이미지 제거 ")
#         filtered_count +=1 
#   except OSError as e:           ## 파일이 안열리는 것(손상된거 )예외처리 
#       print(e)
#       os.remove(file_path)       ## 이미지제거
#       filtered_count +=1


###################################################################
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