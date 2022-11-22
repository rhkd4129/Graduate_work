import cv2
import matplotlib.pyplot as plt
import os


def filter_and_remove(dir_name:str,query:str,filter_size:int)->None:
  filtered_count =0
  try:
    for index,file_name in enumerate(os.listdir(dir_name)):
      file_path = os.path.join(dir_name,file_name)
      img = Image.open(file_path)
      if img.width <filter_size and img.height<filter_size:  ## 지정해준 필터사이즈보다 크면 
        img.close()                                          ## 먼저 이미지를 나가기하고
        os.remove(file_path)                                 ## 이미지제거
        print(f"{index} 이미지 제거 ")
        filtered_count +=1 
  except OSError as e:           ## 파일이 안열리는 것(손상된거 )예외처리 
      print(e)
      os.remove(file_path)       ## 이미지제거
      filtered_count +=1



def cvt_image_save(path:str)->list:# cat_img_download'
  files_names =  [name for name in os.listdir(path)]

  cvt_images=[]
  for i , file_name in enumerate(files_names):
    image = cv2.imread('cat_img_download/'+file_name)    
    cvt_image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cvt_images.append(cvt_image)

  return cvt_images
# images  = cvt_image_save('cat_img_download')
# plt.imshow(images[2])
# plt.show()
